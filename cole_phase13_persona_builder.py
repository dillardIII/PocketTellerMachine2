# cole_phase13_persona_builder.py

import os
import json
from datetime import datetime

# === Persona Data File ===
PERSONA_FILE = "data/cole_personas.json"
PERSONA_LOG_FILE = "data/cole_persona_events_log.json"
os.makedirs("data", exist_ok=True)

# === Default Personas ===
DEFAULT_PERSONAS = [
    {"persona": "Coach Max", "role": "Mentor", "voice_profile": "Sensei", "mood": "supportive", "description": "Guides user with patience and wisdom."},
    {"persona": "Mo Cash", "role": "Hustler", "voice_profile": "Mo Cash", "mood": "hype", "description": "Aggressive motivator who loves the hustle."},
    {"persona": "Sunny Side", "role": "Optimist", "voice_profile": "Sunny", "mood": "cheerful", "description": "Always encouraging and sees the best in every trade."}
]

# === Initialize personas ===
def initialize_personas():
    if not os.path.exists(PERSONA_FILE):
        with open(PERSONA_FILE, "w") as f:
            json.dump(DEFAULT_PERSONAS, f, indent=2)
        print("[PERSONA BUILDER]: Default personas initialized.")

# === Add or update persona ===
def add_persona(persona, role, voice_profile, mood, description):
    with open(PERSONA_FILE, "r") as f:
        personas = json.load(f)
    p = next((x for x in personas if x['persona'] == persona), None)
    if p:
        p.update({"role": role, "voice_profile": voice_profile, "mood": mood, "description": description})
        log_persona_event(persona, "Updated persona.")
    else:
        personas.append({"persona": persona, "role": role, "voice_profile": voice_profile, "mood": mood, "description": description})
        log_persona_event(persona, "New persona created.")
    with open(PERSONA_FILE, "w") as f:
        json.dump(personas, f, indent=2)

# === Log persona events ===
def log_persona_event(persona, message):
    logs = []
    if os.path.exists(PERSONA_LOG_FILE):
        with open(PERSONA_LOG_FILE, "r") as f:
            logs = json.load(f)
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "persona": persona,
        "event": message
    })
    with open(PERSONA_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Get all personas ===
def get_personas():
    if os.path.exists(PERSONA_FILE):
        with open(PERSONA_FILE, "r") as f:
            return json.load(f)
    return []

if __name__ == "__main__":
    initialize_personas()
    print("[PERSONA BUILDER]: Ready. Personas loaded.")