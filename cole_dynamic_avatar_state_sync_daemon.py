from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_dynamic_avatar_state_sync_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
AVATAR_PROFILE_FILE = "data/avatar_profiles.json"
MOOD_STATE_FILE = "data/mood_state.json"
STATE_SYNC_LOG_FILE = "data/avatar_state_sync_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data directory exists ===
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

# === Synchronize avatar mood and voice emotion ===
def sync_avatar_states():
    avatars = load_avatars()
    moods = load_mood_states()

    for avatar, profile in avatars.items():
        mood = moods.get(avatar, "neutral")
        profile["current_mood"] = mood
        profile["voice_emotion"] = generate_voice_emotion_for_mood(mood)
        log_event(f"[STATE SYNC]: {avatar} updated to Mood: {mood}, Voice: {profile['voice_emotion']}")

    with open(AVATAR_PROFILE_FILE, "w") as f:
        json.dump(avatars, f, indent=2)

# === Generate voice emotion based on mood ===
def generate_voice_emotion_for_mood(mood):
    if mood == "happy":
        return "cheerful"
    elif mood == "frustrated":
        return "gritty"
    elif mood == "calm":
        return "relaxed"
    else:
        return "neutral"

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(STATE_SYNC_LOG_FILE):
        try:
            with open(STATE_SYNC_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(STATE_SYNC_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def dynamic_avatar_state_sync_loop():
    print("[AVATAR STATE SYNC]: Running avatar state sync daemon...")
    while True:
        try:
            sync_avatar_states()
        except Exception as e:
            log_event(f"[STATE SYNC ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    dynamic_avatar_state_sync_loop()