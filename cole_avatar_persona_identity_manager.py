from ghost_env import INFURA_KEY, VAULT_ADDRESS
# cole_avatar_persona_identity_manager.py

import os
import json
from datetime import datetime

# === Configurations ===
PERSONA_IDENTITY_FILE = "data/avatar_persona_identity.json"
IDENTITY_LOG_FILE = "data/avatar_identity_log.json"

# === Ensure folders ===
os.makedirs("data", exist_ok=True)

# === Default Persona Profiles ===
DEFAULT_PERSONAS = {
    "Mo Cash": {
        "role": "Hustler Trader",
        "voice": "raspy",
        "mood": "aggressive",
        "nickname": "Big Money",
        "style": "Streetwise Alpha",
        "personality_traits": ["bold", "confident", "street-savvy"]
    },
    "Mentor": {
        "role": "Wise Advisor",
        "voice": "calm",
        "mood": "supportive",
        "nickname": "Coach",
        "style": "Classic Mentor",
        "personality_traits": ["patient", "knowledgeable", "guiding"]
    },
    "Drill Instructor": {
        "role": "Military Enforcer",
        "voice": "intense",
        "mood": "strict",
        "nickname": "DI",
        "style": "Marine Corps Jargon",
        "personality_traits": ["tough", "direct", "disciplined"]
    }
}

# === Save persona identities ===
def save_persona_identities():
    with open(PERSONA_IDENTITY_FILE, "w") as f:
        json.dump(DEFAULT_PERSONAS, f, indent=2)
    log_event("[IDENTITY MANAGER]: Persona identities saved.")

# === Logging helper ===
def log_event(message):
    logs = []
    if os.path.exists(IDENTITY_LOG_FILE):
        try:
            with open(IDENTITY_LOG_FILE, "r") as f:
                logs = json.load(f)
        except:
            logs = []
    logs.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open(IDENTITY_LOG_FILE, "w") as f:
        json.dump(logs[-500:], f, indent=2)

# === Example usage ===
if __name__ == "__main__":
    save_persona_identities()
    print("[IDENTITY MANAGER]: Avatar persona identities initialized.")