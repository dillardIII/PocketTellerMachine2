from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_filter_scheduler.py ===

# ⏱️ GhostFilter Scheduler – Runs ghost_filter.scan() on a timed loop

import threading
import time
from ghost_filter import GhostFilter

def start_ghostfilter_daemon(interval_seconds=300):
    def loop():
        gf = GhostFilter()
        while True:
            print("[GhostFilterDaemon] 🔁 Running automated ghost scan...")
            gf.scan()
            time.sleep(interval_seconds)

    thread = threading.Thread(target=loop, daemon=True)
    thread.start()
    print(f"[GhostFilterDaemon] 🧭 Scheduler launched (every {interval_seconds} sec)")

def log_event():ef drop_files_to_bridge():