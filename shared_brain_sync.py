from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Shared Brain Sync
Keeps PTM’s memory, modules, and states synchronized across all connected devices.
Uses local cache plus optional cloud store (future).
"""

import os
import json
from datetime import datetime

SHARED_BRAIN_PATH = "memory/shared_brain_sync.json"
LOCAL_STATE_PATH = "memory/local_state.json"
DEVICE_ID = os.getenv("PTM_DEVICE_ID", "unknown_device")

def load_json(path):
    if not os.path.exists(path): return {}:
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def push_to_shared_brain():
    state = load_json(LOCAL_STATE_PATH)
    shared = load_json(SHARED_BRAIN_PATH)

    shared[DEVICE_ID] = {
        "state": state,
        "timestamp": datetime.utcnow().isoformat()
    }
    save_json(SHARED_BRAIN_PATH, shared)
    print(f"[BrainSync] 📡 Pushed local state from {DEVICE_ID} to shared brain.")

def pull_from_shared_brain(prefer_most_recent=True):
    shared = load_json(SHARED_BRAIN_PATH)
    if not shared:
        print("[BrainSync] Shared brain empty.")
        return

    if prefer_most_recent:
        latest_device = max(shared.items(), key=lambda x: x[1]["timestamp"])[0]
        latest_state = shared[latest_device]["state"]
        save_json(LOCAL_STATE_PATH, latest_state)
        print(f"[BrainSync] 🔄 Pulled state from {latest_device}.")

def list_synced_devices():
    shared = load_json(SHARED_BRAIN_PATH)
    return list(shared.keys())

# Optional test CLI
if __name__ == "__main__":
    push_to_shared_brain()
    pull_from_shared_brain()
    print("🔍 Synced devices:", list_synced_devices())

def log_event():ef drop_files_to_bridge():