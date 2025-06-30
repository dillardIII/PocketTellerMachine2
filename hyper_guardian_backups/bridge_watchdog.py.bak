# === FILE: bridge_watchdog.py ===
# 🛡️ Bridge Watchdog – Monitors the bridge for new files, triggers execution, and logs events

import os
import time
from bridge_file_exec_engine import execute_incoming_files
from utils.logger import log_event

INBOX_FOLDER = "bridge/inbox"

def start_watchdog():
    print("[Replit Bot Installer] 🛠️ Watching for incoming files...")
    seen_files = set()

    while True:
        try:
            current_files = set([
                f for f in os.listdir(INBOX_FOLDER)
                if f.endswith(".py")
            ])

            new_files = current_files - seen_files
            if new_files:
                print(f"[Watchdog] 📥 Detected {len(new_files)} new file(s): {', '.join(new_files)}")
                execute_incoming_files()
                log_event("Watchdog Triggered", {"new_files": list(new_files)})
                seen_files.update(new_files)

            time.sleep(5)

        except Exception as e:
            print(f"[Watchdog] ❌ Error: {e}")
            time.sleep(10)