from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_emotion_display_engine_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
AVATAR_PROFILE_FILE = "data/avatar_profiles.json"
MOOD_STATE_FILE = "data/mood_state.json"
EMOTION_DISPLAY_LOG_FILE = "data/avatar_emotion_display_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load avatars ===
def load_avatars():
    if os.path.exists(AVATAR_PROFILE_FILE):
        try:
            with open(AVATAR_PROFILE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Load current mood states ===
def load_mood_states():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Update avatar display based on mood ===
def update_avatar_displays():
    avatars = load_avatars()
    mood_states = load_mood_states()

    for avatar, profile in avatars.items():
        mood = mood_states.get(avatar, "neutral")
        display = generate_display_for_mood(mood)
        avatars[avatar]["display_emotion"] = display
        log_event(f"[EMOTION DISPLAY]: {avatar} displays emotion '{display}' (Mood: {mood})")

    with open(AVATAR_PROFILE_FILE, "w") as f:
        json.dump(avatars, f, indent=2)

# === Generate display based on mood ===
def generate_display_for_mood(mood):
    if mood == "happy":
        return "smiling face"
    elif mood == "frustrated":
        return "angry face"
    elif mood == "calm":
        return "neutral face"
    else:
        return "expressionless"

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(EMOTION_DISPLAY_LOG_FILE):
        try:
            with open(EMOTION_DISPLAY_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(EMOTION_DISPLAY_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def avatar_emotion_display_loop():
    print("[AVATAR EMOTION DISPLAY ENGINE]: Running avatar emotion display engine daemon...")
    while True:
        try:
            update_avatar_displays()
        except Exception as e:
            log_event(f"[AVATAR EMOTION DISPLAY ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    avatar_emotion_display_loop()