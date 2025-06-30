from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_voice_dynamic_responder.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_RESPONSE_FILE = "data/avatar_voice_response.json"
RESPONSE_LOG_FILE = "data/avatar_voice_response_log.json"

# === Ensure folders ===
os.makedirs("data", exist_ok=True)

# === Voice Response Rules ===
VOICE_RESPONSE_MAP = {
    "happy": "respond_cheerfully",
    "frustrated": "respond_sternly",
    "calm": "respond_neutrally",
    "sad": "respond_gently"
}

# === Load current mood state ===
def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Generate voice response mapping based on mood ===
def generate_voice_responses():
    mood_state = load_current_mood_state()
    voice_responses = {}

    for persona, mood in mood_state.items():
        voice_response = VOICE_RESPONSE_MAP.get(mood, "respond_neutrally")
        voice_responses[persona] = {
            "current_mood": mood,
            "voice_response_style": voice_response,
            "timestamp": datetime.now().isoformat()
        }
        log_event(f"[VOICE RESPONDER]: {persona} → mood: {mood} → response style: {voice_response}")

    with open(VOICE_RESPONSE_FILE, "w") as f:
        json.dump(voice_responses, f, indent=2)

# === Logging helper ===
def log_event(message):
    logs = []
    if os.path.exists(RESPONSE_LOG_FILE):
        try:
            with open(RESPONSE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(RESPONSE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example usage ===
if __name__ == "__main__":
    generate_voice_responses()
    print("[VOICE RESPONDER]: Voice responses updated based on current mood.")