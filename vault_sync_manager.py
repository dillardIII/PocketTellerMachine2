from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: vault_sync_manager.py ===
import os
import json
import time

VAULT_FILE = "ptm_vault.json"
DASHBOARD_FILE = "ptm_dashboard.json"

def sync_vault_to_dashboard():
    vault_data = {"eth_balance": 0}
    if os.path.exists(VAULT_FILE):
        with open(VAULT_FILE, "r") as f:
            vault_data = json.load(f)
    dashboard = {}
    if os.path.exists(DASHBOARD_FILE):
        with open(DASHBOARD_FILE, "r") as f:
            dashboard = json.load(f)
    dashboard["vault"] = vault_data
    dashboard["last_sync"] = time.ctime()
    with open(DASHBOARD_FILE, "w") as f:
        json.dump(dashboard, f, indent=2)
    print(f"[VaultSync] 🔗 Synced vault to dashboard at {dashboard['last_sync']}")

def vault_loop():
    while True:
        sync_vault_to_dashboard()
        time.sleep(15)

if __name__ == "__main__":
    vault_loop()

def log_event():ef drop_files_to_bridge():