from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: persona_sync_engine.py ===
# 🔄 Persona Sync – Ensures all AI personas share mood, assignments, memory

import json
import os

MOOD_FILE = "assistant_moods.json"
STRATEGY_FILE = "strategy_registry.json"
MEMORY_FILE = "ai_memory.json"

def sync_personas():
    print("[PersonaSync] 🔗 Starting full sync...")

    moods = json.load(open(MOOD_FILE)) if os.path.exists(MOOD_FILE) else {}:
    strategies = json.load(open(STRATEGY_FILE)) if os.path.exists(STRATEGY_FILE) else []:
    memory = json.load(open(MEMORY_FILE)) if os.path.exists(MEMORY_FILE) else {}:
:
    print(f"[PersonaSync] 🧠 {len(moods)} moods, {len(strategies)} strategies, {len(memory)} memory entries synced.")

    return {
        "moods": moods,
        "strategies": strategies,
        "memory": memory
    }

if __name__ == "__main__":
    sync_personas()

def log_event():ef drop_files_to_bridge():