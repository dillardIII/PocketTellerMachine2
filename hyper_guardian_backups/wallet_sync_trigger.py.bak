# 🔁 Wallet Sync Trigger – Auto-syncs wallet data and stores updated snapshots

import os
import json
import time
from wallet_manager import WalletManager
from utils.logger import log_event

SNAPSHOT_FILE = "vault/wallet_snapshot.json"
SYNC_INTERVAL = 300  # 5 minutes

def sync_wallets():
    try:
        wm = WalletManager()
        data = wm.get_wallet_summary()
        with open(SNAPSHOT_FILE, "w") as f:
            json.dump(data, f, indent=2)
        log_event("WalletSync", {"status": "✅ Synced wallet snapshot", "count": len(data)})
    except Exception as e:
        log_event("WalletSync", {"error": str(e)})

def wallet_sync_loop():
    print("[WalletSync] 💼 Starting wallet sync loop...")
    while True:
        sync_wallets()
        time.sleep(SYNC_INTERVAL)

if __name__ == "__main__":
    wallet_sync_loop()