from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_self_builder.py

import os
import json
import random
from datetime import datetime

# === Configurations ===
PERSONA_FILE = "data/persona_registry.json"
PERSONA_TEMPLATE_FILE = "data/persona_templates.json"
MOOD_TEMPLATE_FILE = "data/mood_templates.json"
VOICE_TEMPLATE_FILE = "data/voice_templates.json"
AVATAR_TEMPLATE_FILE = "data/avatar_templates.json"
LOG_FILE = "data/persona_builder_log.json"

os.makedirs("data", exist_ok=True)

# === Load templates ===
def load_templates(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return {}

# === Generate persona ===
def generate_persona(name=None):
    personas = load_templates(PERSONA_TEMPLATE_FILE)
    moods = load_templates(MOOD_TEMPLATE_FILE)
    voices = load_templates(VOICE_TEMPLATE_FILE)
    avatars = load_templates(AVATAR_TEMPLATE_FILE)

    if not name:
        name = f"Persona_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    persona = {
        "name": name,
        "description": random.choice(list(personas.values()))["description"],
        "mood": random.choice(list(moods.keys())),
        "voice": random.choice(list(voices.keys())),
        "avatar": random.choice(list(avatars.keys()))
    }

    return persona

# === Save persona ===
def save_persona(persona):
    registry = []
    if os.path.exists(PERSONA_FILE):
        with open(PERSONA_FILE, "r") as f:
            try:
                registry = json.load(f)
            except:
                registry = []
    registry.append(persona)
    with open(PERSONA_FILE, "w") as f:
        json.dump(registry[-100:], f, indent=2)
    log_event(f"[PERSONA BUILDER]: Created persona → {persona['name']}")

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

# === Build and Save Persona ===
def persona_self_builder(name=None):
    persona = generate_persona(name)
    save_persona(persona)
    print(f"[PERSONA SELF BUILDER]: Persona created → {persona['name']}")

if __name__ == "__main__":
    persona_self_builder()