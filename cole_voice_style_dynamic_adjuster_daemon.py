from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_voice_style_dynamic_adjuster_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
PERSONA_FILE = "data/avatar_personas.json"
VOICE_STYLE_MAP_FILE = "data/voice_style_map.json"
VOICE_LOG_FILE = "data/voice_style_adjuster_log.json"
CHECK_INTERVAL = 1800  # Every 30 minutes

os.makedirs("data", exist_ok=True)

# === Load persona data ===
def load_personas():
    if os.path.exists(PERSONA_FILE):
        try:
            with open(PERSONA_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def load_voice_styles():
    if os.path.exists(VOICE_STYLE_MAP_FILE):
        try:
            with open(VOICE_STYLE_MAP_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def adjust_voice_style_for_persona(personas, styles):
    for name, props in personas.items():
        mood = props.get("mood", "neutral")
        culture = props.get("culture", "default")
        key = f"{mood}_{culture}"
        selected_style = styles.get(key, styles.get("default"))
        if selected_style:
            props["active_voice_style"] = selected_style
            log_event(f"[VOICE ADJUSTER]: {name} voice style updated to {selected_style} based on {mood} & {culture}")
    with open(PERSONA_FILE, "w") as f:
        json.dump(personas, f, indent=2)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(VOICE_LOG_FILE):
        try:
            with open(VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Loop ===
def voice_style_adjuster_loop():
    print("[VOICE STYLE ADJUSTER DAEMON]: Running...")
    while True:
        try:
            personas = load_personas()
            styles = load_voice_styles()
            if personas and styles:
                adjust_voice_style_for_persona(personas, styles)
        except Exception as e:
            log_event(f"[VOICE STYLE ADJUSTER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    voice_style_adjuster_loop()