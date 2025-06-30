from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_dynamic_voice_selector.py

import os
import json
from datetime import datetime

# === Configurations ===
AVATAR_VOICE_FILE = "data/avatar_voice_profiles.json"
VOICE_SELECTION_LOG_FILE = "data/avatar_dynamic_voice_selection_log.json"

# === Load avatar voice profiles ===
def load_avatar_voice_profiles():
    if os.path.exists(AVATAR_VOICE_FILE):
        try:
            with open(AVATAR_VOICE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Select voice for given persona ===
def select_voice_for_avatar(avatar_name):
    profiles = load_avatar_voice_profiles()
    if avatar_name in profiles:
        profile = profiles[avatar_name]
        log_event(f"[VOICE SELECTOR]: Selected voice for {avatar_name} → {profile['voice_id']}")
        return profile
    else:
        log_event(f"[VOICE SELECTOR]: No profile found for {avatar_name}. Using default.")
        return {"voice_id": "default_voice", "tone": "neutral", "speed": "moderate"}

# === Logging helper ===
def log_event(message):
    logs = []
    if os.path.exists(VOICE_SELECTION_LOG_FILE):
        try:
            with open(VOICE_SELECTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_SELECTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example usage ===
if __name__ == "__main__":
    test_avatars = ["Mo Cash", "Mentor", "OG", "Unknown Avatar"]
    for avatar in test_avatars:
        profile = select_voice_for_avatar(avatar)
        print(f"[TEST]: Avatar: {avatar} → Voice ID: {profile['voice_id']}, Tone: {profile['tone']}, Speed: {profile['speed']}")