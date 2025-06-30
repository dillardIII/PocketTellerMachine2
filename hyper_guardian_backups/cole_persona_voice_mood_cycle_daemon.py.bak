# cole_persona_voice_mood_cycle_daemon.py

import os
import json
import random
import time
from datetime import datetime

# === Configurations ===
PERSONA_FILE = "data/persona_registry.json"
MOOD_OPTIONS = ["neutral", "happy", "confident", "sarcastic", "strict", "excited", "calm", "angry", "sad", "motivational"]
VOICE_OPTIONS = ["deep", "light", "robotic", "sweet", "raspy", "echo", "authoritative", "friendly", "whisper", "bold"]
LOG_FILE = "data/persona_voice_mood_cycle_log.json"
CHECK_INTERVAL = 1800  # Every 30 minutes

os.makedirs("data", exist_ok=True)

# === Load personas ===
def load_personas():
    if os.path.exists(PERSONA_FILE):
        with open(PERSONA_FILE, "r") as f:
            return json.load(f)
    return []

# === Cycle mood and voice ===
def cycle_mood_and_voice(persona):
    mood = random.choice(MOOD_OPTIONS)
    voice = random.choice(VOICE_OPTIONS)
    persona['mood'] = mood
    persona['voice'] = voice
    log_event(f"[CYCLE]: {persona['name']} → Mood: {mood} | Voice: {voice}")
    return persona

# === Update registry ===
def update_persona_registry(updated_personas):
    with open(PERSONA_FILE, "w") as f:
        json.dump(updated_personas, f, indent=2)

# === Logging ===
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

# === Daemon loop ===
def persona_voice_mood_cycle_loop():
    print("[PERSONA VOICE MOOD CYCLE]: Daemon running...")
    while True:
        try:
            personas = load_personas()
            if not personas:
                print("[CYCLE]: No personas found.")
            else:
                updated = [cycle_mood_and_voice(p) for p in personas]
                update_persona_registry(updated)
                print("[CYCLE]: All personas mood and voice cycled.")
        except Exception as e:
            log_event(f"[ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_voice_mood_cycle_loop()