from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_voice_tone_personality_mapper.py

import os
import json
from datetime import datetime

# === Configurations ===
VOICE_PERSONALITY_MAP_FILE = "data/voice_personality_map.json"
LOG_FILE = "data/voice_personality_mapper_log.json"

# === Default Mapping ===
VOICE_PERSONALITY_MAP = {
    "cheerful_upbeat": ["Optimist", "Mo Cash"],
    "firm_direct": ["Drill Instructor", "Mentor"],
    "neutral_balanced": ["Strategist", "Chill Trader"],
    "sad_soft": ["Empath", "Caregiver"]
}

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

def get_matching_personas(voice_tone):
    personas = VOICE_PERSONALITY_MAP.get(voice_tone, ["DefaultPersona"])
    log_event(f"[PERSONALITY MAPPER]: Voice tone '{voice_tone}' maps to personas: {personas}")
    return personas

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

if __name__ == "__main__":
    # Example test calls
    get_matching_personas("cheerful_upbeat")
    get_matching_personas("firm_direct")
    get_matching_personas("neutral_balanced")