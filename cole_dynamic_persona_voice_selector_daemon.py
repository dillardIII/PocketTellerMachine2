# cole_dynamic_persona_voice_selector_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
PERSONA_FILE = "data/avatar_personas.json"
VOICE_MAP_FILE = "data/voice_map.json"
SELECTION_LOG_FILE = "data/persona_voice_selector_log.json"
CHECK_INTERVAL = 1800  # Every 30 minutes

os.makedirs("data", exist_ok=True)

# === Load personas and voices ===
def load_personas():
    if os.path.exists(PERSONA_FILE):
        try:
            with open(PERSONA_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def load_voice_map():
    if os.path.exists(VOICE_MAP_FILE):
        try:
            with open(VOICE_MAP_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def select_voice_for_persona(personas, voices):
    for name, props in personas.items():
        mood = props.get("mood", "neutral")
        culture = props.get("culture", "default")
        key = f"{mood}_{culture}"
        selected_voice = voices.get(key, voices.get("default"))
        if selected_voice:
            props["active_voice"] = selected_voice
            log_event(f"[VOICE SELECTOR]: {name} assigned voice {selected_voice} based on {mood} & {culture}")
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
def persona_voice_selector_loop():
    print("[VOICE SELECTOR DAEMON]: Running...")
    while True:
        try:
            personas = load_personas()
            voices = load_voice_map()
            if personas and voices:
                select_voice_for_persona(personas, voices)
        except Exception as e:
            log_event(f"[VOICE SELECTOR ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_voice_selector_loop()