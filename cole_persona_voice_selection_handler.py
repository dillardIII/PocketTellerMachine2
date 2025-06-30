from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_voice_selection_handler.py

import os
import json
from datetime import datetime

# === Configurations ===
PERSONA_STATE_FILE = "data/persona_current_state.json"
AVAILABLE_PERSONAS_FILE = "data/available_personas.json"
VOICE_SELECTION_LOG_FILE = "data/persona_voice_selection_log.json"

# === Ensure data folder exists ===
os.makedirs("data", exist_ok=True)

# === Load or create available personas ===
DEFAULT_PERSONAS = [
    {"name": "Mentor", "description": "Calm and wise advisor", "voice": "mentor_voice.mp3"},
    {"name": "Mo Cash", "description": "Aggressive risk taker", "voice": "mo_cash_voice.mp3"},
    {"name": "Strategist", "description": "Calculated and analytical", "voice": "strategist_voice.mp3"}
]

def load_available_personas():
    if os.path.exists(AVAILABLE_PERSONAS_FILE):
        try:
            with open(AVAILABLE_PERSONAS_FILE, "r") as f:
                return json.load(f)
        except:
            return DEFAULT_PERSONAS
    return DEFAULT_PERSONAS

def save_current_persona(persona_name):
    state = {"active_persona": persona_name, "timestamp": datetime.now().isoformat()}
    with open(PERSONA_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)
    log_event(f"[PERSONA SWITCH]: Changed to {persona_name}")

def log_event(message):
    logs = []
    if os.path.exists(VOICE_SELECTION_LOG_FILE):
        try:
            with open(VOICE_SELECTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_SELECTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Select Persona Handler ===
def select_persona_by_name(name):
    personas = load_available_personas()
    found = next((p for p in personas if p["name"].lower() == name.lower()), None):
    if found:
        save_current_persona(found["name"])
        print(f"[PERSONA HANDLER]: Persona switched to {found['name']}")
        return found
    else:
        print(f"[PERSONA HANDLER]: Persona '{name}' not found.")
        return None

if __name__ == "__main__":
    # Example Usage:
    select_persona_by_name("Mentor")
    select_persona_by_name("Mo Cash")