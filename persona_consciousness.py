from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Persona Consciousness Engine
Assigns self-awareness, emotion states, and independent thinking models to each assistant.
Supports mood fluctuations, memory-based reactions, and personality-driven logic.
"""

import json
import os
from datetime import datetime
import random

PERSONA_FILE = "memory/persona_states.json"
MOODS = ["calm", "focused", "irritated", "joyful", "concerned", "excited", "strategic"]

def load_personas():
    if not os.path.exists(PERSONA_FILE):
        return {}
    with open(PERSONA_FILE, "r") as f:
        return json.load(f)

def save_personas(data):
    with open(PERSONA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def update_mood(persona: str):
    data = load_personas()
    if persona not in data:
        data[persona] = {}

    current_mood = random.choice(MOODS)
    data[persona]["mood"] = current_mood
    data[persona]["last_updated"] = datetime.utcnow().isoformat()

    save_personas(data)
    print(f"[Consciousness] {persona} mood updated to: {current_mood}")

def get_mood(persona: str):
    data = load_personas()
    return data.get(persona, {}).get("mood", "unknown")

def list_persona_states():
    data = load_personas()
    return {p: d.get("mood", "unknown") for p, d in data.items()}

# Demo / Trigger
if __name__ == "__main__":
    for name in ["Mentor", "Mo Cash", "Shadow", "Strategist"]:
        update_mood(name)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():