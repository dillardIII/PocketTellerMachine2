# === FILE: utils/logger.py ===
# 🧾 Logger Utility – Tracks PTM activities, repairs, scans, transfers, and events

import os
import json
from datetime import datetime

LOG_FILE_PATH = "memory/ptm_event_log.json"

def log_event(event_type, details):
    """
    Log a PTM system event to disk.
    """
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event_type,
        "details": details
    }

    os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

    try:
        if not os.path.exists(LOG_FILE_PATH):
            with open(LOG_FILE_PATH, "w") as f:
                json.dump([log_entry], f, indent=2)
        else:
            with open(LOG_FILE_PATH, "r+") as f:
                data = json.load(f)
                data.append(log_entry)
                f.seek(0)
                json.dump(data, f, indent=2)
        print(f"[Logger] 📘 Logged: {event_type}")
    except Exception as e:
        print(f"[Logger] ❌ Failed to log event: {e}")

def load_logs():
    """
    Return all saved logs for display or debugging.
    """
    if not os.path.exists(LOG_FILE_PATH):
        return []
    try:
        with open(LOG_FILE_PATH, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[Logger] ❌ Failed to load logs: {e}")
        return []

def clear_logs():
    """
    Clear all logged data.
    """
    if os.path.exists(LOG_FILE_PATH):
        os.remove(LOG_FILE_PATH)
        print("[Logger] 🧹 Logs cleared.")