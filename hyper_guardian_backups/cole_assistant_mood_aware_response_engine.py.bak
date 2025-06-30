# cole_assistant_mood_aware_response_engine.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
RESPONSE_LOG_FILE = "data/mood_aware_response_log.json"

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load current mood states ===
def load_mood_states():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Generate mood aware response ===
def generate_response(persona, message):
    moods = load_mood_states()
    mood = moods.get(persona, "neutral")

    if mood == "happy":
        response = f"{persona} (cheerfully): That's a great move! {message}"
    elif mood == "frustrated":
        response = f"{persona} (frustrated): Hmm, that didn't go as planned. {message}"
    elif mood == "calm":
        response = f"{persona} (calm): Let's keep the strategy steady. {message}"
    else:
        response = f"{persona}: {message}"

    log_event(f"[MOOD RESPONSE]: {response}")
    return response

# === Logging ===
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
    persona = "Cole Mentor"
    message = "Let's review today's performance."
    print(generate_response(persona, message))