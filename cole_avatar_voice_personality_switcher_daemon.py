from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_voice_personality_switcher_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
AVATAR_PROFILE_FILE = "data/avatar_profiles.json"
SWITCH_LOG_FILE = "data/avatar_personality_switch_log.json"
CHECK_INTERVAL = 1200  # Every 20 minutes

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

# === Switch voice personality dynamically ===
def switch_avatar_personality():
    avatars = load_avatars()

    for avatar, profile in avatars.items():
        old_voice = profile.get("voice_personality", "default")
        new_voice = generate_dynamic_voice_profile(avatar)
        profile["voice_personality"] = new_voice
        log_event(f"[VOICE SWITCH]: {avatar} switched voice from {old_voice} to {new_voice}")

    with open(AVATAR_PROFILE_FILE, "w") as f:
        json.dump(avatars, f, indent=2)

# === Dynamic voice generator logic (placeholder logic) ===
def generate_dynamic_voice_profile(avatar_name):
    # This would normally use AI mood logic or user settings.
    voices = ["energetic", "serious", "calm", "sarcastic", "cheerful", "bold"]
    return voices[hash(avatar_name + str(datetime.now())) % len(voices)]

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(SWITCH_LOG_FILE):
        try:
            with open(SWITCH_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(SWITCH_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def avatar_voice_personality_switcher_loop():
    print("[AVATAR VOICE SWITCHER]: Running voice personality switcher daemon...")
    while True:
        try:
            switch_avatar_personality()
        except Exception as e:
            log_event(f"[VOICE SWITCH ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    avatar_voice_personality_switcher_loop()