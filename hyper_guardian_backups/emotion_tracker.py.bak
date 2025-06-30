"""
Emotion Tracker:
Records and monitors the mood of each assistant over time.
Useful for mood-based logic, escalating reactions, and tracking persona behavior patterns.
"""

import json
import os
from datetime import datetime

MOOD_LOG_PATH = "data/emotion_log.json"

def log_emotion(persona_name, mood):
    """
    Logs the current mood of a given persona with timestamp.
    """
    log_entry = {
        "persona": persona_name,
        "mood": mood,
        "timestamp": datetime.now().isoformat()
    }

    if not os.path.exists(MOOD_LOG_PATH):
        with open(MOOD_LOG_PATH, "w") as f:
            json.dump([log_entry], f, indent=2)
    else:
        with open(MOOD_LOG_PATH, "r") as f:
            mood_log = json.load(f)

        mood_log.append(log_entry)

        with open(MOOD_LOG_PATH, "w") as f:
            json.dump(mood_log, f, indent=2)

def get_latest_mood(persona_name):
    """
    Retrieves the last known mood of the given persona.
    """
    if not os.path.exists(MOOD_LOG_PATH):
        return "unknown"

    with open(MOOD_LOG_PATH, "r") as f:
        mood_log = json.load(f)

    for entry in reversed(mood_log):
        if entry["persona"] == persona_name:
            return entry["mood"]

    return "unknown"

# === Test Mode
if __name__ == "__main__":
    log_emotion("MoCash", "win")
    print("MoCash mood:", get_latest_mood("MoCash"))