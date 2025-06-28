# 🧠 GhostForge Memory Core – Stores, updates, and retrieves long-term bot memories

import json
import os
from utils.logger import log_event

MEMORY_PATH = "ghostforge_data/memory_core.json"

def init_memory():
    if not os.path.exists(MEMORY_PATH):
        os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
        with open(MEMORY_PATH, "w") as f:
            json.dump({}, f, indent=2)
        log_event("MemoryCore", {"status": "🆕 Initialized memory core"})

def load_memory():
    with open(MEMORY_PATH, "r") as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_PATH, "w") as f:
        json.dump(data, f, indent=2)
    log_event("MemoryCore", {"status": "✅ Saved memory core"})

def remember(key, value):
    data = load_memory()
    data[key] = value
    save_memory(data)
    log_event("MemoryCore", {"remembered": {key: value}})

def recall(key):
    data = load_memory()
    return data.get(key, None)

if __name__ == "__main__":
    init_memory()