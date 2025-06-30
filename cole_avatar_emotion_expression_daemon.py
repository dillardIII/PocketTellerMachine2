from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_emotion_expression_daemon.py

import os
import json
import time
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)

# === Configurations ===
AVATAR_PROFILE_FILE = "data/avatar_profiles.json"
AVATAR_EXPRESSION_LOG_FILE = "data/avatar_emotion_expression_log.json"
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

# === Assign emotional expression ===
def assign_emotion_expressions():
    avatars = load_avatars()

    for avatar, profile in avatars.items():
        mood = profile.get("current_mood", "neutral")
        if mood == "happy":
            profile["expression"] = "smiling, bright eyes, enthusiastic gestures"
        elif mood == "frustrated":
            profile["expression"] = "frown, tight lips, defensive posture"
        elif mood == "calm":
            profile["expression"] = "relaxed face, gentle smile, open body language"
        else:
            profile["expression"] = "neutral face, default stance"
        profile["last_expression_update"] = datetime.now().isoformat()
        log_event(f"[EMOTION EXPRESSION]: {avatar} updated to {profile['expression']}")

    save_avatars(avatars)

# === Save avatars ===
def save_avatars(avatars):
    with open(AVATAR_PROFILE_FILE, "w") as f:
        json.dump(avatars, f, indent=2)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(AVATAR_EXPRESSION_LOG_FILE):
        try:
            with open(AVATAR_EXPRESSION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(AVATAR_EXPRESSION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def avatar_emotion_expression_loop():
    print("[AVATAR EMOTION EXPRESSION]: Running emotion expression daemon...")
    while True:
        try:
            assign_emotion_expressions()
        except Exception as e:
            log_event(f"[AVATAR EXPRESSION ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    avatar_emotion_expression_loop()