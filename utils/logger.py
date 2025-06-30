from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: utils/logger.py ===
# 📜 Logger – Safely logs PTM activity into system_log.json as a valid JSON list

import json
import os
from datetime import datetime

LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "system_log.json")

def log_event(event_type, data):
    # Ensure the logs folder exists
    os.makedirs(LOG_FOLDER, exist_ok=True)

    logs = []

    # Try to load existing log file if present
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except Exception as e:
            print(f"[Logger] ⚠️ Corrupted or empty log file. Starting fresh. Error: {e}")
            logs = []

    # Prepare new log entry
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": event_type,
        "data": data
    }

    logs.append(log_entry)

    # Attempt to write updated log list
    try:
        with open(LOG_FILE, "w") as f:
            json.dump(logs, f, indent=2)
        print(f"[Logger] ✅ Logged: {event_type}")
    except Exception as e:
        print(f"[Logger] ❌ Failed to write log: {e}")