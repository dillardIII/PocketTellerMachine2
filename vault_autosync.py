from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: vault_autosync.py ===

# 🔐 Vault AutoSync – Keeps vault data synced across devices or cloud

import shutil
import os
from datetime import datetime

def sync_vault(destination_folder="vault_backup"):
    os.makedirs(destination_folder, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    try:
        shutil.copytree("vault", f"{destination_folder}/vault_{timestamp}")
        print(f"[VaultAutoSync] 🔄 Vault snapshot saved: vault_{timestamp}")
    except Exception as e:
        print(f"[VaultAutoSync] ❌ Sync failed: {e}")

def log_event():ef drop_files_to_bridge():