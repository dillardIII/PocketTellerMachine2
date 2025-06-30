from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: device_bridge.py ===
# 🌐 Device Bridge – Syncs PTM states, files, and configs across connected devices

import os
import json
import shutil
from pathlib import Path
from utils.logger import log_event

# Path where all synced data will live
SYNC_FOLDER = Path("device_sync")
DEVICE_LIST_FILE = SYNC_FOLDER / "authorized_devices.json"
SYNCED_STATE_FILE = SYNC_FOLDER / "synced_state.json"

class DeviceBridge:
    def __init__(self):
        self.devices = self.load_devices()
        self.ensure_sync_folder()
        log_event("🔗 Device Bridge initialized.")

    def ensure_sync_folder(self):
        if not SYNC_FOLDER.exists():
            SYNC_FOLDER.mkdir(parents=True)

    def load_devices(self):
        if not DEVICE_LIST_FILE.exists():
            return []
        with open(DEVICE_LIST_FILE, "r") as f:
            return json.load(f)

    def sync_to_all_devices(self, data):
        log_event(f"📡 Syncing data to {len(self.devices)} device(s).")
        for device in self.devices:
            device_path = Path(device["path"])
            if device_path.exists():
                try:
                    with open(device_path / "ptm_sync_payload.json", "w") as f:
                        json.dump(data, f, indent=4)
                    log_event(f"✅ Synced to {device['name']}")
                except Exception as e:
                    log_event(f"❌ Sync failed for {device['name']}: {e}")

        # Save latest snapshot
        with open(SYNCED_STATE_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def add_device(self, name, path):
        new_device = {"name": name, "path": path}
        self.devices.append(new_device)
        with open(DEVICE_LIST_FILE, "w") as f:
            json.dump(self.devices, f, indent=4)
        log_event(f"➕ Device added: {name}")

    def get_last_synced_state(self):
        if not SYNCED_STATE_FILE.exists():
            return {}
        with open(SYNCED_STATE_FILE, "r") as f:
            return json.load(f)

# Example Usage
if __name__ == "__main__":
    bridge = DeviceBridge()
    bridge.add_device("Z Fold 6", "/mnt/zfold6_ptm")
    bridge.sync_to_all_devices({"status": "Bridge Online", "time": "now"})