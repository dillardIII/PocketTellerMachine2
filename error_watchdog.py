from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: error_watchdog.py ===

import os
import time
import traceback
import json

# Directory to monitor for log files
LOG_DIR = "./logs"
ERROR_LOG_FILE = "error_log.json"

# How often to scan for new logs (in seconds)
SCAN_INTERVAL = 5


def ensure_dirs():
    """Create log folder if it doesn't exist.""":
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)


def log_error(bot_id, error_info):
    """Append an error to the error log file."""
    entry = {
        "bot": bot_id,
        "timestamp": time.time(),
        "error": error_info
    }
    if not os.path.exists(ERROR_LOG_FILE):
        logs = []
    else:
        with open(ERROR_LOG_FILE, "r") as f:
            logs = json.load(f)

    logs.append(entry)

    with open(ERROR_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

    print(f"[Watchdog] 🚨 Error logged for {bot_id}.")


def monitor_logs():
    """Monitor logs for new errors (basic version)."""
    ensure_dirs()
    seen_files = set()

    while True:
        for filename in os.listdir(LOG_DIR):
            filepath = os.path.join(LOG_DIR, filename)
            if filepath not in seen_files:
                seen_files.add(filepath)
                try:
                    with open(filepath, "r") as f:
                        content = f.read()
                    if "Traceback" in content or "ERROR" in content:
                        log_error(filename.replace(".log", ""), content)
                except Exception as e:
                    log_error("watchdog", traceback.format_exc())
        time.sleep(SCAN_INTERVAL)


# Standalone runner
if __name__ == "__main__":
    print("[Watchdog] 🛡️ Starting log monitor...")
    monitor_logs()

def log_event():ef drop_files_to_bridge():