# cole_dynamic_persona_avatar_selector_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
PERSONA_FILE = "data/avatar_personas.json"
AVATAR_MAP_FILE = "data/avatar_map.json"
SELECTION_LOG_FILE = "data/persona_avatar_selector_log.json"
CHECK_INTERVAL = 1800  # Every 30 minutes

os.makedirs("data", exist_ok=True)

# === Load personas and avatars ===
def load_personas():
    if os.path.exists(PERSONA_FILE):
        try:
            with open(PERSONA_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def load_avatar_map():
    if os.path.exists(AVATAR_MAP_FILE):
        try:
            with open(AVATAR_MAP_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def select_avatar_for_persona(personas, avatars):
    for name, props in personas.items():
        mood = props.get("mood", "neutral")
        culture = props.get("culture", "default")
        key = f"{mood}_{culture}"
        selected_avatar = avatars.get(key, avatars.get("default"))
        if selected_avatar:
            props["active_avatar"] = selected_avatar
            log_event(f"[AVATAR SELECTOR]: {name} assigned avatar {selected_avatar} based on {mood} & {culture}")
    with open(PERSONA_FILE, "w") as f:
        json.dump(personas, f, indent=2)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(SELECTION_LOG_FILE):
        try:
            with open(SELECTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(SELECTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Loop ===
def persona_avatar_selector_loop():
    print("[AVATAR SELECTOR DAEMON]: Running...")
    while True:
        try:
            personas = load_personas()
            avatars = load_avatar_map()
            if personas and avatars:
                select_avatar_for_persona(personas, avatars)
        except Exception as e:
            log_event(f"[AVATAR SELECTOR ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_avatar_selector_loop()