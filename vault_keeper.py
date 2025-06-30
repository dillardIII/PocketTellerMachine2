from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: vault_keeper.py ===
import json
import os
from datetime import datetime

VAULT_LOG = "vault/vault_keeper_log.json"
WALLET_FILE = "vault/wallet_registry.json"
NFT_FILE = "vault/nft_registry.json"
LICENSE_FILE = "vault/license_registry.json"
DAO_FILE = "vault/dao_registry.json"

class VaultKeeper:
    def __init__(self, codename="Aurum"):
        self.name = codename
        self.vault_log = []
        self.assets = {
            "wallets": {},
            "nfts": {},
            "licenses": {},
            "dao": {}
        }
        self.load_all()

    def log(self, message):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "message": message
        }
        self.vault_log.append(entry)
        print(f"[{self.name}] {message}")
        self.save_logs()

    def save_logs(self):
        os.makedirs("vault", exist_ok=True)
        with open(VAULT_LOG, "w") as f:
            json.dump(self.vault_log[-100:], f, indent=2)

    def load_all(self):
        self.assets["wallets"] = self._load_json(WALLET_FILE)
        self.assets["nfts"] = self._load_json(NFT_FILE)
        self.assets["licenses"] = self._load_json(LICENSE_FILE)
        self.assets["dao"] = self._load_json(DAO_FILE)

    def _load_json(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                return json.load(f)
        return {}

    def show_all_assets(self):
        self.log("Displaying all stored vault assets:")
        for category, items in self.assets.items():
            print(f"\n🗂️ {category.upper()}")
            if not items:
                print("   No items found.")
                continue
            for k, v in items.items():
                print(f" - {k}: {v.get('description', 'No description')}")

    def get_wallet_value_estimate(self):
        total = 0.0
        for key, data in self.assets["wallets"].items():
            total += data.get("estimated_usd", 0)
        self.log(f"Total estimated wallet value: ${total:,.2f}")
        return total

    def sync_new_asset(self, category, asset_id, asset_data):
        if category in self.assets:
            self.assets[category][asset_id] = asset_data
            self.log(f"Synced new {category} asset: {asset_id}")
            self._save_registry(category)
        else:
            self.log(f"⚠️ Unknown asset category: {category}")

    def _save_registry(self, category):
        file_map = {
            "wallets": WALLET_FILE,
            "nfts": NFT_FILE,
            "licenses": LICENSE_FILE,
            "dao": DAO_FILE
        }
        if category in file_map:
            with open(file_map[category], "w") as f:
                json.dump(self.assets[category], f, indent=2)

# === Entrypoint ===
if __name__ == "__main__":
    aurum = VaultKeeper()
    aurum.show_all_assets()
    aurum.get_wallet_value_estimate()

def log_event():ef drop_files_to_bridge():