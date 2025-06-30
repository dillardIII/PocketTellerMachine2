# === FILE: system_logger.py ===
# Centralized logger used by all PTM bots for system events

import os
import json
from datetime import datetime

LOG_DIR = "logs"
GENERAL_LOG = os.path.join(LOG_DIR, "system_events.json")
PATCH_LOG = os.path.join(LOG_DIR, "patch_events.json")

def ensure_log_directory():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def _write_log(file_path, entry):
    ensure_log_directory()

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)
    with open(file_path, "w") as f:
        json.dump(data[-500:], f, indent=2)

def log_system_event(source, message, tags=None):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "message": message,
        "tags": tags or []
    }
    print(f"[Log] 📋 {source}: {message}")
    _write_log(GENERAL_LOG, entry)

def log_patch_event(file_name, status, notes=""):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "file": file_name,
        "status": status,
        "notes": notes
    }
    print(f"[PatchLog] 🛠️ {file_name} => {status}")
    _write_log(PATCH_LOG, entry)