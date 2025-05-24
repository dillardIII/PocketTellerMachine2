# cole_persona_voice_mood_manager.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
PERSONA_STATE_FILE = "data/persona_current_state.json"
MOOD_VOICE_LOG_FILE = "data/persona_voice_mood_log.json"

# === Voice mood presets per persona ===
MOOD_VOICE_MAP = {
    "Mentor": {
        "happy": "mentor_happy_voice.mp3",
        "frustrated": "mentor_frustrated_voice.mp3",
        "calm": "mentor_calm_voice.mp3"
    },
    "Mo Cash": {
        "happy": "mo_cash_hype_voice.mp3",
        "frustrated": "mo_cash_angry_voice.mp3",
        "calm": "mo_cash_chill_voice.mp3"
    },
    "Strategist": {
        "happy": "strategist_confident_voice.mp3",
        "frustrated": "strategist_serious_voice.mp3",
        "calm": "strategist_calm_voice.mp3"
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

def load_current_persona():
    if os.path.exists(PERSONA_STATE_FILE):
        try:
            with open(PERSONA_STATE_FILE, "r") as f:
                state = json.load(f)
                return state.get("active_persona", "Mentor")
        except:
            return "Mentor"
    return "Mentor"

def get_voice_for_current_persona_and_mood():
    persona = load_current_persona()
    mood_state = load_current_mood_state()
    mood = mood_state.get(persona, "calm")
    voice_file = MOOD_VOICE_MAP.get(persona, {}).get(mood, "default_voice.mp3")
    log_event(f"[VOICE MOOD MANAGER]: Persona '{persona}' in mood '{mood}' will use '{voice_file}'")
    return voice_file

def log_event(message):
    logs = []
    if os.path.exists(MOOD_VOICE_LOG_FILE):
        try:
            with open(MOOD_VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(MOOD_VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

if __name__ == "__main__":
    get_voice_for_current_persona_and_mood()