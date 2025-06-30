from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: auto_sync_engine.py ===

import threading
import time
from wallet_sync_engine import WalletSyncEngine

def start_hourly_sync():
    def sync_job():
        while True:
            try:
                WalletSyncEngine().run_sync()
                print("[AutoSync] ✅ Synced wallets on schedule.")
            except Exception as e:
                print(f"[AutoSync] ❌ Error syncing: {e}")
            time.sleep(3600)  # Wait 1 hour

    thread = threading.Thread(target=sync_job, daemon=True)
    thread.start()

def log_event():ef drop_files_to_bridge():