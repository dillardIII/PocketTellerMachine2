# 🧿 Vault Sync Monitor – Ensures the vault stays synced across PTM devices

import os
import json
import time
from utils.logger import log_event
from datetime import datetime

VAULT_FILE = "vault/wallet_snapshot.json"
SYNC_LOG = "vault/sync_status.json"
CHECK_INTERVAL = 60  # check every 60 seconds

def get_vault_status():
    try:
        if not os.path.exists(VAULT_FILE):
            return {"status": "❌ No vault file"}

        mod_time = os.path.getmtime(VAULT_FILE)
        timestamp = datetime.utcfromtimestamp(mod_time).isoformat()
        size = os.path.getsize(VAULT_FILE)

        return {"status": "✅ Vault found", "last_modified": timestamp, "size": size}
    except Exception as e:
        return {"status": "❌ Error", "error": str(e)}

def save_sync_log(status):
    try:
        with open(SYNC_LOG, "w") as f:
            json.dump(status, f, indent=4)
    except Exception as e:
        log_event("VaultSync", {"error": str(e)})

def monitor_vault_sync():
    print("[VaultSyncMonitor] 🧿 Watching vault for updates...")
    while True:
        status = get_vault_status()
        log_event("VaultSync", status)
        save_sync_log(status)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_vault_sync()