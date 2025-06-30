from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_voice_selector.py

import os
import json
from datetime import datetime

# === Configurations ===
VOICE_SELECTION_FILE = "data/persona_voice_selection.json"
MOOD_STATE_FILE = "data/mood_state.json"
os.makedirs("data", exist_ok=True)

# === Voice Profiles ===
VOICE_PROFILES = {
    "happy": ["JoyfulMale", "JoyfulFemale"],
    "frustrated": ["GrittyMale", "FrustratedFemale"],
    "calm": ["CalmMale", "CalmFemale"],
    "neutral": ["DefaultMale", "DefaultFemale"]
}

# === Load Mood State ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Select Voice Based on Mood ===
def assign_voice_for_persona(persona, mood):
    voices = VOICE_PROFILES.get(mood, ["DefaultMale"])
    selected_voice = voices[0]  # You could randomize or rotate later
    return selected_voice

# === Generate Voice Assignment ===
def generate_voice_selection():
    mood_state = load_mood_state()
    voice_selection = {}

    for persona, mood in mood_state.items():
        selected_voice = assign_voice_for_persona(persona, mood)
        voice_selection[persona] = {
            "mood": mood,
            "voice": selected_voice,
            "timestamp": datetime.now().isoformat()
        }

    with open(VOICE_SELECTION_FILE, "w") as f:
        json.dump(voice_selection, f, indent=2)

    print("[VOICE SELECTOR]: Updated persona voices based on mood.")
    return voice_selection

# === Run once ===
if __name__ == "__main__":
    selection = generate_voice_selection()
    print(json.dumps(selection, indent=2))

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():