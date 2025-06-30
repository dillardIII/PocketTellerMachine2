from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_voice_personality_selector_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
PERSONALITY_SETTINGS_FILE = "data/voice_personality_settings.json"
MOOD_STATE_FILE = "data/mood_state.json"
PERSONALITY_LOG_FILE = "data/voice_personality_selector_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(PERSONALITY_LOG_FILE):
        try:
            with open(PERSONALITY_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(PERSONALITY_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Load Personality Settings ===
def load_personality_settings():
    if os.path.exists(PERSONALITY_SETTINGS_FILE):
        try:
            with open(PERSONALITY_SETTINGS_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Load Mood States ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Assign Persona Personality Based on Mood ===
def assign_personality_to_mood():
    settings = load_personality_settings()
    moods = load_mood_state()

    for persona, mood in moods.items():
        selected_personality = mood_to_personality(mood)
        settings[persona] = {"current_personality": selected_personality}
        log_event(f"[VOICE PERSONALITY]: {persona} personality set to {selected_personality} based on mood {mood}")

    with open(PERSONALITY_SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=2)

def mood_to_personality(mood):
    if mood == "happy":
        return "Cheerful Mentor"
    elif mood == "frustrated":
        return "Tough Coach"
    elif mood == "calm":
        return "Zen Guide"
    else:
        return "Neutral Companion"

# === Main Daemon Loop ===
def voice_personality_selector_loop():
    print("[VOICE PERSONALITY SELECTOR]: Running voice personality selector daemon...")
    while True:
        try:
            assign_personality_to_mood()
        except Exception as e:
            log_event(f"[VOICE PERSONALITY SELECTOR ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    voice_personality_selector_loop()