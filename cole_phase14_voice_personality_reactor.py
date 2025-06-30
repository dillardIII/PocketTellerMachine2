from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase14_voice_personality_reactor.py

import os
import json
from datetime import datetime

# === Configurations ===
MOOD_STATE_FILE = "data/mood_state.json"
PERSONALITY_VOICE_MAP_FILE = "data/personality_voice_map.json"
REACT_LOG_FILE = "data/voice_personality_reactor_log.json"
os.makedirs("data", exist_ok=True)

# === Load Mood ===
def load_current_mood():
    if not os.path.exists(MOOD_STATE_FILE):
        return {}
    with open(MOOD_STATE_FILE, "r") as f:
        return json.load(f)

# === Load Personality Voice Map ===
def load_personality_voice_map():
    if not os.path.exists(PERSONALITY_VOICE_MAP_FILE):
        return {}
    with open(PERSONALITY_VOICE_MAP_FILE, "r") as f:
        return json.load(f)

# === Log Voice Reaction ===
def log_voice_reaction(message):
    logs = []
    if os.path.exists(REACT_LOG_FILE):
        try:
            with open(REACT_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(REACT_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Core: Select Voice Style Based on Mood & Personality ===
def select_voice_for_persona(persona):
    mood_state = load_current_mood()
    personality_voice_map = load_personality_voice_map()

    mood = mood_state.get(persona, "neutral")
    mood_personality_key = f"{persona}_{mood}"

    voice_config = personality_voice_map.get(mood_personality_key)

    if not voice_config:
        # Fallback to neutral voice for persona
        voice_config = personality_voice_map.get(f"{persona}_neutral", {"voice": "Default_AI_Voice", "style": "calm"})

    log_voice_reaction(f"Persona {persona} mood {mood} → Voice: {voice_config['voice']} Style: {voice_config['style']}")
    return voice_config

# === Example Usage Simulation ===
if __name__ == "__main__":
    personas = ["Mentor", "Mo_Cash", "Drill_Sergeant"]
    for persona in personas:
        voice_choice = select_voice_for_persona(persona)
        print(f"{persona} should now speak using voice: {voice_choice['voice']} and style: {voice_choice['style']}")

def log_event():ef drop_files_to_bridge():