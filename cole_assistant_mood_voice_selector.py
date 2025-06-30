from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_assistant_mood_voice_selector.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
VOICE_MAP_FILE = "data/voice_map.json"
VOICE_LOG_FILE = "data/mood_voice_selector_log.json"

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load mood state ===
def load_mood_states():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Load voice mappings ===
def load_voice_map():
    if os.path.exists(VOICE_MAP_FILE):
        try:
            with open(VOICE_MAP_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Select voice based on mood ===
def select_voice_for_persona(persona):
    moods = load_mood_states()
    voices = load_voice_map()
    mood = moods.get(persona, "neutral")

    persona_voices = voices.get(persona, {})
    selected_voice = persona_voices.get(mood, "default_voice")

    log_event(f"[MOOD VOICE SELECTOR]: {persona} mood {mood} → voice {selected_voice}")
    return selected_voice

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(VOICE_LOG_FILE):
        try:
            with open(VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example usage ===
if __name__ == "__main__":
    persona = "Cole Mentor"
    voice = select_voice_for_persona(persona)
    print(f"Selected voice for {persona}: {voice}")