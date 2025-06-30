from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_speech_personality_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
AVATAR_PROFILE_FILE = "data/avatar_profiles.json"
AVATAR_SPEECH_LOG_FILE = "data/avatar_speech_personality_log.json"
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

# === Assign speech personality ===
def assign_speech_personalities():
    avatars = load_avatars()

    for avatar, profile in avatars.items():
        mood = profile.get("current_mood", "neutral")
        if mood == "happy":
            profile["speech_personality"] = "cheerful, energetic, optimistic"
        elif mood == "frustrated":
            profile["speech_personality"] = "stern, sharp, reactive"
        elif mood == "calm":
            profile["speech_personality"] = "soft, patient, balanced"
        else:
            profile["speech_personality"] = "neutral, default"
        profile["last_speech_update"] = datetime.now().isoformat()
        log_event(f"[SPEECH PERSONALITY]: {avatar} updated speech to {profile['speech_personality']}")

    save_avatars(avatars)

# === Save avatars ===
def save_avatars(avatars):
    with open(AVATAR_PROFILE_FILE, "w") as f:
        json.dump(avatars, f, indent=2)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(AVATAR_SPEECH_LOG_FILE):
        try:
            with open(AVATAR_SPEECH_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(AVATAR_SPEECH_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def avatar_speech_personality_loop():
    print("[AVATAR SPEECH PERSONALITY]: Running speech personality daemon...")
    while True:
        try:
            assign_speech_personalities()
        except Exception as e:
            log_event(f"[AVATAR SPEECH ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    avatar_speech_personality_loop()