# cole_persona_voice_assignment_engine.py

import os
import json
import random
from datetime import datetime

# === Configurations ===
PERSONA_FILE = "data/persona_registry.json"
VOICE_TEMPLATE_FILE = "data/voice_templates.json"
LOG_FILE = "data/persona_voice_assignment_log.json"

os.makedirs("data", exist_ok=True)

# === Load voices ===
def load_voice_templates():
    if os.path.exists(VOICE_TEMPLATE_FILE):
        with open(VOICE_TEMPLATE_FILE, "r") as f:
            return json.load(f)
    return {}

# === Load personas ===
def load_personas():
    if os.path.exists(PERSONA_FILE):
        with open(PERSONA_FILE, "r") as f:
            return json.load(f)
    return []

# === Assign new voice ===
def assign_new_voice(persona):
    voices = load_voice_templates()
    if voices:
        persona['voice'] = random.choice(list(voices.keys()))
        log_event(f"[VOICE ASSIGNMENT]: {persona['name']} assigned new voice → {persona['voice']}")
    return persona

# === Update persona registry ===
def update_persona_registry(updated_personas):
    with open(PERSONA_FILE, "w") as f:
        json.dump(updated_personas, f, indent=2)

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except:
                logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Voice Reassignment Function ===
def reassign_all_persona_voices():
    personas = load_personas()
    if not personas:
        print("[VOICE ASSIGNMENT]: No personas found.")
        return
    updated_personas = [assign_new_voice(p) for p in personas]
    update_persona_registry(updated_personas)
    print("[VOICE ASSIGNMENT]: All persona voices reassigned.")

if __name__ == "__main__":
    reassign_all_persona_voices()