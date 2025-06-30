from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Autonomy Manifest Console
Visual + programmatic interface for checking active autonomy layers.

Displays status of:
- Bridge Listener
- Voice Command Handler
- GhostForge Evolution Loop
- Temporal Reflex System
- Assistant Command Council
"""

import json
import os
from datetime import datetime

MANIFEST_PATH = "memory/autonomy_status.json"

def update_status(layer, state):
    manifest = load_manifest()
    manifest[layer] = {
        "state": state,
        "updated": datetime.utcnow().isoformat()
    }
    save_manifest(manifest)

def load_manifest():
    if not os.path.exists(MANIFEST_PATH):
        return {}
    with open(MANIFEST_PATH, "r") as f:
        return json.load(f)

def save_manifest(data):
    with open(MANIFEST_PATH, "w") as f:
        json.dump(data, f, indent=2)

def show_manifest():
    manifest = load_manifest()
    print("\n🧭 AUTONOMY STATUS MANIFEST")
    print("=" * 35)
    for layer, info in manifest.items():
        print(f"🔹 {layer}: {info['state']} @ {info['updated']}")
    print("=" * 35 + "\n")

if __name__ == "__main__":
    show_manifest()