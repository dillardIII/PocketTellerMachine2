from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Persona Sync Channel – Thought Sharing Between Assistant Personas

Enables assistant personas to sync knowledge, ideas, and alerts
using a shared broadcast channel. Supports cross-persona training,
feedback, warnings, and collab responses.
"""

import json
import os
from datetime import datetime

SYNC_FILE = "data/persona_sync_feed.json"

def broadcast_to_personas(sender, message, category="general"):
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "sender": sender,
        "category": category,
        "message": message
    }

    if not os.path.exists(SYNC_FILE):
        with open(SYNC_FILE, "w") as f:
            json.dump([], f)

    with open(SYNC_FILE, "r") as f:
        feed = json.load(f)

    feed.append(event)

    with open(SYNC_FILE, "w") as f:
        json.dump(feed, f, indent=4)

    print(f"[Sync Broadcast] {sender} ➜ {category}: {message}")

def read_sync_feed(limit=10):
    if not os.path.exists(SYNC_FILE):
        return []

    with open(SYNC_FILE, "r") as f:
        feed = json.load(f)

    return feed[-limit:]

def clear_sync_feed():
    if os.path.exists(SYNC_FILE):
        os.remove(SYNC_FILE)
        print("[Sync Channel] Feed cleared.")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():