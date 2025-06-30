from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_emotional_memory_logger_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
PERSONA_FILE = "data/persona_registry.json"
EMOTIONAL_MEMORY_FILE = "data/emotional_memory_log.json"
CHECK_INTERVAL = 300  # Every 5 minutes

# === Ensure data folder ===
os.makedirs("data", exist_ok=True)

# === Load personas ===
def load_personas():
    if os.path.exists(PERSONA_FILE):
        try:
            with open(PERSONA_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Load existing emotional memory log ===
def load_emotional_memory():
    if os.path.exists(EMOTIONAL_MEMORY_FILE):
        try:
            with open(EMOTIONAL_MEMORY_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

# === Save emotional memory log ===
def save_emotional_memory(logs):
    with open(EMOTIONAL_MEMORY_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Emotional Memory Updater ===
def update_emotional_memory():
    personas = load_personas()
    emotional_memory = load_emotional_memory()

    for p in personas:
        event = {
            "timestamp": datetime.now().isoformat(),
            "persona": p.get('name', 'Unknown'),
            "mood": p.get('mood', 'neutral'),
            "voice": p.get('voice', 'default')
        }
        emotional_memory.append(event)
        print(f"[EMOTIONAL MEMORY LOGGER]: Recorded mood for {p.get('name', 'Unknown')} → {p.get('mood', 'neutral')}")

    save_emotional_memory(emotional_memory)

# === Main Daemon Loop ===
def emotional_memory_logger_loop():
    print("[EMOTIONAL MEMORY LOGGER]: Running...")
    while True:
        try:
            update_emotional_memory()
        except Exception as e:
            print(f"[EMOTIONAL MEMORY LOGGER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    emotional_memory_logger_loop()

def log_event():ef drop_files_to_bridge():