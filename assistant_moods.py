from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: assistant_moods.py ===
# 🎭 Assistant Moods – Stores and updates current AI emotional states

import json
import os

MOOD_FILE = "assistant_moods.json"

DEFAULT_MOODS = {
    "Mo Cash": "Hyped",
    "Mentor": "Calm",
    "Strategist": "Focused",
    "Drill Instructor": "Intense",
    "GhostBot": "Neutral"
}

def get_moods():
    if not os.path.exists(MOOD_FILE):
        with open(MOOD_FILE, "w") as f:
            json.dump(DEFAULT_MOODS, f, indent=4)
    with open(MOOD_FILE, "r") as f:
        return json.load(f)

def set_mood(name, mood):
    moods = get_moods()
    moods[name] = mood
    with open(MOOD_FILE, "w") as f:
        json.dump(moods, f, indent=4)

if __name__ == "__main__":
    print(get_moods())

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():