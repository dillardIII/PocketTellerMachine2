from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: log_watcher.py ===
# 📡 Log Watcher – Monitors logs for new errors & sends to Self-Rebuilder

import os
import time
import traceback
from datetime import datetime
from error_parser import get_latest_error
from self_rebuilder import rebuild_from_latest_error

LOG_PATH = "logs/error.log"
CHECK_INTERVAL = 15  # seconds

def watch_logs_and_trigger_rebuild():
    print("[LOG-WATCHER] 📡 Watching logs for error signals...")
    last_mtime = 0

    while True:
        try:
            if os.path.exists(LOG_PATH):
                mtime = os.path.getmtime(LOG_PATH)
                if mtime != last_mtime:
                    print("[LOG-WATCHER] 🔄 Log change detected.")
                    result = rebuild_from_latest_error()
                    print(f"[LOG-WATCHER] 🛠 Repair result: {result}")
                    last_mtime = mtime
            time.sleep(CHECK_INTERVAL)
        except Exception as e:
            print(f"[LOG-WATCHER ERROR] ❌ {traceback.format_exc()}")
            time.sleep(CHECK_INTERVAL)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():