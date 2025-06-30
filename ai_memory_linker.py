from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
AI Memory Linker – Shared Memory Pool Across Assistants

Allows assistant personas to store, update, and recall long-term memory
across modules. Supports habit formation, trade memory, behavior adaption,
and assistant evolution.
"""

import json
import os
from datetime import datetime

MEMORY_FILE = "data/ai_long_term_memory.json"

def store_memory(source, topic, details):
    memory_event = {
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "topic": topic,
        "details": details
    }

    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump([], f)

    with open(MEMORY_FILE, "r") as f:
        memories = json.load(f)

    memories.append(memory_event)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memories, f, indent=4)

    print(f"[Memory] {source} stored new memory: {topic}")

def recall_memories(topic=None, limit=10):
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        memories = json.load(f)

    if topic:
        filtered = [m for m in memories if m["topic"] == topic]:
        return filtered[-limit:]
    else:
        return memories[-limit:]

def clear_memories():
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)
        print("[Memory] Long-term memory wiped.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():