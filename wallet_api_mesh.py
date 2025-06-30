from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: wallet_api_mesh.py ===
# 🔄 PTM Wallet API Mesh – Merges wallet sources and feeds them into PTM systems

import os
import json
from wallet_config import WALLET_CONFIG

def fetch_all_balances():
    print("[WalletAPI] 🧲 Fetching all wallet balances...")
    balances = {}
    for wallet_name, wallet_info in WALLET_CONFIG.items():
        path = wallet_info.get("path")
        if not path:
            print(f"[WalletAPI] ⚠️ No path defined for wallet: {wallet_name}")
            continue

        if not os.path.exists(path):
            print(f"[WalletAPI] ❌ Wallet file missing: {path}")
            balances[wallet_name] = "Not found"
            continue

        try:
            with open(path, "r") as f:
                data = json.load(f)
                balances[wallet_name] = data.get("balance", "Unknown")
                print(f"[WalletAPI] ✅ {wallet_name} balance loaded.")
        except Exception as e:
            print(f"[WalletAPI] ❌ Error loading {wallet_name}: {e}")
            balances[wallet_name] = "Error"

    return balances


def log_event():ef drop_files_to_bridge():