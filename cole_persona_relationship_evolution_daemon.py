# cole_persona_relationship_evolution_daemon.py

import os
import json
import time
from datetime import datetime
import pytz

CENTRAL_TZ = pytz.timezone("US/Central")

def get_local_time():
    return datetime.now(CENTRAL_TZ)

# === Configurations ===
PERSONA_FILE = "data/avatar_personas.json"
RELATIONSHIP_LOG_FILE = "data/persona_relationship_evolution_log.json"
CHECK_INTERVAL = 1800  # Every 30 minutes

os.makedirs("data", exist_ok=True)

# === Sample evolution mapping ===
EVOLUTION_RULES = {
    "friendship": ["acquaintance", "friend", "trusted"],
    "rivalry": ["neutral", "competitive", "adversarial"]
}

def load_personas():
    if os.path.exists(PERSONA_FILE):
        try:
            with open(PERSONA_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def evolve_relationship(personas):
    for name, props in personas.items():
        relationship = props.get("relationship_status", "acquaintance")
        mood = props.get("mood", "neutral")

        if mood == "happy" and relationship in EVOLUTION_RULES["friendship"]:
            idx = EVOLUTION_RULES["friendship"].index(relationship)
            if idx < len(EVOLUTION_RULES["friendship"]) - 1:
                new_status = EVOLUTION_RULES["friendship"][idx + 1]
                props["relationship_status"] = new_status
                log_event(f"[RELATIONSHIP EVOLUTION]: {name} evolved to {new_status}")
        elif mood == "frustrated" and relationship in EVOLUTION_RULES["rivalry"]:
            idx = EVOLUTION_RULES["rivalry"].index(relationship)
            if idx < len(EVOLUTION_RULES["rivalry"]) - 1:
                new_status = EVOLUTION_RULES["rivalry"][idx + 1]
                props["relationship_status"] = new_status
                log_event(f"[RELATIONSHIP EVOLUTION]: {name} evolved to {new_status}")

    with open(PERSONA_FILE, "w") as f:
        json.dump(personas, f, indent=2)

def log_event(message):
    logs = []
    if os.path.exists(RELATIONSHIP_LOG_FILE):
        try:
            with open(RELATIONSHIP_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(RELATIONSHIP_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

def relationship_evolution_loop():
    print("[RELATIONSHIP EVOLUTION]: Running...")
    while True:
        try:
            personas = load_personas()
            if personas:
                evolve_relationship(personas)
        except Exception as e:
            log_event(f"[RELATIONSHIP EVOLUTION ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    relationship_evolution_loop()