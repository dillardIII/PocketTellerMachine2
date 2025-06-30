from ghost_env import INFURA_KEY, VAULT_ADDRESS
# ghost_executor.py
# Core listener for executing commands sent to the autonomous AI system.

import time
import json
from command_interpreter import interpret_command
from task_router import route_task
from status_sitrep import log_status

def listen_and_execute():
    print("👻 Ghost Executor Online. Awaiting Commands...")

    while True:
        try:
            with open("input_command.json", "r") as file:
                command_data = json.load(file)
                user_input = command_data.get("command", "").strip()

# === MELD BREAK ===
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