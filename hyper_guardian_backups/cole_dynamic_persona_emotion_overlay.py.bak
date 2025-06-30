# cole_dynamic_persona_emotion_overlay.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
OVERLAY_LOG_FILE = "data/persona_emotion_overlay_log.json"
AVATAR_OVERLAY_MAP = {
    "Mentor": {
        "happy": "mentor_happy_overlay.png",
        "frustrated": "mentor_frustrated_overlay.png",
        "calm": "mentor_calm_overlay.png"
    },
    "Mo Cash": {
        "happy": "mo_cash_hype_overlay.png",
        "frustrated": "mo_cash_angry_overlay.png",
        "calm": "mo_cash_chill_overlay.png"
    },
    "Strategist": {
        "happy": "strategist_confident_overlay.png",
        "frustrated": "strategist_serious_overlay.png",
        "calm": "strategist_calm_overlay.png"
    }
}

# === Ensure data folder ===
os.makedirs("data", exist_ok=True)

def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def get_overlay_for_persona(persona):
    mood_state = load_current_mood_state()
    mood = mood_state.get(persona, "calm")
    overlay_file = AVATAR_OVERLAY_MAP.get(persona, {}).get(mood, "default_overlay.png")
    log_event(f"[EMOTION OVERLAY]: Persona '{persona}' mood '{mood}' will use overlay '{overlay_file}'")
    return overlay_file

def log_event(message):
    logs = []
    if os.path.exists(OVERLAY_LOG_FILE):
        try:
            with open(OVERLAY_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(OVERLAY_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

if __name__ == "__main__":
    # Example test
    get_overlay_for_persona("Mentor")
    get_overlay_for_persona("Mo Cash")
    get_overlay_for_persona("Strategist")