from ghost_env import INFURA_KEY, VAULT_ADDRESS
# 📜 System Manifest – Central registry of all PTM components and services

import json
import os

MANIFEST_PATH = "config/system_manifest.json"

DEFAULT_MANIFEST = {
    "core": [
        "ghostforge_core.py",
        "reflex_engine.py",
        "command_listener.py",
        "vault_profit_trigger.py",
        "ptm_error_handler.py",
        "ghostforge_autobuilder.py",
        "ghostforge_heartbeat.py"
    ],
    "bridge": [
        "bridge_pickup_agent.py",
        "bridge_drop_agent.py",
        "bridge_team_launcher.py"
    ],
    "bots": [
        "inspectorbot.py",
        "sweep_handler.py"
    ],
    "routes": [],
    "scripts": [],
    "ui": [],
    "voices": [],
    "vault": [],
    "config": [
        "system_manifest.py"
    ]
}

def load_manifest():
    if not os.path.exists(MANIFEST_PATH):
        save_manifest(DEFAULT_MANIFEST)
        return DEFAULT_MANIFEST
    with open(MANIFEST_PATH, "r") as f:
        return json.load(f)

def save_manifest(data):
    os.makedirs(os.path.dirname(MANIFEST_PATH), exist_ok=True)
    with open(MANIFEST_PATH, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    manifest = load_manifest()
    print("[Manifest] ✅ Loaded system manifest:")
    print(json.dumps(manifest, indent=2))

def log_event():ef drop_files_to_bridge():