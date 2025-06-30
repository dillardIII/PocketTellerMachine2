from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_emotion_reactor_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
AVATAR_EMOTION_FILE = "data/avatar_emotion_state.json"
MOOD_STATE_FILE = "data/mood_state.json"
AVATAR_EMOTION_LOG_FILE = "data/avatar_emotion_reactor_log.json"
CHECK_INTERVAL = 300  # Every 5 minutes

os.makedirs("data", exist_ok=True)

# === Load current avatar emotion state ===
def load_avatar_emotion_state():
    if os.path.exists(AVATAR_EMOTION_FILE):
        try:
            with open(AVATAR_EMOTION_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Save avatar emotion state ===
def save_avatar_emotion_state(state):
    with open(AVATAR_EMOTION_FILE, "w") as f:
        json.dump(state, f, indent=2)

# === Load current mood state ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === React to mood changes ===
def react_to_mood_changes():
    mood_state = load_mood_state()
    avatar_state = load_avatar_emotion_state()

    for persona, mood in mood_state.items():
        avatar_state[persona] = {
            "expression": map_mood_to_expression(mood),
            "color_theme": map_mood_to_color(mood),
            "status": f"Reacted to mood {mood}"
        }
        log_event(f"[AVATAR EMOTION REACTOR]: {persona} avatar updated to expression {avatar_state[persona]['expression']} with color {avatar_state[persona]['color_theme']}")

    save_avatar_emotion_state(avatar_state)

def map_mood_to_expression(mood):
    mapping = {
        "happy": "smile",
        "frustrated": "frown",
        "calm": "neutral"
    }
    return mapping.get(mood, "neutral")

def map_mood_to_color(mood):
    mapping = {
        "happy": "green",
        "frustrated": "red",
        "calm": "blue"
    }
    return mapping.get(mood, "gray")

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(AVATAR_EMOTION_LOG_FILE):
        try:
            with open(AVATAR_EMOTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(AVATAR_EMOTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Daemon loop ===
def avatar_emotion_reactor_loop():
    print("[AVATAR EMOTION REACTOR]: Running...")
    while True:
        try:
            react_to_mood_changes()
        except Exception as e:
            log_event(f"[AVATAR EMOTION REACTOR ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    avatar_emotion_reactor_loop()