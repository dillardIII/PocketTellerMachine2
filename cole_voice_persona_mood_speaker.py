from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_voice_persona_mood_speaker.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
EMOTION_TONE_FILE = "data/voice_emotion_tone.json"
LOG_FILE = "data/voice_persona_speaker_log.json"

# === Ensure folders ===
os.makedirs("data", exist_ok=True)

# === Load Mood State ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Load Emotion Tones ===
def load_emotion_tones():
    if os.path.exists(EMOTION_TONE_FILE):
        try:
            with open(EMOTION_TONE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Log Event ===
def log_event(message):
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Generate Persona Voice Style ===
def generate_persona_voice_style(persona):
    mood_state = load_mood_state()
    emotion_tones = load_emotion_tones()

    mood = mood_state.get(persona, "neutral")
    tone = emotion_tones.get(mood, "default")

    voice_style = f"{persona} is currently {mood} and will speak in a {tone} tone."
    log_event(f"[VOICE SPEAKER]: {voice_style}")

    return voice_style

# Example Usage (testable)
if __name__ == "__main__":
    persona = "Mentor"
    style = generate_persona_voice_style(persona)
    print(style)