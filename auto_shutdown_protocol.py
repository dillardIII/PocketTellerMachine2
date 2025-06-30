from ghost_env import INFURA_KEY, VAULT_ADDRESS
# auto_shutdown_protocol.py
# Purpose: Autonomous shutdown system for PTM when critical conditions are hit

import os
import json
from datetime import datetime
from utils.logger import log_event
from core.voice_synthesizer import VoiceSynthesizer

SHUTDOWN_FLAG = "memory/shutdown_triggered.json"
STATS_FILE = "memory/trade_stats.json"
AUTONOMY_CONFIG = "autonomy_mode_config.json"

class AutoShutdownProtocol:
    def __init__(self):
        self.voice = VoiceSynthesizer()
        self.triggered = self.check_shutdown_flag()
        self.stats = self.load_stats()
        self.config = self.load_config()

    def check_shutdown_flag(self):
        return os.path.exists(SHUTDOWN_FLAG)

    def load_stats(self):
        if os.path.exists(STATS_FILE):
            with open(STATS_FILE, "r") as f:
                return json.load(f)
        return {}

    def load_config(self):
        if os.path.exists(AUTONOMY_CONFIG):
            with open(AUTONOMY_CONFIG, "r") as f:
                return json.load(f)
        return {}

    def should_shutdown(self):
        """Determine if shutdown should be triggered.""":
        loss = self.stats.get("daily_loss", 0)
        drawdown = self.stats.get("drawdown_pct", 0)
        streak = self.stats.get("consecutive_losses", 0)

        max_loss = self.config.get("fail_safe", {}).get("max_daily_loss", 1000)
        max_drawdown = self.config.get("fail_safe", {}).get("max_drawdown_pct", 10)
        max_streak = self.config.get("fail_safe", {}).get("max_consecutive_losses", 5)

        if loss >= max_loss or drawdown >= max_drawdown or streak >= max_streak:
            return True
        return False

    def trigger_shutdown(self, reason="Autonomous safety threshold breached."):
        if self.triggered:
            return False  # Already shut down

        data = {
            "timestamp": str(datetime.now()),
            "reason": reason
        }

        with open(SHUTDOWN_FLAG, "w") as f:
            json.dump(data, f, indent=4)

        log_event("Auto Shutdown Triggered", data)

        if self.config.get("voice_alert_on_shutdown", True):
            self.voice.generate_voice("GhostBot", "regretful", f"System has shut down. Reason: {reason}")

        self.triggered = True
        return True

    def lift_shutdown(self):
        """Manually clear shutdown flag."""
        if os.path.exists(SHUTDOWN_FLAG):
            os.remove(SHUTDOWN_FLAG)
            log_event("Auto Shutdown Lifted", {"timestamp": str(datetime.now()}})
        self.triggered = False

# Example usage
if __name__ == "__main__":
    protocol = AutoShutdownProtocol()
    if protocol.should_shutdown():
        protocol.trigger_shutdown("Thresholds exceeded.")
    else:
        print("System operating within safe range.")