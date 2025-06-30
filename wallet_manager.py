from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: wallet_manager.py ===
# 🛠️ Wallet Manager – Reads, writes, and logs wallet data for PTM

import os
import json
from datetime import datetime

class WalletManager:
    def __init__(self, snapshot_path="vault/wallet_snapshot.json"):
        self.snapshot_path = snapshot_path
        os.makedirs(os.path.dirname(self.snapshot_path), exist_ok=True)
        self._ensure_snapshot()

    def _ensure_snapshot(self):
        if not os.path.isfile(self.snapshot_path):
            with open(self.snapshot_path, "w") as f:
                json.dump({}, f, indent=2)

    def load_wallet(self):
        try:
            with open(self.snapshot_path, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"[WalletManager] ❌ Failed to load wallet: {e}")
            return {}

    def save_wallet(self, data):
        try:
            with open(self.snapshot_path, "w") as f:
                json.dump(data, f, indent=2)
            print("[WalletManager] 💾 Wallet saved.")
        except Exception as e:
            print(f"[WalletManager] ❌ Failed to save wallet: {e}")

    def update_asset(self, asset, amount):
        wallet = self.load_wallet()
        wallet[asset] = amount
        self.save_wallet(wallet)
        log_wallet_event("update_asset", {"asset": asset, "amount": amount})

    def delete_asset(self, asset):
        wallet = self.load_wallet()
        if asset in wallet:
            del wallet[asset]
            self.save_wallet(wallet)
            log_wallet_event("delete_asset", {"asset": asset})

# === Logging Enhancements ===

WALLET_LOG = "wallets/wallet_log.json"

def ensure_wallet_dir():
    os.makedirs("wallets", exist_ok=True)

def log_wallet_event(event_type, data):
    ensure_wallet_dir()
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "type": event_type,
        "data": data
    }

    if os.path.exists(WALLET_LOG):
        with open(WALLET_LOG, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(log_entry)

    with open(WALLET_LOG, "w") as f:
        json.dump(logs, f, indent=4)

    print(f"[WalletManager] 📝 Logged wallet event: {event_type}")

def log_event():ef drop_files_to_bridge():