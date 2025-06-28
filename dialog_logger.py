"""
Dialog Logger:
Records interactions between assistants for playback, learning, and continuity.
Supports training future AI memory and conversation threading.
"""

import json
import os
from datetime import datetime
from pathlib import Path

DIALOG_LOG_FILE = "data/dialog_log.json"
Path("data").mkdir(parents=True, exist_ok=True)

def log_dialog(initiator, receiver, initiator_msg, receiver_msg, emotion):
    """
    Stores a dialog event with metadata for future use.
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "initiator": initiator,
        "receiver": receiver,
        "initiator_msg": initiator_msg,
        "receiver_msg": receiver_msg,
        "emotion": emotion
    }

    log_data = []
    if os.path.exists(DIALOG_LOG_FILE):
        with open(DIALOG_LOG_FILE, "r") as f:
            try:
                log_data = json.load(f)
            except json.JSONDecodeError:
                log_data = []

    log_data.append(entry)
    with open(DIALOG_LOG_FILE, "w") as f:
        json.dump(log_data[-200:], f, indent=2)  # Keep most recent 200 logs

    print(f"[📚 Dialog Logged] {initiator} ➜ {receiver} | Emotion: {emotion}")

def get_recent_dialogs(limit=10):
    """
    Retrieves recent dialog events.
    """
    if not os.path.exists(DIALOG_LOG_FILE):
        return []

    with open(DIALOG_LOG_FILE, "r") as f:
        try:
            log_data = json.load(f)
        except json.JSONDecodeError:
            return []

    return log_data[-limit:]

# === Manual test
if __name__ == "__main__":
    log_dialog("MoCash", "Mentor", "That trade was lit!", "Indeed, but let's stay focused.", "win")
    print(get_recent_dialogs())