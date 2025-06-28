# === FILE: memory_mapper.py ===
# 🧠 Memory Mapper – Tracks, tags, and snapshots runtime memory for AI modules and bots

import json
import os
from datetime import datetime
from utils.logger import log_event

MEMORY_DIR = "memory"
MEMORY_MAP_FILE = f"{MEMORY_DIR}/memory_map.json"

class MemoryMapper:
    def __init__(self):
        self.memory_map = {}
        self._load_memory()

    def _load_memory(self):
        if not os.path.exists(MEMORY_MAP_FILE):
            self._save_memory()
        else:
            with open(MEMORY_MAP_FILE, "r") as f:
                self.memory_map = json.load(f)
        print("[MemoryMapper] ✅ Memory map loaded.")

    def _save_memory(self):
        os.makedirs(MEMORY_DIR, exist_ok=True)
        with open(MEMORY_MAP_FILE, "w") as f:
            json.dump(self.memory_map, f, indent=4)
        print("[MemoryMapper] 💾 Memory map saved.")

    def tag_memory(self, key, value):
        self.memory_map[key] = {
            "value": value,
            "timestamp": str(datetime.now())
        }
        self._save_memory()
        log_event("Memory Tag Updated", {key: value})

    def get_memory(self, key):
        return self.memory_map.get(key, {}).get("value")

    def snapshot_memory(self, label="snapshot"):
        snapshot_file = f"{MEMORY_DIR}/{label}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open