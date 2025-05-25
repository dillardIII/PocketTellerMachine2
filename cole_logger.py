import os
import json
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "cole_system_log.json")

def log_info(message):
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.now().isoformat()

    log_entry = {
        "timestamp": timestamp,
        "level": "INFO",
        "message": message
    }

    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []

    logs.append(log_entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

    print(f"[{timestamp}] {message}")