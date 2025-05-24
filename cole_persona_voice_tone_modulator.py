# cole_persona_voice_tone_modulator.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_TONE_LOG_FILE = "data/persona_voice_tone_modulator_log.json"
CHECK_INTERVAL = 300  # Every 5 minutes

# === Voice tone presets based on mood ===
VOICE_TONE_MAP = {
    "happy": "cheerful",
    "frustrated": "firm",
    "calm": "soothing",
    "default": "neutral"
}

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def apply_voice_tone_adjustments():
    mood_state = load_current_mood_state()

    for persona, mood in mood_state.items():
        tone = VOICE_TONE_MAP.get(mood, VOICE_TONE_MAP["default"])
        log_event(f"[VOICE TONE MODULATOR]: {persona}'s voice tone adjusted to '{tone}' due to mood '{mood}'.")

def log_event(message):
    logs = []
    if os.path.exists(VOICE_TONE_LOG_FILE):
        try:
            with open(VOICE_TONE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_TONE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

if __name__ == "__main__":
    print("[VOICE TONE MODULATOR]: Starting...")
    apply_voice_tone_adjustments()