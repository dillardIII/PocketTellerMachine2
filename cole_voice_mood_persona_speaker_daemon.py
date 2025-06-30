from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_voice_mood_persona_speaker_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
PERSONA_STATE_FILE = "data/persona_current_state.json"
SPEAKER_LOG_FILE = "data/persona_voice_speaker_log.json"
CHECK_INTERVAL = 900  # Every 15 minutes

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# === Helper Functions ===
def load_json(file_path, default):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except:
            return default
    return default

def log_event(message):
    logs = load_json(SPEAKER_LOG_FILE, [])
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(SPEAKER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Persona Voice Mood Speaker Logic ===
def speak_persona_mood():
    mood_state = load_json(MOOD_STATE_FILE, {})
    persona_state = load_json(PERSONA_STATE_FILE, {"active_persona": "Mentor"})
    active_persona = persona_state.get("active_persona", "Mentor")

    current_mood = mood_state.get(active_persona, "neutral")
    speech = generate_voice_line(active_persona, current_mood)

    log_event(f"[VOICE SPEAKER]: {active_persona} ({current_mood}) says: {speech}")
    print(f"[VOICE SPEAKER]: {active_persona} ({current_mood}) says: {speech}")

# === Generate Voice Line based on persona and mood ===
def generate_voice_line(persona, mood):
    if mood == "happy":
        return f"{persona} is feeling great and says, 'Let's crush the next trade together!'"
    elif mood == "frustrated":
        return f"{persona} sounds frustrated and says, 'We need to adjust our strategy and be smarter.'"
    elif mood == "calm":
        return f"{persona} remains calm and says, 'Stay patient, the market will come to us.'"
    else:
        return f"{persona} is in a neutral state and says, 'Reviewing current strategies.'"

# === Main Daemon Loop ===
def persona_voice_speaker_loop():
    print("[VOICE MOOD SPEAKER]: Running...")
    while True:
        try:
            speak_persona_mood()
        except Exception as e:
            log_event(f"[VOICE SPEAKER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

# === Run the Daemon ===
if __name__ == "__main__":
    persona_voice_speaker_loop()