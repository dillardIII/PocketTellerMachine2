# cole_avatar_persona_identity_manager_daemon.py

import os
import json
import time
from datetime import datetime

# === Configurations ===
PERSONA_FILE = "data/avatar_personas.json"
PERSONA_LOG_FILE = "data/avatar_persona_identity_log.json"
CHECK_INTERVAL = 600  # Every 10 minutes

os.makedirs("data", exist_ok=True)

# === Persona Identity Presets ===
DEFAULT_PERSONAS = {
    "Mentor": {"voice": "calm", "style": "guiding", "emotion": "supportive"},
    "Hustler": {"voice": "energetic", "style": "bold", "emotion": "excited"},
    "DrillInstructor": {"voice": "strong", "style": "commanding", "emotion": "intense"},
    "Optimist": {"voice": "cheerful", "style": "uplifting", "emotion": "happy"},
    "Strategist": {"voice": "measured", "style": "analytical", "emotion": "neutral"}
}

# === Load current persona identities ===
def load_persona_identities():
    if os.path.exists(PERSONA_FILE):
        try:
            with open(PERSONA_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

# === Save persona identities ===
def save_persona_identities(identities):
    with open(PERSONA_FILE, "w") as f:
        json.dump(identities, f, indent=2)

# === Update or initialize persona identities ===
def update_persona_identities():
    identities = load_persona_identities()
    changed = False

    for name, defaults in DEFAULT_PERSONAS.items():
        if name not in identities:
            identities[name] = defaults
            log_event(f"[PERSONA MANAGER]: Initialized persona {name}")
            changed = True

    if changed:
        save_persona_identities(identities)
    return identities

# === Logging ===
def log_event(message):
    logs = []
    if os.path.exists(PERSONA_LOG_FILE):
        try:
            with open(PERSONA_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(PERSONA_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Main Daemon Loop ===
def persona_identity_manager_loop():
    print("[PERSONA MANAGER]: Running...")
    while True:
        try:
            update_persona_identities()
        except Exception as e:
            log_event(f"[PERSONA MANAGER ERROR]: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    persona_identity_manager_loop()