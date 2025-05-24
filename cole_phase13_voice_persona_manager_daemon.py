# cole_phase13_voice_persona_manager_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
VOICE_PERSONAS_FILE = "data/cole_voice_personas.json"
VOICE_LOG_FILE = "data/cole_voice_persona_manager_log.json"
CHECK_INTERVAL = 3600  # Every hour

# === Ensure folders and files exist ===
os.makedirs("data", exist_ok=True)

# === Default Voice Personas ===
default_personas = [
    {"name": "The Mentor", "style": "calm, wise, informative"},
    {"name": "The Hustler", "style": "aggressive, street-smart, hype"},
    {"name": "The Comedian", "style": "funny, sarcastic, uplifting"},
    {"name": "The Drill Sergeant", "style": "strict, commanding, no-nonsense"},
    {"name": "The Chill Trader", "style": "relaxed, patient, zen"}
]

if not os.path.exists(VOICE_PERSONAS_FILE):
    with open(VOICE_PERSONAS_FILE, "w") as f:
        json.dump(default_personas, f, indent=2)

# === Logging Helper ===
def log_voice_event(message):
    logs = []
    if os.path.exists(VOICE_LOG_FILE):
        try:
            with open(VOICE_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(VOICE_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Persona Rotation ===
def rotate_persona():
    try:
        with open(VOICE_PERSONAS_FILE, "r") as f:
            personas = json.load(f)

        active_persona = personas.pop(0)
        personas.append(active_persona)

        with open(VOICE_PERSONAS_FILE, "w") as f:
            json.dump(personas, f, indent=2)

        log_voice_event(f"[ROTATION]: Activated persona → {active_persona['name']}")
        print(f"[VOICE PERSONA MANAGER DAEMON]: Rotated to → {active_persona['name']}")

    except Exception as e:
        log_voice_event(f"[ERROR]: {e}")
        print(f"[VOICE PERSONA MANAGER ERROR]: {e}")

# === Main Daemon Loop ===
def voice_persona_manager_loop():
    print("[VOICE PERSONA MANAGER DAEMON]: Running...")
    while True:
        rotate_persona()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    voice_persona_manager_loop()