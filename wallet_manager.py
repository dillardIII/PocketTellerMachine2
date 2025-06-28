# === FILE: wallet_manager.py ===
# 🛠️ Wallet Manager – Reads and writes wallet data for PTM

import os
import json

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

    def delete_asset(self, asset):
        wallet = self.load_wallet()
        if asset in wallet:
            del wallet[asset]
            self.save_wallet(wallet)