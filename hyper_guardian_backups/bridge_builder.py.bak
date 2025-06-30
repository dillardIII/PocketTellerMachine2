# === bridge_builder.py ===
"""
Bridge Builder – Autonomous Drop Zone Constructor
Creates and manages virtual bridge folders across PTM devices for syncing and code delivery.
"""

import os
import json
from datetime import datetime
from utils.logger import log_event

BRIDGE_CONFIG_PATH = "memory/bridge_config.json"
DEFAULT_BRIDGE_ROOT = "bridge_drops"

class BridgeBuilder:
    def __init__(self, persona="Spectra"):
        self.persona = persona
        self.config = self.load_config()
        self.ensure_directory(DEFAULT_BRIDGE_ROOT)

    def ensure_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
            log_event("Bridge Directory Created", {"path": path})
        return path

    def load_config(self):
        if not os.path.exists(BRIDGE_CONFIG_PATH):
            return {"bridges": []}
        with open(BRIDGE_CONFIG_PATH, "r") as f:
            return json.load(f)

    def save_config(self):
        with open(BRIDGE_CONFIG_PATH, "w") as f:
            json.dump(self.config, f, indent=2)

    def create_bridge(self, name, target_folder=None, purpose="sync"):
        timestamp = datetime.utcnow().isoformat()
        folder = target_folder or os.path.join(DEFAULT_BRIDGE_ROOT, name)
        self.ensure_directory(folder)

        bridge = {
            "name": name,
            "folder": folder,
            "purpose": purpose,
            "created_at": timestamp,
            "persona": self.persona
        }

        self.config["bridges"].append(bridge)
        self.save_config()
        log_event("Bridge Created", bridge)
        return bridge

    def list_bridges(self):
        return self.config.get("bridges", [])

if __name__ == "__main__":
    builder = BridgeBuilder()
    drop = builder.create_bridge("phase6_transfer")
    print(f"[BridgeBuilder] New drop zone created → {drop['folder']}")