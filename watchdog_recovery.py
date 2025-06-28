# 🛡️ Watchdog Recovery – Detects system lockups and force restarts stuck modules

import os
import time
from datetime import datetime
from utils.logger import log_event

WATCHDOG_FILE = "bridge/status/heartbeat.txt"
CRITICAL_SCRIPTS = [
    "ghostforge_core.py",
    "reflex_engine.py",
    "command_listener.py",
    "vault_profit_trigger.py",
    "bridge_pickup_agent.py",
    "bridge_drop_agent.py"
]

TIMEOUT_SECONDS = 90  # time without heartbeat before triggering restart

def check_last_heartbeat():
    try:
        with open(WATCHDOG_FILE, "r") as f:
            line = f.readline().strip()
            if "PTM ALIVE" in line:
                timestamp = line.split(":")[-1].strip()
                return datetime.fromisoformat(timestamp)
    except Exception as e:
        log_event("Watchdog", {"error": str(e)})
    return None

def restart_critical_scripts():
    log_event("Watchdog", {"status": "🛠️ Restarting critical scripts..."})
    for script in CRITICAL_SCRIPTS:
        try:
            os.system(f"python {script} &")
            log_event("WatchdogRestart", {"file": script, "status": "✅ Restarted"})
        except Exception as e:
            log_event("WatchdogRestart", {"file": script, "error": str(e)})

def watchdog_loop():
    print("[Watchdog] 👁️ Monitoring PTM heartbeat...")
    while True:
        last_beat = check_last_heartbeat()
        if last_beat:
            elapsed = (datetime.utcnow() - last_beat).total_seconds()
            if elapsed > TIMEOUT_SECONDS:
                log_event("Watchdog", {"warning": "💀 Heartbeat timeout", "elapsed": elapsed})
                restart_critical_scripts()
        else:
            log_event("Watchdog", {"warning": "⚠️ No heartbeat found!"})
            restart_critical_scripts()

        time.sleep(30)

if __name__ == "__main__":
    watchdog_loop()