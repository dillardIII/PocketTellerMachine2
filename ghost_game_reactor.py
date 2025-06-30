from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_game_reactor.py ===
"""
Listens for game updates and triggers Ghost Gamer reactions,
such as voice lines, strategy hints, or mood shifts.
"""

import json
import os
import time
from datetime import datetime
from voice_engine import speak_from_ghost_profile  # Placeholder for ElevenLabs trigger

GAME_STATUS_FILE = "data/game_status.json"
PROFILE_FILE = "data/ghost_profile.json"
CHECK_INTERVAL = 4  # seconds

def load_game():
    if not os.path.exists(GAME_STATUS_FILE):
        return "None"
    with open(GAME_STATUS_FILE, "r") as f:
        return json.load(f).get("current_game", "None")

def load_profile():
    if not os.path.exists(PROFILE_FILE):
        return {}
    with open(PROFILE_FILE, "r") as f:
        return json.load(f)

def trigger_reaction(game, profile):
    quotes = profile.get("game_quotes", {}).get(game.lower(), [])
    if quotes:
        message = quotes[0]  # In future: random.choice or dynamic selection
        speak_from_ghost_profile(message, profile)
        print(f"[GhostReactor] Reacted to {game}: {message}")
    else:
        print(f"[GhostReactor] No quote found for {game}")

def start_game_reactor():
    print("[GhostReactor] Starting game reaction loop...")
    last_game = None

    while True:
        game = load_game()
        if game != last_game and game != "None":
            profile = load_profile()
            trigger_reaction(game, profile)
            last_game = game
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    start_game_reactor()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():