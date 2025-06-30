from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: fix_logger.py ===

import os
import json
import time
from datetime import datetime

# === Log File Path ===
FIXES_LOG_FILE = "data/fixes_log.json"

# === Unified Fix Logger ===
def log_fix(error_info, fix_code):
    os.makedirs("data", exist_ok=True)

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "file": error_info.get("file") or error_info.get("file_path"),
        "error": error_info.get("error_message") or error_info.get("error"),
        "fix": fix_code
    }

    if os.path.exists(FIXES_LOG_FILE):
        try:
            with open(FIXES_LOG_FILE, "r") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
    else:
        logs = []

    logs.append(log_entry)

    with open(FIXES_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

    print(f"[Fix Logger] Logged fix for {log_entry['file']}")

# === Log Fix Entry (Alternative Format) ===
def log_fix_entry(file_path, error_message, fix_code):
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "file": file_path,
        "error": error_message,
        "fix": fix_code
    }

    os.makedirs(os.path.dirname(FIXES_LOG_FILE), exist_ok=True)

    try:
        if os.path.exists(FIXES_LOG_FILE):
            with open(FIXES_LOG_FILE, 'r') as f:
                log_data = json.load(f)
        else:
            log_data = []

        log_data.append(log_entry)

        with open(FIXES_LOG_FILE, 'w') as f:
            json.dump(log_data, f, indent=2)

        print(f"[Fix Logger] Logged fix for {file_path}")

    except Exception as e:
        print(f"[Fix Logger] Error logging fix: {e}")


def log_event():ef drop_files_to_bridge():