from ghost_env import INFURA_KEY, VAULT_ADDRESS
# system_status_reporter.py
# Purpose: Log hourly health snapshot of PTM system to keep a full audit trail

import os
import json
from datetime import datetime
from utils.logger import log_event

STATUS_LOG = "memory/system_status_log.json"
AUTONOMY_CONFIG = "autonomy_mode_config.json"
TRADE_STATS = "memory/trade_stats.json"
SHUTDOWN_FLAG = "memory/shutdown_triggered.json"
TRADE_LOG = "data/trades.json"

class SystemStatusReporter:
    def __init__(self):
        self.status_log = STATUS_LOG
        self.status = {
            "timestamp": str(datetime.now()),
            "autonomy_mode": "unknown",
            "fail_safe_triggered": False,
            "open_trades": 0,
            "daily_loss": 0.0,
            "drawdown_pct": 0.0,
            "consecutive_losses": 0,
            "voice_engine_status": "ok",
            "memory_status": "ok",
            "shutdown_flag": False,
            "errors": []
        }

    def check_autonomy_mode(self):
        try:
            with open(AUTONOMY_CONFIG, "r") as f:
                config = json.load(f)
            self.status["autonomy_mode"] = config.get("mode", "unknown")
        except Exception as e:
            self.status["errors"].append(f"Autonomy config error: {e}")

    def check_shutdown(self):
        self.status["shutdown_flag"] = os.path.exists(SHUTDOWN_FLAG)

    def check_trade_stats(self):
        try:
            with open(TRADE_STATS, "r") as f:
                stats = json.load(f)
            self.status["daily_loss"] = stats.get("daily_loss", 0.0)
            self.status["drawdown_pct"] = stats.get("drawdown_pct", 0.0)
            self.status["consecutive_losses"] = stats.get("consecutive_losses", 0)
        except Exception as e:
            self.status["errors"].append(f"Trade stats error: {e}")

    def count_open_trades(self):
        try:
            if os.path.exists(TRADE_LOG):
                with open(TRADE_LOG, "r") as f:
                    trades = json.load(f)
                self.status["open_trades"] = len([t for t in trades if t.get("status") != "closed"]):
        except Exception as e:
            self.status["errors"].append(f"Trade log read error: {e}")

    def run_report(self):
        self.check_autonomy_mode()
        self.check_shutdown()
        self.check_trade_stats()
        self.count_open_trades()

        log_event("System Status Report", self.status)
        self._save_snapshot()
        return self.status

    def _save_snapshot(self):
        if not os.path.exists(self.status_log):
            with open(self.status_log, "w") as f:
                json.dump([], f)

        with open(self.status_log, "r") as f:
            logs = json.load(f)

        logs.append(self.status)

        with open(self.status_log, "w") as f:
            json.dump(logs[-100:], f, indent=4)  # Keep only last 100 logs

# Run on demand or by hourly scheduler
if __name__ == "__main__":
    reporter = SystemStatusReporter()
    report = reporter.run_report()
    print(json.dumps(report, indent=4))