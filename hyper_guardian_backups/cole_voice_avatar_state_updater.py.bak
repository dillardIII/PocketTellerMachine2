# cole_voice_avatar_state_updater.py

import os
import json
from datetime import datetime

# === Configurations ===
AVATAR_STATE_FILE = "data/avatar_state.json"
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_TRAITS_FILE = "data/voice_traits.json"
AVATAR_LOG_FILE = "data/avatar_state_log.json"

# === Ensure folders ===
os.makedirs("data", exist_ok=True)

# === Load Avatar State ===
def load_avatar_state():
    if os.path.exists(AVATAR_STATE_FILE):
        try:
            with open(AVATAR_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Load Mood State ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Load Voice Traits ===
def load_voice_traits():
    if os.path.exists(VOICE_TRAITS_FILE):
        try:
            with open(VOICE_TRAITS_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Update Avatar State ===
def update_avatar_state():
    avatar_state = load_avatar_state()
    mood_state = load_mood_state()
    voice_traits = load_voice_traits()

    for persona in mood_state.keys():
        mood = mood_state.get(persona, "neutral")
        voice = voice_traits.get(persona, "default")

        avatar_state[persona] = {
            "mood": mood,
            "voice": voice,
            "updated_at": datetime.now().isoformat()
        }

        log_event(f"[AVATAR STATE]: {persona} updated → mood: {mood}, voice: {voice}")

    with open(AVATAR_STATE_FILE, "w") as f:
        json.dump(avatar_state, f, indent=2)

# === Log Event ===
def log_event(message):
    logs = []
    if os.path.exists(AVATAR_LOG_FILE):
        try:
            with open(AVATAR_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(AVATAR_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example Usage (testable) ===
if __name__ == "__main__":
    update_avatar_state()
    print("[AVATAR STATE UPDATER]: Avatar states updated based on mood and voice traits.")