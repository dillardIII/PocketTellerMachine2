from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: assistant_mood_engine.py ===
"""
Assistant Mood Engine:
Tracks and updates the emotional state of each persona.
Triggered by trade outcomes or user interactions.
Influences tone, voice, and visual feedback.
"""

import os
import json
from datetime import datetime

MOOD_FILE = "data/assistant_moods.json"
os.makedirs("data", exist_ok=True)

DEFAULT_MOODS = {
    "win": "energized",
    "loss": "frustrated",
    "neutral": "focused"
}

def load_moods():
    if not os.path.exists(MOOD_FILE):
        with open(MOOD_FILE, "w") as f:
            json.dump({}, f)
    with open(MOOD_FILE, "r") as f:
        return json.load(f)

def save_moods(data):
    with open(MOOD_FILE, "w") as f:
        json.dump(data, f, indent=2)

def update_mood(persona_name, result):
    """
    Sets mood based on trade result: 'win', 'loss', or 'neutral'.
    """
    mood_map = load_moods()
    new_mood = DEFAULT_MOODS.get(result, "neutral")
    mood_map[persona_name] = {
        "mood": new_mood,
        "last_result": result,
        "timestamp": datetime.utcnow().isoformat()
    }
    save_moods(mood_map)
    print(f"[🧠 Mood Engine] {persona_name} → Mood: {new_mood} ({result})")

def get_mood(persona_name):
    moods = load_moods()
    return moods.get(persona_name, {"mood": "neutral", "timestamp": None})

def list_all_moods():
    return load_moods()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():