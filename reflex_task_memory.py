from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: reflex_task_memory.py ===

# 🧠 Reflex Task Memory – Tracks completed missions to avoid repetition

import os
import json

MEMORY_FILE = "vault/task_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory[-50:], f, indent=4)  # Keep last 50

def record_task(filename):
    memory = load_memory()
    if filename not in memory:
        memory.append(filename)
        save_memory(memory)

def is_repeat(filename):
    memory = load_memory()
    return filename in memory

def log_event():ef drop_files_to_bridge():