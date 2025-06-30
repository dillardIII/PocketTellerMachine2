from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_dynamic_persona_speech_mood_daemon.py

import os
import json
import time
from datetime import datetime

# === Configuration ===
MOOD_LOG_FILE = "data/persona_mood_log.json"
PERSONA_CONFIG_FILE = "data/persona_profiles.json"
CHECK_INTERVAL = 300  # Every 5 minutes

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

# === Logging Helper ===
def log_persona_mood_event(message):
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

# === Load Persona Profiles ===
def load_persona_profiles():
    if not os.path.exists(PERSONA_CONFIG_FILE):
        return []
    try:
        with open(PERSONA_CONFIG_FILE, "r") as f:
            return json.load(f)
    except:
        return []

# === Adjust Persona Mood Based on System Triggers ===
def adjust_persona_moods():
    profiles = load_persona_profiles()
    updated_profiles = []
    for persona in profiles:
        mood = persona.get("current_mood", "neutral")
        # Example mood fluctuation logic
        if mood == "neutral":
            persona["current_mood"] = "curious"
        elif mood == "curious":
            persona["current_mood"] = "encouraging"
        elif mood == "encouraging":
            persona["current_mood"] = "critical"
        else:
            persona["current_mood"] = "neutral"
        
        log_persona_mood_event(f"[MOOD CYCLE]: {persona['name']} mood changed to {persona['current_mood']}")
        updated_profiles.append(persona)
    
    # Save updated moods
    with open(PERSONA_CONFIG_FILE, "w") as f:
        json.dump(updated_profiles, f, indent=2)

# === Main Daemon Loop ===
def persona_mood_cycle_daemon():
    print("[PERSONA MOOD DAEMON]: Running...")
    while True:
        try:
            adjust_persona_moods()
        except Exception as e:
            log_persona_mood_event(f"[ERROR]: {e}")
            print(f"[PERSONA MOOD ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run Daemon ===
if __name__ == "__main__":
    persona_mood_cycle_daemon()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():