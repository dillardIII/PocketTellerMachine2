# === FILE: ghost_mesh.py ===
"""
Ghost Memory Mesh:
Shared memory interface between PTM AI personas.
Allows all bots to read/write to shared ghost memory.
"""

import os
import json
from datetime import datetime

GHOST_MEMORY_FILE = "data/ghost_memory.json"
os.makedirs(os.path.dirname(GHOST_MEMORY_FILE), exist_ok=True)

def _get_timestamp():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

def load_ghost_memory():
    if os.path.exists(GHOST_MEMORY_FILE):
        try:
            with open(GHOST_MEMORY_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_ghost_memory(memory):
    with open(GHOST_MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def log_ghost_event(actor, category, message, tags=None):
    entry = {
        "timestamp": _get_timestamp(),
        "actor": actor,
        "category": category,
        "message": message,
        "tags": tags or []
    }
    memory = load_ghost_memory()
    memory.append(entry)
    save_ghost_memory(memory)
    print(f"[GhostMesh] 🕸️ Logged by {actor}: {category} - {message}")

def recall_by_category(category):
    memory = load_ghost_memory()
    return [m for m in memory if m["category"] == category]

def recall_by_actor(actor):
    memory = load_ghost_memory()
    return [m for m in memory if m["actor"] == actor]

def clear_ghost_memory():
    save_ghost_memory([])
    print("[GhostMesh] 💀 Ghost memory cleared.")

# === Manual test
if __name__ == "__main__":
    log_ghost_event("Mentor", "strategy", "Recommended mean reversion strategy.")
    print("Memory Entries:", load_ghost_memory())