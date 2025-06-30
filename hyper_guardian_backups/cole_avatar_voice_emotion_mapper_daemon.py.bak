# cole_avatar_voice_emotion_mapper_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
AVATAR_PROFILE_FILE = "data/avatar_profiles.json"
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_EMOTION_LOG_FILE = "data/avatar_voice_emotion_log.json"
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

# === Update avatar voice tone based on mood ===
def update_avatar_voice_emotions():
    avatars = load_avatars()
    mood_states = load_mood_states()

    for avatar, profile in avatars.items():
        mood = mood_states.get(avatar, "neutral")
        voice_emotion = generate_voice_emotion_for_mood(mood)
        avatars[avatar]["voice_emotion"] = voice_emotion
        log_event(f"[VOICE EMOTION]: {avatar} voice tone set to '{voice_emotion}' (Mood: {mood})")

    with open(AVATAR_PROFILE_FILE, "w") as f:
        json.dump(avatars, f, indent=2)

# === Generate voice emotion based on mood ===
def generate_voice_emotion_for_mood(mood):
    if mood == "happy":
        return "cheerful and upbeat"
    elif mood == "frustrated":
        return "sharp and annoyed"
    elif mood == "calm":
        return "soft and steady"
    else:
        return "neutral"

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(VOICE_EMOTION_LOG_FILE):
        try:
            with open(VOICE_EMOTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_EMOTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def avatar_voice_emotion_mapper_loop():
    print("[AVATAR VOICE EMOTION MAPPER]: Running avatar voice emotion mapper daemon...")
    while True:
        try:
            update_avatar_voice_emotions()
        except Exception as e:
            log_event(f"[VOICE EMOTION ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    avatar_voice_emotion_mapper_loop()