from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_dynamic_emotion_trigger_responder.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
EMOTION_TRIGGER_LOG_FILE = "data/emotion_trigger_responder_log.json"

EMOTION_RESPONSE_MAP = {
    "happy": "Playing celebratory sound and using upbeat voice.",
    "frustrated": "Using firm tone. Suggesting analysis correction.",
    "calm": "Using balanced voice. Maintaining normal flow."
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

def trigger_emotional_response(persona):
    mood_state = load_current_mood_state()
    mood = mood_state.get(persona, "calm")
    response_action = EMOTION_RESPONSE_MAP.get(mood, "Using default neutral tone.")
    log_event(f"[EMOTION TRIGGER]: Persona '{persona}' mood '{mood}' triggered → {response_action}")
    return response_action

def log_event(message):
    logs = []
    if os.path.exists(EMOTION_TRIGGER_LOG_FILE):
        try:
            with open(EMOTION_TRIGGER_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(EMOTION_TRIGGER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

if __name__ == "__main__":
    # Example test calls
    trigger_emotional_response("Mentor")
    trigger_emotional_response("Mo Cash")
    trigger_emotional_response("Strategist")