"""
Memory Weaver
Encodes context-aware reflection events into PTM's long-term memory structure.
Supports reinforcement, regret, correction, and insight preservation.
"""

import os
import json
from datetime import datetime

MEMORY_PATH = "memory/insight_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_PATH):
        return []
    with open(MEMORY_PATH, "r") as f:
        return json.load(f)

def save_memory(memories):
    with open(MEMORY_PATH, "w") as f:
        json.dump(memories[-250:], f, indent=2)

def weave_insight(event_type, description, related_nodes=[]):
    insight = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "description": description,
        "related_nodes": related_nodes
    }

    memory_log = load_memory()
    memory_log.append(insight)
    save_memory(memory_log)
    print(f"[MemoryWeaver] 🧠 Insight woven: {event_type} | {description}")
    return insight

def retrieve_by_event(event_type):
    memory_log = load_memory()
    return [entry for entry in memory_log if entry["event_type"] == event_type]