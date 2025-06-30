# cole_voice_mood_response_generator.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_RESPONSES_FILE = "data/voice_responses.json"
VOICE_RESPONSE_LOG_FILE = "data/voice_response_log.json"

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load mood state ===
def load_mood_states():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Load pre-defined voice responses ===
def load_voice_responses():
    if os.path.exists(VOICE_RESPONSES_FILE):
        try:
            with open(VOICE_RESPONSES_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Generate response based on mood ===
def generate_response(persona, message):
    moods = load_mood_states()
    responses = load_voice_responses()

    mood = moods.get(persona, "neutral")
    persona_responses = responses.get(persona, {})
    mood_responses = persona_responses.get(mood, [])

    if mood_responses:
        selected_response = random.choice(mood_responses)
    else:
        selected_response = f"{persona} says (neutral): {message}"

    log_event(f"[VOICE RESPONSE GENERATOR]: {persona} ({mood}) → {selected_response}")
    return selected_response

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(VOICE_RESPONSE_LOG_FILE):
        try:
            with open(VOICE_RESPONSE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_RESPONSE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example usage ===
if __name__ == "__main__":
    import random
    persona = "Cole Mentor"
    message = "Let's review the last trade."
    response = generate_response(persona, message)
    print(response)