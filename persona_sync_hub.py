from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: persona_sync_hub.py ===

import time
import json
import os

SYNC_FILE = "persona_state.json"
SYNC_INTERVAL = 10  # seconds


def load_persona_state():
    """Load current shared persona state."""
    if not os.path.exists(SYNC_FILE):
        return {}
    with open(SYNC_FILE, "r") as f:
        return json.load(f)


def save_persona_state(state):
    """Save updated persona state."""
    with open(SYNC_FILE, "w") as f:
        json.dump(state, f, indent=2)


def update_persona(bot_id, mood=None, task=None, memory=None):
    """Update a bot persona's shared state."""
    state = load_persona_state()
    if bot_id not in state:
        state[bot_id] = {}

    if mood:
        state[bot_id]["mood"] = mood
    if task:
        state[bot_id]["task"] = task
    if memory:
        state[bot_id]["memory"] = memory

    save_persona_state(state)
    print(f"[PersonaHub] Synced: {bot_id} → mood:{mood}, task:{task}")


def get_persona_state(bot_id):
    """Get latest state for a specific bot persona."""
    state = load_persona_state()
    return state.get(bot_id, {})


def monitor_persona(bot_id, mood_callback=None):
    """Live monitoring of a persona's state (pass callback for reactions)."""
    last_state = None

    while True:
        state = get_persona_state(bot_id)
        if state != last_state:
            print(f"[PersonaHub] 🔁 {bot_id} state updated: {state}")
            last_state = state
            if mood_callback:
                mood_callback(state)
        time.sleep(SYNC_INTERVAL)


# Example (test mode)
if __name__ == "__main__":
    update_persona("MoCash", mood="pumped", task="reviewing AAPL call spread")
    update_persona("Mentor", mood="focused", memory="Reviewing last week's trades")
    print(get_persona_state("Mentor"))

def log_event():ef drop_files_to_bridge():