from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: core/shared_brain_sync.py ===
"""
Shared Brain Sync
Handles shared memory and cloud sync state across PTM installations (Z Fold 6, S10, Predator, Slate, etc.)
Facilitates distributed cognition, memory replay, and collaborative learning.
"""

import json
import os
from datetime import datetime

SHARED_STATE_FILE = "memory/shared_brain.json"

def load_shared_brain():
    if not os.path.exists(SHARED_STATE_FILE):
        return {"sync_log": [], "memory_core": {}}
    with open(SHARED_STATE_FILE, "r") as f:
        return json.load(f)

def save_shared_brain(data):
    with open(SHARED_STATE_FILE, "w") as f:
        json.dump(data, f, indent=2)

def sync_memory(key: str, content: str, source: str = "unknown"):
    brain = load_shared_brain()
    timestamp = datetime.utcnow().isoformat()

    # Memory sync core
    brain["memory_core"][key] = {
        "content": content,
        "source": source,
        "timestamp": timestamp
    }

    # Sync log for tracking
    brain["sync_log"].append({
        "key": key,
        "source": source,
        "timestamp": timestamp
    })

    # Cap log
    brain["sync_log"] = brain["sync_log"][-500:]
    save_shared_brain(brain)
    print(f"[SharedBrain] 🔗 Synced: {key} from {source}")

def replay_memory(key: str):
    brain = load_shared_brain()
    return brain.get("memory_core", {}).get(key, {}).get("content", None)

# Example use
if __name__ == "__main__":
    sync_memory("lesson_alpha", "Trade what you see, not what you feel.", "Mentor")