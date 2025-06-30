from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_asset_locker.py ===
import os
import json
from datetime import datetime

LOCKER_FILE = "vault/ghost_asset_locker.json"

class GhostAssetLocker:
    def __init__(self):
        self.assets = {
            "nfts": {},
            "songs": {},
            "licenses": {},
            "contracts": {},
            "blueprints": {}
        }
        self.log = []
        self._load_assets()

    def _load_assets(self):
        if os.path.exists(LOCKER_FILE):
            with open(LOCKER_FILE, "r") as f:
                data = json.load(f)
                self.assets = data.get("assets", self.assets)
                self.log = data.get("log", self.log)
        else:
            self._save_assets()

    def _save_assets(self):
        os.makedirs("vault", exist_ok=True)
        with open(LOCKER_FILE, "w") as f:
            json.dump({"assets": self.assets, "log": self.log}, f, indent=2)

    def log_event(self, message):
        timestamp = datetime.utcnow().isoformat()
        entry = {"timestamp": timestamp, "message": message}
        self.log.append(entry)
        self._save_assets()
        print(f"[GhostLocker] {message}")

    def add_asset(self, category, asset_id, description, metadata=None):
        if category not in self.assets:
            self.log_event(f"⚠️ Unknown asset category: {category}")
            return
        self.assets[category][asset_id] = {
            "description": description,
            "metadata": metadata or {},
            "added": datetime.utcnow().isoformat()
        }
        self.log_event(f"🔐 Added new {category}: {asset_id}")
        self._save_assets()

    def list_assets(self, category=None):
        if category:
            return self.assets.get(category, {})
        return self.assets

    def show_summary(self):
        self.log_event("📦 Displaying asset summary:")
        for cat, items in self.assets.items():
            print(f"\n🗂️ {cat.upper()}: {len(items)} item(s)")
            for key, data in items.items():
                print(f" - {key}: {data['description']}")

# === Entrypoint ===
if __name__ == "__main__":
    locker = GhostAssetLocker()
    locker.show_summary()