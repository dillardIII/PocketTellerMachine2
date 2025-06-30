# cole_persona_mood_assignment_engine.py

import os
import json
import random
from datetime import datetime

# === Configurations ===
PERSONA_FILE = "data/persona_registry.json"
MOOD_OPTIONS = ["neutral", "happy", "confident", "sarcastic", "strict", "excited", "calm", "angry", "sad", "motivational"]
LOG_FILE = "data/persona_mood_assignment_log.json"

os.makedirs("data", exist_ok=True)

# === Load personas ===
def load_personas():
    if os.path.exists(PERSONA_FILE):
        with open(PERSONA_FILE, "r") as f:
            return json.load(f)
    return []

# === Assign random mood ===
def assign_random_mood(persona):
    mood = random.choice(MOOD_OPTIONS)
    persona['mood'] = mood
    log_event(f"[MOOD ASSIGNMENT]: {persona['name']} assigned mood → {mood}")
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

# === Main Mood Assignment Function ===
def reassign_all_persona_moods():
    personas = load_personas()
    if not personas:
        print("[MOOD ASSIGNMENT]: No personas found.")
        return
    updated_personas = [assign_random_mood(p) for p in personas]
    update_persona_registry(updated_personas)
    print("[MOOD ASSIGNMENT]: All persona moods reassigned.")

if __name__ == "__main__":
    reassign_all_persona_moods()