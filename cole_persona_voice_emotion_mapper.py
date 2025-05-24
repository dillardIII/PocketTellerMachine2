# cole_persona_voice_emotion_mapper.py

import os
import json
from datetime import datetime

# === Configurations ===
PERSONALITY_FILE = "data/avatar_personalities.json"
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_EMOTION_FILE = "data/persona_voice_emotion_map.json"
VOICE_EMOTION_LOG = "data/voice_emotion_mapper_log.json"

# === Ensure data directory ===
os.makedirs("data", exist_ok=True)

# === Voice emotion presets ===
EMOTION_TONES = {
    "happy": ["Cheerful", "Excited", "Energetic"],
    "frustrated": ["Annoyed", "Serious", "Calm but sharp"],
    "calm": ["Relaxed", "Gentle", "Soothing"]
}

def load_personalities():
    if os.path.exists(PERSONALITY_FILE):
        try:
            with open(PERSONALITY_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def map_voice_emotions():
    personalities = load_personalities()
    mood_state = load_mood_state()
    mapping = {}

    for persona, details in personalities.items():
        current_mood = mood_state.get(persona, "calm")
        emotion_tone = EMOTION_TONES.get(current_mood, EMOTION_TONES["calm"])
        mapping[persona] = {
            "current_mood": current_mood,
            "voice_emotion": emotion_tone
        }
        log_event(f"[VOICE EMOTION MAPPER]: {persona} mapped to {emotion_tone} based on mood {current_mood}")

    with open(VOICE_EMOTION_FILE, "w") as f:
        json.dump(mapping, f, indent=2)

    return mapping

def log_event(message):
    logs = []
    if os.path.exists(VOICE_EMOTION_LOG):
        try:
            with open(VOICE_EMOTION_LOG, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_EMOTION_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)

if __name__ == "__main__":
    print("[VOICE EMOTION MAPPER]: Mapping voice emotions...")
    map_voice_emotions()