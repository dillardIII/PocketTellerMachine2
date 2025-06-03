# === FILE: repair_team_watcher_loop.py ===
# Bravo Squad: Loop-enabled Repair Dispatcher

import time
from repair_team_watcher import handle_repo_requests

def start_repair_watch_loop(interval=120):
    print("[Bravo Squad] 🔄 Auto-trigger loop initialized.")
    while True:
        try:
            handle_repo_requests()
        except Exception as e:
            print(f"[Bravo Squad] ❌ Error in repair loop: {e}")
        time.sleep(interval)

if __name__ == "__main__":
    start_repair_watch_loop()