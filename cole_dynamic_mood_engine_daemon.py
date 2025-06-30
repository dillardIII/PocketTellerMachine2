from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_dynamic_mood_engine_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_LOG_FILE = "data/persona_mood_log.json"
MOOD_STATE_FILE = "data/persona_mood_state.json"
CHECK_INTERVAL = 900  # Every 15 minutes

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Logging Helper ===
def log_mood_event(message):
    logs = []
    if os.path.exists(MOOD_LOG_FILE):
        try:
            with open(MOOD_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(MOOD_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load current moods ===
def load_mood_state():
    if not os.path.exists(MOOD_STATE_FILE):
        return {}
    try:
        with open(MOOD_STATE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

# === Update moods based on trade events or system health ===
def update_persona_moods():
    mood_state = load_mood_state()

    # Example: cycle moods randomly or based on mock inputs (could later tie to real events)
    for persona in ["Mo Cash", "Mentor", "Drill Instructor"]:
        current_mood = mood_state.get(persona, "neutral")
        if current_mood == "neutral":
            new_mood = "happy"
        elif current_mood == "happy":
            new_mood = "stressed"
        elif current_mood == "stressed":
            new_mood = "angry"
        else:
            new_mood = "neutral"

        mood_state[persona] = new_mood
        log_mood_event(f"[MOOD CYCLE]: {persona} mood changed to {new_mood}")

    # Save updated mood state
    with open(MOOD_STATE_FILE, "w") as f:
        json.dump(mood_state, f, indent=2)

# === Main Daemon Loop ===
def mood_engine_loop():
    print("[DYNAMIC MOOD ENGINE DAEMON]: Running...")
    while True:
        try:
            update_persona_moods()
        except Exception as e:
            log_mood_event(f"[ERROR]: {e}")
            print(f"[MOOD ENGINE ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run Daemon ===
if __name__ == "__main__":
    mood_engine_loop()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():