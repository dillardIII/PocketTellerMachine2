# cole_avatar_mood_adjuster_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
AVATAR_PROFILE_FILE = "data/avatar_profiles.json"
MOOD_STATE_FILE = "data/mood_state.json"
AVATAR_MOOD_LOG_FILE = "data/avatar_mood_adjuster_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load mood state ===
def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Load avatars ===
def load_avatars():
    if os.path.exists(AVATAR_PROFILE_FILE):
        try:
            with open(AVATAR_PROFILE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Adjust avatar mood ===
def adjust_avatar_moods():
    mood_state = load_current_mood_state()
    avatars = load_avatars()

    for avatar, profile in avatars.items():
        mood = mood_state.get(avatar, "calm")
        profile["current_mood"] = mood
        profile["last_mood_update"] = datetime.now().isoformat()
        log_event(f"[MOOD ADJUSTER]: {avatar} mood set to {mood}")

    save_avatars(avatars)

# === Save avatars ===
def save_avatars(avatars):
    with open(AVATAR_PROFILE_FILE, "w") as f:
        json.dump(avatars, f, indent=2)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(AVATAR_MOOD_LOG_FILE):
        try:
            with open(AVATAR_MOOD_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(AVATAR_MOOD_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def avatar_mood_adjuster_loop():
    print("[AVATAR MOOD ADJUSTER]: Running mood adjuster daemon...")
    while True:
        try:
            adjust_avatar_moods()
        except Exception as e:
            log_event(f"[AVATAR MOOD ADJUSTER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    avatar_mood_adjuster_loop()