from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bridge_monitor_guard.py ===

# 🛡️ Bridge Monitor Guard – Ensures the syncer and drop agent stay running, restarts if needed:
:
import threading
import time
import traceback
from bridge_file_syncer import sync_bridge_to_replit
from bridge_drop_agent import monitor_drop_folder

class BridgeMonitorGuard:
    def __init__(self):
        self.sync_thread = None
        self.drop_thread = None

    def start_guard(self):
        print("[Bridge Guard] 🧿 Starting bridge process monitor...")
        self.sync_thread = threading.Thread(target=self._run_syncer, daemon=True)
        self.drop_thread = threading.Thread(target=self._run_dropper, daemon=True)
        self.sync_thread.start()
        self.drop_thread.start()
        self._watch_threads()

    def _run_syncer(self):
        try:
            sync_bridge_to_replit()
        except Exception:
            print("[Bridge Guard] ❌ Syncer crashed.")
            traceback.print_exc()

    def _run_dropper(self):
        try:
            monitor_drop_folder()
        except Exception:
            print("[Bridge Guard] ❌ Drop Agent crashed.")
            traceback.print_exc()

    def _watch_threads(self):
        while True:
            if not self.sync_thread.is_alive():
                print("[Bridge Guard] 🔁 Restarting Syncer...")
                self.sync_thread = threading.Thread(target=self._run_syncer, daemon=True)
                self.sync_thread.start()
            if not self.drop_thread.is_alive():
                print("[Bridge Guard] 🔁 Restarting Drop Agent...")
                self.drop_thread = threading.Thread(target=self._run_dropper, daemon=True)
                self.drop_thread.start()
            time.sleep(10)

def log_event():ef drop_files_to_bridge():