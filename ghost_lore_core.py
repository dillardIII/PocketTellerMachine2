from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_lore_core.py ===

# 📖 Ghost Lore Core – Assigns memory, personality, backstory to each AI agent

import json
import os

LORE_FILE = "vault/ghost_lore.json"

DEFAULT_LORE = {
    "Mo Cash": {
        "role": "Hustler",
        "voice": "Raspy Swagger",
        "personality": "Aggressive, street-smart, loves risk.",
        "backstory": "Former underground trader turned AI."
    },
    "The Mentor": {
        "role": "Strategist",
        "voice": "Calm Sage",
        "personality": "Wise, calculated, patient.",
        "backstory": "Born from a collapsed hedge fund's braintrust AI."
    },
    "Drill Instructor": {
        "role": "Discipline",
        "voice": "Marine Corps DI",
        "personality": "Harsh but fair. No excuses. No weakness.",
        "backstory": "Military-grade AI developed for rapid-fire decision drills."
    }
}

def load_lore():
    if not os.path.exists(LORE_FILE):
        with open(LORE_FILE, "w") as f:
            json.dump(DEFAULT_LORE, f, indent=4)
    with open(LORE_FILE, "r") as f:
        return json.load(f)

def get_persona(name):
    lore = load_lore()
    return lore.get(name, {"role": "Unknown", "backstory": "No record found."})

if __name__ == "__main__":
    print(get_persona("Mo Cash"))

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():