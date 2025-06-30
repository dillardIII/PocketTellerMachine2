from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_interaction_engine_daemon.py

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
INTERACTION_LOG_FILE = "data/avatar_interaction_log.json"
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

# === Simulate interactions between avatars ===
def simulate_avatar_interactions():
    avatars = load_avatars()
    avatar_list = list(avatars.keys())

    if len(avatar_list) < 2:
        return

    # Simple interaction simulation between avatars
    for i in range(len(avatar_list)):
        avatar_a = avatar_list[i]
        for j in range(i + 1, len(avatar_list)):
            avatar_b = avatar_list[j]
            mood_a = avatars[avatar_a].get("current_mood", "neutral")
            mood_b = avatars[avatar_b].get("current_mood", "neutral")
            interaction_result = determine_interaction(mood_a, mood_b)
            log_event(f"[INTERACTION]: {avatar_a} ({mood_a}) interacts with {avatar_b} ({mood_b}) → {interaction_result}")

# === Determine interaction result based on moods ===
def determine_interaction(mood_a, mood_b):
    if mood_a == mood_b:
        return "friendly exchange"
    elif mood_a == "happy" and mood_b == "frustrated":
        return "comforting interaction"
    elif mood_a == "frustrated" and mood_b == "happy":
        return "ignored by happy persona"
    else:
        return "neutral dialogue"

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(INTERACTION_LOG_FILE):
        try:
            with open(INTERACTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(INTERACTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def avatar_interaction_loop():
    print("[AVATAR INTERACTION ENGINE]: Running avatar interaction engine daemon...")
    while True:
        try:
            simulate_avatar_interactions()
        except Exception as e:
            log_event(f"[AVATAR INTERACTION ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    avatar_interaction_loop()