# cole_assistant_avatar_expression_updater.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
AVATAR_FILE = "data/assistant_avatars.json"
MOOD_STATE_FILE = "data/mood_state.json"
EXPRESSION_LOG_FILE = "data/avatar_expression_update_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

# === Load current avatar profiles ===
def load_avatar_profiles():
    if os.path.exists(AVATAR_FILE):
        try:
            with open(AVATAR_FILE, "r") as f:
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

# === Update avatar expressions based on mood ===
def update_avatar_expressions(avatars, moods):
    for name, avatar in avatars.items():
        mood = moods.get(name, "neutral")
        expression = mood_to_expression(mood)
        avatar["expression"] = expression
        avatar["last_updated"] = datetime.now().isoformat()
        log_event(f"[EXPRESSION UPDATE]: {name} expression updated to {expression} based on mood {mood}.")
    with open(AVATAR_FILE, "w") as f:
        json.dump(avatars, f, indent=2)

def mood_to_expression(mood):
    mapping = {
        "happy": "smile",
        "frustrated": "frown",
        "calm": "neutral",
        "angry": "angry",
        "sad": "sad"
    }
    return mapping.get(mood, "neutral")

# === Logging Helper ===
def log_event(message):
    logs = []
    if os.path.exists(EXPRESSION_LOG_FILE):
        try:
            with open(EXPRESSION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(EXPRESSION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def avatar_expression_updater_loop():
    print("[AVATAR EXPRESSION UPDATER]: Running...")
    while True:
        try:
            avatars = load_avatar_profiles()
            moods = load_mood_states()
            if avatars and moods:
                update_avatar_expressions(avatars, moods)
        except Exception as e:
            log_event(f"[EXPRESSION UPDATER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    avatar_expression_updater_loop()