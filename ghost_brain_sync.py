# === FILE: ghost_brain_sync.py ===
# 👻 Ghost Brain Sync – Stores & syncs persistent memories: trades, lessons, insights, mood changes

import os
import json
from pathlib import Path
from datetime import datetime

BRAIN_DIR = "ghost_brain"
MEMORY_FILE = os.path.join(BRAIN_DIR, "memory_log.json")

def init_ghost_brain():
    Path(BRAIN_DIR).mkdir(parents=True, exist_ok=True)
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump({"entries": []}, f, indent=2)
    print("[GhostBrain] 🧠 Initialized.")

def log_memory(entry_type, data):
    init_ghost_brain()
    timestamp = datetime.utcnow().isoformat()
    entry = {
        "type": entry_type,
        "timestamp": timestamp,
        "data": data
    }

    with open(MEMORY_FILE, "r+", encoding="utf-8") as f:
        memory = json.load(f)
        memory["entries"].append(entry)
        f.seek(0)
        json.dump(memory, f, indent=2)
        f.truncate()

    print(f"[GhostBrain] 📚 Memory logged: {entry_type} @ {timestamp}")

def get_memory(log_type=None):
    init_ghost_brain()
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)
    if log_type:
        return [entry for entry in memory["entries"] if entry["type"] == log_type]
    return memory["entries"]