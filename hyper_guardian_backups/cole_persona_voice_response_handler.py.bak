# cole_persona_voice_response_handler.py

import os
import json
from datetime import datetime
from cole_persona_voice_player import play_voice_line

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
MOOD_LOG_FILE = "data/mood_engine_log.json"
os.makedirs("data", exist_ok=True)

# === Load current mood state ===
def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Generate voice response based on mood ===
def generate_voice_response(persona, context="default"):
    mood_state = load_current_mood_state()
    mood = mood_state.get(persona, "neutral")
    
    if mood == "happy":
        message = f"{persona} says with excitement: 'Let's go! I'm feeling great!'"
    elif mood == "frustrated":
        message = f"{persona} grumbles: 'Ugh... we need to do better next time.'"
    else:
        message = f"{persona} calmly says: 'Processing... stay patient.'"
    
    play_voice_line(persona, message)
    log_event(f"[VOICE RESPONSE]: Generated response for {persona} in mood {mood}")

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(MOOD_LOG_FILE):
        try:
            with open(MOOD_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(MOOD_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example Call ===
if __name__ == "__main__":
    generate_voice_response("DefaultPersona")