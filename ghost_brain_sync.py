# === FILE: ghost_brain_sync.py ===
# 👻 Ghost Brain Sync – Stores & syncs persistent memories: trades, lessons, insights, mood changes
# Cross-persona mood and memory harmonization layer for GhostNet

import os
import json
from pathlib import Path
from datetime import datetime

# === FILE & DIR PATHS ===
BRAIN_DIR = "ghost_brain"
MEMORY_FILE = os.path.join(BRAIN_DIR, "memory_log.json")
SYNC_FILE = "data/ghost_brain_sync.json"
MOODS_FILE = "data/persona_moods.json"

# === INIT STRUCTURE ===
def init_ghost_brain():
    Path(BRAIN_DIR).mkdir(parents=True, exist_ok=True)
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump({"entries": []}, f, indent=2)

    if not os.path.exists(SYNC_FILE):
        with open(SYNC_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2)

    if not os.path.exists(MOODS_FILE):
        with open(MOODS_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=2)

    print("[GhostBrain] 🧠 Initialized.")


# === MEMORY LOGGING ===
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


# === MOOD SYNC ===
def update_mood(persona, mood):
    init_ghost_brain()
    moods = load_moods()
    moods[persona] = {
        "mood": mood,
        "timestamp": datetime.utcnow().isoformat()
    }
    with open(MOODS_FILE, "w") as f:
        json.dump(moods, f, indent=4)
    print(f"[🌀 MOOD SYNC] {persona} is now feeling {mood}")


def load_moods():
    init_ghost_brain()
    if not os.path.exists(MOODS_FILE):
        return {}
    with open(MOODS_FILE, "r") as f:
        return json.load(f)


# === MEMORY EVENT BROADCAST ===
def broadcast_memory_event(event_type, content):
    init_ghost_brain()
    sync = load_brain_sync()
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "type": event_type,
        "content": content
    }
    sync.append(event)
    with open(SYNC_FILE, "w") as f:
        json.dump(sync, f, indent=4)
    print(f"[🧠 MEMORY BROADCAST] {event_type}: {content}")


def load_brain_sync():
    init_ghost_brain()
    if not os.path.exists(SYNC_FILE):
        return []
    with open(SYNC_FILE, "r") as f:
        return json.load(f)


# === TEST RUN HOOK ===
if __name__ == "__main__":
    update_mood("MoCash", "hype")
    broadcast_memory_event("trade_success", "Closed $TSLA with 9% gain")
    log_memory("trade_success", {"symbol": "TSLA", "result": "gain", "percent": 9})