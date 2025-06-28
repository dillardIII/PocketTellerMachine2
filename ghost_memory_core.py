# === FILE: ghost_memory_core.py ===
# 🧠 Ghost Memory Core – Centralized memory for all major PTM events and experiences

import json
from datetime import datetime
from utils.logger import log_event

MEMORY_FILE = "memory/ghost_longterm_memory.json"

class GhostMemoryCore:
    def __init__(self):
        self.path = MEMORY_FILE
        self.memory = self.load()

    def load(self):
        try:
            with open(self.path, "r") as f:
                return json.load(f)
        except:
            return []

    def remember(self, category, data):
        memory_entry = {
            "timestamp": str(datetime.now()),
            "category": category,
            "data": data
        }
        self.memory.append(memory_entry)
        self.save()
        log_event(f"🧠 Memory saved: [{category}]")

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.memory, f, indent=4)

    def recall(self, category=None):
        if not category:
            return self.memory[-10:]  # Last 10
        return [m for m in self.memory if m["category"] == category][-5:]

# Example usage
if __name__ == "__main__":
    core = GhostMemoryCore()
    core.remember("TradeDecision", {"symbol": "NVDA", "decision": "HOLD"})
    print(core.recall("TradeDecision"))