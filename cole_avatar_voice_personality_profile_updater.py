# cole_avatar_voice_personality_profile_updater.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
PERSONALITY_FILE = "data/avatar_personalities.json"
MOOD_STATE_FILE = "data/mood_state.json"
PROFILE_LOG_FILE = "data/avatar_voice_profile_update_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data folder ===
os.makedirs("data", exist_ok=True)

# === Loaders ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def load_personality_profiles():
    if os.path.exists(PERSONALITY_FILE):
        try:
            with open(PERSONALITY_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Updater Logic ===
def update_personality_profiles():
    mood_state = load_mood_state()
    profiles = load_personality_profiles()

    for persona in profiles:
        mood = mood_state.get(persona, "calm")
        profiles[persona]["current_mood"] = mood
        profiles[persona]["voice_emotion"] = determine_voice_emotion(mood)
        log_event(f"[PROFILE UPDATER]: Updated {persona} mood to {mood} with voice emotion {profiles[persona]['voice_emotion']}")

    with open(PERSONALITY_FILE, "w") as f:
        json.dump(profiles, f, indent=2)

    return profiles

def determine_voice_emotion(mood):
    mapping = {
        "happy": "Cheerful",
        "frustrated": "Assertive",
        "calm": "Gentle"
    }
    return mapping.get(mood, "Gentle")

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(PROFILE_LOG_FILE):
        try:
            with open(PROFILE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(PROFILE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def profile_updater_loop():
    print("[PROFILE UPDATER]: Running avatar voice & personality updater...")
    while True:
        try:
            update_personality_profiles()
        except Exception as e:
            log_event(f"[PROFILE UPDATER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    profile_updater_loop()