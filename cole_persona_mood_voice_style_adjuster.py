from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_mood_voice_style_adjuster.py

import os
import json

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"

# === Voice Style Mapping per Mood ===
MOOD_VOICE_STYLE_MAP = {
    "happy": "upbeat",
    "frustrated": "stern",
    "calm": "soothing"
}

# === Load mood state ===
def load_current_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Determine voice style based on persona's mood ===
def get_voice_style_for_persona(persona):
    moods = load_current_mood_state()
    mood = moods.get(persona, "calm")
    voice_style = MOOD_VOICE_STYLE_MAP.get(mood, "neutral")
    return voice_style

# === Example usage ===
if __name__ == "__main__":
    personas = ["MoCash", "Mentor", "DrillInstructor"]
    for persona in personas:
        voice_style = get_voice_style_for_persona(persona)
        print(f"[VOICE STYLE]: {persona} → {voice_style} style based on mood.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():