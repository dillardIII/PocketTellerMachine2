from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_persona_interaction_simulator.py

import os
import json
import time
from datetime import datetime
import random

# === Configurations ===
INTERACTION_LOG_FILE = "data/persona_interaction_log.json"
MOOD_STATE_FILE = "data/mood_state.json"
CHECK_INTERVAL = 900  # Every 15 minutes

# === Persona Definitions ===
PERSONAS = ["Mentor", "Mo Cash", "Drill Instructor", "Strategist", "Chill Trader", "OG"]

# === Predefined Banter Templates ===
BANTER_TEMPLATES = [
    "{persona1} says to {persona2}: 'Your last trade call was weak, I could've done better blindfolded!'",
    "{persona1} challenges {persona2}: 'Let's see who nails the next options chain, rookie.'",
    "{persona1} laughs at {persona2}: 'You still using those outdated indicators?'",
    "{persona1} calms {persona2}: 'Chill out, sometimes losses happen, even to me.'",
    "{persona1} nods to {persona2}: 'I like that last trade setup, bold but calculated.'"
]

# === Load mood state ===
def load_mood_state():
    if os.path.exists(MOOD_STATE_FILE):
        try:
            with open(MOOD_STATE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Simulate interaction ===
def simulate_persona_banter():
    mood_state = load_mood_state()
    logs = []

    for _ in range(5):
        persona1, persona2 = random.sample(PERSONAS, 2)
        mood1 = mood_state.get(persona1, "neutral")
        template = random.choice(BANTER_TEMPLATES)
        interaction = template.format(persona1=persona1, persona2=persona2)
        interaction += f" (Mood: {persona1} is {mood1})"
        logs.append({"timestamp": datetime.now().isoformat(), "message": interaction})

    return logs

# === Logging ===
def log_event(entries):
    logs = []
    if os.path.exists(INTERACTION_LOG_FILE):
        try:
            with open(INTERACTION_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.extend(entries)
    with open(INTERACTION_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def persona_interaction_loop():
    print("[PERSONA INTERACTION SIMULATOR]: Starting simulated interactions...")
    while True:
        try:
            entries = simulate_persona_banter()
            log_event(entries)
        except Exception as e:
            log_event([{"timestamp": datetime.now().isoformat(), "message": f"[ERROR]: {e}"}])
        time.sleep(CHECK_INTERVAL)

# === Run ===
if __name__ == "__main__":
    persona_interaction_loop()