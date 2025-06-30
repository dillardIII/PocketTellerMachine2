from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_emotional_expression_handler_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
EMOTION_LOG_FILE = "data/avatar_emotional_expression_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load current mood state ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Generate emotional expressions ===
def generate_emotional_expression(avatar, mood):
    if mood == "happy":
        return f"{avatar} smiles brightly and speaks with enthusiasm."
    elif mood == "frustrated":
        return f"{avatar} frowns slightly and uses a firmer tone."
    elif mood == "calm":
        return f"{avatar} maintains a neutral, soothing tone."
    else:
        return f"{avatar} shows no distinct emotion."

# === Update emotional expression ===
def update_emotional_expression():
    moods = load_mood_state()

    for avatar, mood in moods.items():
        expression = generate_emotional_expression(avatar, mood)
        log_event(f"[EMOTIONAL EXPRESSION]: {expression}")

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(EMOTION_LOG_FILE):
        try:
            with open(EMOTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(EMOTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def emotional_expression_loop():
    print("[AVATAR EMOTIONAL EXPRESSION]: Running daemon...")
    while True:
        try:
            update_emotional_expression()
        except Exception as e:
            log_event(f"[EMOTIONAL EXPRESSION ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    emotional_expression_loop()