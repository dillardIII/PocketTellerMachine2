# cole_phase13_persona_engine.py

import os
import json
from datetime import datetime
import random

# === Data Files ===
PERSONA_FILE = "data/cole_personas.json"
MOOD_FILE = "data/cole_persona_moods.json"
os.makedirs("data", exist_ok=True)

# === Persona Templates ===
TEMPLATES = [
    {"role": "Mentor", "mood": "Calm", "nickname": "Sensei", "voice": "mentor_voice_id"},
    {"role": "Aggressive Trader", "mood": "Hyped", "nickname": "Mo Cash", "voice": "hustler_voice_id"},
    {"role": "Optimist", "mood": "Cheerful", "nickname": "Sunny", "voice": "optimist_voice_id"},
    {"role": "Strategist", "mood": "Serious", "nickname": "Chessmaster", "voice": "strategist_voice_id"}
]

# === Initialize personas ===
def initialize_personas():
    if not os.path.exists(PERSONA_FILE):
        with open(PERSONA_FILE, "w") as f:
            json.dump(TEMPLATES, f, indent=2)
        print("[PERSONA ENGINE]: Initialized default personas.")

# === Add persona ===
def add_persona(role, mood, nickname, voice):
    with open(PERSONA_FILE, "r") as f:
        personas = json.load(f)
    new_persona = {
        "role": role,
        "mood": mood,
        "nickname": nickname,
        "voice": voice
    }
    personas.append(new_persona)
    with open(PERSONA_FILE, "w") as f:
        json.dump(personas, f, indent=2)
    log_mood_event(nickname, f"Created with mood {mood}")

# === Log mood history ===
def log_mood_event(persona, mood_message):
    logs = []
    if os.path.exists(MOOD_FILE):
        with open(MOOD_FILE, "r") as f:
            logs = json.load(f)
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "persona": persona,
        "mood_event": mood_message
    })
    with open(MOOD_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Random mood change trigger ===
def trigger_random_mood(persona):
    moods = ["Calm", "Hyped", "Frustrated", "Optimistic", "Sarcastic"]
    mood = random.choice(moods)
    log_mood_event(persona, f"Mood changed to {mood}")
    return mood

# === Run as a loop ===
def persona_engine_loop():
    print("[COLE PERSONA ENGINE]: Running...")
    initialize_personas()
    while True:
        # Future: listen for events and adjust personas dynamically
        pass

if __name__ == "__main__":
    persona_engine_loop()