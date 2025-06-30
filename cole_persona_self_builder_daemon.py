from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_self_builder_daemon.py

import os
import json
import time
from datetime import datetime

PERSONAS_FILE = "data/personas.json"
PERSONA_BUILDER_LOG_FILE = "data/persona_self_builder_log.json"
CHECK_INTERVAL = 3600  # 1 hour

os.makedirs("data", exist_ok=True)

default_personas = [
    {
        "name": "Mo Cash",
        "role": "Hustler",
        "voice": "mo_cash.mp3",
        "description": "Aggressive, confident, and always looking for the next trade."
    },
    {
        "name": "The Mentor",
        "role": "Teacher",
        "voice": "mentor.mp3",
        "description": "Patient and calm, offering wise trading insights and feedback."
    },
    {
        "name": "Drill Instructor",
        "role": "Discipline Enforcer",
        "voice": "drill_instructor.mp3",
        "description": "Strict, loud, and no-nonsense, keeping you focused and accountable."
    }
]

def log_persona_event(message):
    logs = []
    if os.path.exists(PERSONA_BUILDER_LOG_FILE):
        try:
            with open(PERSONA_BUILDER_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(PERSONA_BUILDER_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def ensure_personas_exist():
    if not os.path.exists(PERSONAS_FILE):
        with open(PERSONAS_FILE, "w") as f:
            json.dump(default_personas, f, indent=2)
        log_persona_event("[PERSONA BUILDER]: Default personas created.")
        print("[PERSONA BUILDER]: Default personas created.")
    else:
        print("[PERSONA BUILDER]: Personas already exist.")

def persona_self_builder_loop():
    print("[PERSONA SELF BUILDER DAEMON]: Running...")
    while True:
        try:
            ensure_personas_exist()
        except Exception as e:
            log_persona_event(f"[ERROR]: {e}")
            print(f"[PERSONA BUILDER ERROR]: {e}")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_self_builder_loop()

def log_event():ef drop_files_to_bridge():