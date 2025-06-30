from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 🔐 Vault Sync Agent – Synchronizes vault files across all connected PTM devices

import os
import shutil
import time
from utils.logger import log_event

VAULT_DIR = "vault"
SYNCED_DIR = "bridge/vault_synced"
SYNC_INTERVAL = 60  # seconds

os.makedirs(VAULT_DIR, exist_ok=True)
os.makedirs(SYNCED_DIR, exist_ok=True)

def sync_vault_files():
    print("[VaultSync] 🔁 Starting vault sync loop...")
    while True:
        try:
            for filename in os.listdir(VAULT_DIR):
                source = os.path.join(VAULT_DIR, filename)
                target = os.path.join(SYNCED_DIR, filename)

                if os.path.isfile(source):
                    shutil.copy2(source, target)
                    log_event("VaultSync", {"synced": filename})
        except Exception as e:
            log_event("VaultSync", {"error": str(e)})

        time.sleep(SYNC_INTERVAL)

if __name__ == "__main__":
    sync_vault_files()