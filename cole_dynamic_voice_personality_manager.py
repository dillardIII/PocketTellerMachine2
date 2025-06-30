from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_dynamic_voice_personality_manager.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_PROFILE_LOG_FILE = "data/dynamic_voice_personality_log.json"

VOICE_PERSONALITY_MAP = {
    "Mentor": {
        "happy": "mentor_voice_happy.mp3",
        "frustrated": "mentor_voice_strict.mp3",
        "calm": "mentor_voice_calm.mp3"
    },
    "Mo Cash": {
        "happy": "mo_cash_voice_hype.mp3",
        "frustrated": "mo_cash_voice_angry.mp3",
        "calm": "mo_cash_voice_chill.mp3"
    },
    "Strategist": {
        "happy": "strategist_voice_encouraging.mp3",
        "frustrated": "strategist_voice_commanding.mp3",
        "calm": "strategist_voice_analytical.mp3"
    }
}

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def get_voice_for_persona(persona):
    mood_state = load_current_mood_state()
    mood = mood_state.get(persona, "calm")
    voice_file = VOICE_PERSONALITY_MAP.get(persona, {}).get(mood, "default_voice.mp3")
    log_event(f"[VOICE PERSONALITY]: Persona '{persona}' mood '{mood}' will use voice '{voice_file}'")
    return voice_file

def log_event(message):
    logs = []
    if os.path.exists(VOICE_PROFILE_LOG_FILE):
        try:
            with open(VOICE_PROFILE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_PROFILE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

if __name__ == "__main__":
    # Example test
    get_voice_for_persona("Mentor")
    get_voice_for_persona("Mo Cash")
    get_voice_for_persona("Strategist")