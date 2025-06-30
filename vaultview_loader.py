from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: vaultview_loader.py ===
# 💰 Loads and displays wallet data inside VaultView for visual sync

def load_vault_view():
    try:
        with open("quantum_wallets.json", "r") as f:
            data = f.read()
            print("[VaultView] Wallets Loaded:")
            print(data)
    except:
        print("[VaultView] Wallet data not found.")

load_vault_view()

def log_event():ef drop_files_to_bridge():