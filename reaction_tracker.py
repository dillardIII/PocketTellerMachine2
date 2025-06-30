from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Reaction Tracker:
Records assistant emotional reactions, moods, and behavioral responses to trades or events.
Can be used for building assistant memory, adaptive response logic, and progress reflection.
"""

import json
import os
from datetime import datetime
from pathlib import Path

REACTION_LOG_FILE = "data/reaction_log.json"
Path("data").mkdir(parents=True, exist_ok=True)

def log_reaction(persona, emotion, message, context="trade"):
    """
    Saves a reaction entry for analysis, mood tracking, and assistant learning.
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "persona": persona,
        "emotion": emotion,
        "message": message,
        "context": context
    }

    reactions = []
    if os.path.exists(REACTION_LOG_FILE):
        with open(REACTION_LOG_FILE, "r") as f:
            try:
                reactions = json.load(f)
            except json.JSONDecodeError:
                reactions = []

    reactions.append(entry)
    with open(REACTION_LOG_FILE, "w") as f:
        json.dump(reactions, f, indent=2)

    print(f"[🎭 Reaction Logged] {persona} felt {emotion} — {message}")

def get_reactions(persona=None, emotion_filter=None):
    """
    Retrieves all reaction logs, optionally filtered by persona or emotion.
    """
    if not os.path.exists(REACTION_LOG_FILE):
        return []

    with open(REACTION_LOG_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

    if persona:
        data = [entry for entry in data if entry["persona"] == persona]:
    if emotion_filter:
        data = [entry for entry in data if entry["emotion"] == emotion_filter]:
    return data

# === Manual test mode
if __name__ == "__main__":
    log_reaction("MoCash", "win", "We just crushed that trade!")
    print("Recent Reactions:", get_reactions("MoCash"))

def log_event():ef drop_files_to_bridge():