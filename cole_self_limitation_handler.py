# cole_self_limitation_handler.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
ERROR_LOG_FILE = "data/ghost_log.json"
LIMITATION_TRIGGER_FILE = "data/self_limitation_state.json"
LIMITATION_LOG_FILE = "data/self_limitation_log.json"
CHECK_INTERVAL = 300  # Every 5 minutes
ERROR_THRESHOLD = 10  # Number of critical errors before limitation triggers

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_limitation_event(message):
    logs = []
    if os.path.exists(LIMITATION_LOG_FILE):
        try:
            with open(LIMITATION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(LIMITATION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load error logs ===
def load_critical_errors():
    if os.path.exists(ERROR_LOG_FILE):
        try:
            with open(ERROR_LOG_FILE, "r") as f:
                logs = json.load(f)
            return [log for log in logs if "CRITICAL ERROR" in log.get("message", "")]
        except:
            return []
    return []

# === Check and trigger self-limitation ===
def check_for_limitation_trigger():
    errors = load_critical_errors()
    if len(errors) >= ERROR_THRESHOLD:
        limitation_state = {"state": "LIMITATION_MODE", "reason": "Too many critical errors", "timestamp": datetime.now().isoformat()}
        with open(LIMITATION_TRIGGER_FILE, "w") as f:
            json.dump(limitation_state, f, indent=2)
        log_limitation_event("[SELF-LIMITATION]: Activated LIMITATION_MODE due to error threshold.")
        print("[SELF-LIMITATION]: Activated LIMITATION_MODE.")
    else:
        limitation_state = {"state": "NORMAL_MODE", "timestamp": datetime.now().isoformat()}
        with open(LIMITATION_TRIGGER_FILE, "w") as f:
            json.dump(limitation_state, f, indent=2)
        print("[SELF-LIMITATION]: System within normal thresholds.")

# === Main Daemon Loop ===
def self_limitation_loop():
    print("[SELF-LIMITATION HANDLER]: Active...")
    while True:
        try:
            check_for_limitation_trigger()
        except Exception as e:
            log_limitation_event(f"[SELF-LIMITATION ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    self_limitation_loop()