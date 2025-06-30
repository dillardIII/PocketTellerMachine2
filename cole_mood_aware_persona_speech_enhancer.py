from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_mood_aware_persona_speech_enhancer.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
SPEECH_ENHANCER_LOG_FILE = "data/mood_aware_speech_enhancer_log.json"

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load current mood state ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Enhance message based on persona mood ===
def enhance_speech(persona, message):
    mood_state = load_mood_state()
    mood = mood_state.get(persona, "neutral").lower()

    if mood == "happy":
        enhanced_message = f"{message} Woohoo! Things are going great!"
    elif mood == "frustrated":
        enhanced_message = f"{message} Hmm... this isn't going as planned."
    elif mood == "calm":
        enhanced_message = f"{message} Let's keep our focus and stay steady."
    else:
        enhanced_message = message

    log_event(f"[MOOD ENHANCER]: {persona} mood '{mood}' applied to message.")
    return enhanced_message

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(SPEECH_ENHANCER_LOG_FILE):
        try:
            with open(SPEECH_ENHANCER_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(SPEECH_ENHANCER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example use (can be removed in daemonized usage) ===
if __name__ == "__main__":
    persona = "Cole"
    sample_message = "We completed the trade cycle."
    print(enhance_speech(persona, sample_message))