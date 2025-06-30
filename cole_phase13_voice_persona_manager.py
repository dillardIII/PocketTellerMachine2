from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_phase13_voice_persona_manager.py

import os
import json
from datetime import datetime

# === Voice Persona Management ===
VOICE_PERSONA_FILE = "data/cole_voice_personas.json"
VOICE_PERSONA_LOG_FILE = "data/cole_voice_persona_events_log.json"
os.makedirs("data", exist_ok=True)

# === Default Voice Personas ===
DEFAULT_PERSONAS = [
    {"name": "Sensei", "voice_id": "mentor_voice", "tone": "Calm, wise, patient", "gender": "Neutral"},
    {"name": "Mo Cash", "voice_id": "mo_cash_voice", "tone": "Hustler, hype, aggressive", "gender": "Male"},
    {"name": "Sunny", "voice_id": "sunny_voice", "tone": "Bright, cheerful, optimistic", "gender": "Female"}
]

# === Initialize voice personas ===
def initialize_voice_personas():
    if not os.path.exists(VOICE_PERSONA_FILE):
        with open(VOICE_PERSONA_FILE, "w") as f:
            json.dump(DEFAULT_PERSONAS, f, indent=2)
        print("[VOICE PERSONA MANAGER]: Default voice personas initialized.")

# === Add or update voice persona ===
def add_voice_persona(name, voice_id, tone, gender):
    with open(VOICE_PERSONA_FILE, "r") as f:
        personas = json.load(f)
    p = next((x for x in personas if x['name'] == name), None):
    if p:
        p.update({"voice_id": voice_id, "tone": tone, "gender": gender})
        log_voice_persona_event(name, "Updated voice persona.")
    else:
        personas.append({"name": name, "voice_id": voice_id, "tone": tone, "gender": gender})
        log_voice_persona_event(name, "New voice persona created.")
    with open(VOICE_PERSONA_FILE, "w") as f:
        json.dump(personas, f, indent=2)

# === Log voice persona events ===
def log_voice_persona_event(name, message):
    logs = []
    if os.path.exists(VOICE_PERSONA_LOG_FILE):
        with open(VOICE_PERSONA_LOG_FILE, "r") as f:
            logs = json.load(f)
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "persona": name,
        "event": message
    })
    with open(VOICE_PERSONA_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Get all voice personas ===
def get_voice_personas():
    if os.path.exists(VOICE_PERSONA_FILE):
        with open(VOICE_PERSONA_FILE, "r") as f:
            return json.load(f)
    return []

if __name__ == "__main__":
    initialize_voice_personas()
    print("[VOICE PERSONA MANAGER]: Ready. Voice personas loaded.")

def log_event():ef drop_files_to_bridge():