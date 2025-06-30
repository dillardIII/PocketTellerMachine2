from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Cole Logger:
Unified logging utility for PTM botnet systems.
Logs categorized events to rotating log files for each bot or service.
"""

import os
import json
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_log_file_path(source):
    """
    Generates a log file path based on the source.
    """
    filename = f"{source.lower().replace(' ', '_')}_log.json"
    return os.path.join(LOG_DIR, filename)

def log_event(source, message, level="info"):
    """
    Appends a log entry with timestamp and severity level.
    """
    log_entry = {
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "level": level.lower(),
        "source": source,
        "message": message
    }

    log_file = get_log_file_path(source)

    # Load existing logs or start new
    if os.path.exists(log_file):
        try:
            with open(log_file, "r") as f:
                logs = json.load(f)
                if not isinstance(logs, list):
                    logs = []
        except Exception:
            logs = []
    else:
        logs = []

    logs.append(log_entry)

    # Save back to disk
    try:
        with open(log_file, "w") as f:
            json.dump(logs, f, indent=2)
    except Exception as e:
        print(f"[Logger] ❌ Failed to write log: {e}")

    # Optional: also print(to console)
    print(f"[{level.upper()}] {source}: {message}")