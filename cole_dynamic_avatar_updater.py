from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_dynamic_avatar_updater.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
AVATAR_STATE_FILE = "data/avatar_state.json"
MOOD_STATE_FILE = "data/mood_state.json"
AVATAR_LOG_FILE = "data/avatar_update_log.json"
CHECK_INTERVAL = 600  # 10 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load avatar state ===
def load_avatar_state():
    if os.path.exists(AVATAR_STATE_FILE):
        try:
            with open(AVATAR_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Save avatar state ===
def save_avatar_state(avatar_state):
    with open(AVATAR_STATE_FILE, "w") as f:
        json.dump(avatar_state, f, indent=2)

# === Load mood state ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Update avatars based on mood ===
def update_avatars_based_on_mood():
    mood_state = load_mood_state()
    avatar_state = load_avatar_state()

    for persona, mood in mood_state.items():
        avatar_state[persona] = f"{persona}_{mood}_avatar"
        log_event(f"[AVATAR UPDATE]: {persona} avatar updated to {avatar_state[persona]} based on mood {mood}")

    save_avatar_state(avatar_state)
    return avatar_state

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(AVATAR_LOG_FILE):
        try:
            with open(AVATAR_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(AVATAR_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def avatar_updater_loop():
    print("[AVATAR UPDATER]: Starting avatar updater...")
    while True:
        try:
            update_avatars_based_on_mood()
        except Exception as e:
            log_event(f"[AVATAR UPDATER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    avatar_updater_loop()