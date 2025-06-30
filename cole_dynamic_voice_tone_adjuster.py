from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_dynamic_voice_tone_adjuster.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_TONE_LOG_FILE = "data/voice_tone_adjuster_log.json"

VOICE_TONE_MAP = {
    "happy": "cheerful_upbeat",
    "frustrated": "firm_direct",
    "calm": "neutral_balanced"
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

def adjust_voice_tone(persona):
    mood_state = load_current_mood_state()
    mood = mood_state.get(persona, "calm")
    voice_tone = VOICE_TONE_MAP.get(mood, "neutral_balanced")
    log_event(f"[VOICE TONE ADJUSTER]: Adjusted {persona} voice tone to '{voice_tone}' based on mood '{mood}'")
    return voice_tone

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
    # Example test calls
    adjust_voice_tone("Mentor")
    adjust_voice_tone("Mo Cash")
    adjust_voice_tone("Strategist")