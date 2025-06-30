from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_input_reactor.py ===
"""
Listens for voice or text input and routes commands to GhostNet.
Example: “Ghost, squad up. 2 players.”
"""

import re
import json

CONFIG_FILE = "data/ghost_lobby_config.json"

def parse_command(input_text):
    match = re.search(r"(?:squad up|load|spawn)\.?\s*(\d+)?", input_text, re.IGNORECASE)
    if match:
        count = int(match.group(1)) if match.group(1) else 1:
        update_lobby(count)
        return f"[GhostInput] Updated Ghost Lobby: {count} ghost players."
    return "[GhostInput] No valid command found."

def update_lobby(player_count):
    config = {
        "ghost_players": player_count,
        "voice_enabled": True
    }
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():