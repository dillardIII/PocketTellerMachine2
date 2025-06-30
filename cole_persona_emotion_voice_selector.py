from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_emotion_voice_selector.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_SELECTION_LOG = "data/persona_voice_selection_log.json"

# === Voice Profiles ===
VOICE_PROFILES = {
    "happy": ["cheerful_male", "cheerful_female"],
    "frustrated": ["strict_male", "strict_female"],
    "calm": ["calm_male", "calm_female"],
    "neutral": ["neutral_male", "neutral_female"]
}

# === Ensure data directory exists ===
os.makedirs("data", exist_ok=True)

# === Load Mood State ===
def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Select Voice Based on Mood ===
def select_voice_for_persona(persona):
    mood_state = load_current_mood_state()
    current_mood = mood_state.get(persona, "neutral")
    available_voices = VOICE_PROFILES.get(current_mood, VOICE_PROFILES["neutral"])

    selected_voice = available_voices[0]  # Future upgrade can make this randomized or adaptive
    log_voice_selection(persona, current_mood, selected_voice)
    return selected_voice

# === Logging Voice Selection ===
def log_voice_selection(persona, mood, voice):
    logs = []
    if os.path.exists(VOICE_SELECTION_LOG):
        try:
            with open(VOICE_SELECTION_LOG, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "persona": persona, "mood": mood, "voice": voice})
    with open(VOICE_SELECTION_LOG, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example Usage ===
if __name__ == "__main__":
    personas = ["Mentor", "Mo Cash", "Drill Instructor"]

    for persona in personas:
        voice = select_voice_for_persona(persona)
        print(f"[{persona}]: Selected voice profile → {voice}")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():