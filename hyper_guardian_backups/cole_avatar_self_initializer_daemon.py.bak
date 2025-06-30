# cole_avatar_self_initializer_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
AVATAR_PROFILE_FILE = "data/avatar_profiles.json"
AVATAR_INIT_LOG_FILE = "data/avatar_self_initializer_log.json"
CHECK_INTERVAL = 900  # Every 15 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Avatar Initialization Logic ===
def load_existing_avatars():
    if os.path.exists(AVATAR_PROFILE_FILE):
        try:
            with open(AVATAR_PROFILE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def initialize_avatar(avatar_name, personality_traits, voice_id):
    avatars = load_existing_avatars()
    if avatar_name not in avatars:
        avatars[avatar_name] = {
            "personality_traits": personality_traits,
            "voice_id": voice_id,
            "created": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat()
        }
        save_avatars(avatars)
        log_event(f"[AVATAR INITIALIZER]: Created new avatar → {avatar_name}")
    else:
        log_event(f"[AVATAR INITIALIZER]: Avatar already exists → {avatar_name}")

def save_avatars(avatars):
    with open(AVATAR_PROFILE_FILE, "w") as f:
        json.dump(avatars, f, indent=2)

def log_event(message):
    logs = []
    if os.path.exists(AVATAR_INIT_LOG_FILE):
        try:
            with open(AVATAR_INIT_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(AVATAR_INIT_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Avatar Initialization Daemon Loop ===
def avatar_initializer_loop():
    print("[AVATAR INITIALIZER]: Running avatar initializer daemon...")
    while True:
        try:
            # Example avatars (can be dynamically loaded later)
            initialize_avatar("Mo Cash", ["confident", "fast-talking", "hustler"], "mo_cash_voice")
            initialize_avatar("Mentor", ["calm", "encouraging", "wise"], "mentor_voice")
            initialize_avatar("OG", ["old-school", "realistic", "strategist"], "og_voice")
        except Exception as e:
            log_event(f"[AVATAR INITIALIZER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    avatar_initializer_loop()