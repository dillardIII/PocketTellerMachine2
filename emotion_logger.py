from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Emotion Logger:
Captures inferred emotion states and stores them for short-term persona memory.
Used by dialog systems and trade analysis to drive mood shifts and memory chains.
"""

import os
import json
from datetime import datetime

EMOTION_LOG_PATH = "data/emotion_states.json"

def save_emotion_state(persona, emotion):
    """
    Save the emotional state of a persona to disk.
    """
    if not os.path.exists("data"):
        os.makedirs("data")

    log = []
    if os.path.exists(EMOTION_LOG_PATH):
        with open(EMOTION_LOG_PATH, "r") as f:
            try:
                log = json.load(f)
            except json.JSONDecodeError:
                log = []

    log.append({
        "persona": persona,
        "emotion": emotion,
        "timestamp": datetime.utcnow().isoformat()
    })

    with open(EMOTION_LOG_PATH, "w") as f:
        json.dump(log[-100:], f, indent=2)  # Keep only last 100 entries

    print(f"[🧠 Emotion Logged] {persona}: {emotion}")

def get_recent_emotion(persona):
    """
    Fetch the most recent emotional state for a persona.
    """
    if not os.path.exists(EMOTION_LOG_PATH):
        return None

    with open(EMOTION_LOG_PATH, "r") as f:
        try:
            log = json.load(f)
        except json.JSONDecodeError:
            return None

    filtered = [entry for entry in log if entry["persona"] == persona]:
    return filtered[-1] if filtered else None:
:
# === Test Mode
if __name__ == "__main__":
    save_emotion_state("Mentor", "win")
    print(get_recent_emotion("Mentor"))

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():