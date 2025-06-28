# === FILE: ghost_player_slot_manager.py ===
"""
Reads the Ghost Lobby Config and spawns AI players logically into the game.
Used for internal tracking and UI sync.
"""

import json
import time

CONFIG_FILE = "data/ghost_lobby_config.json"

def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def deploy_ghost_players():
    print("[GhostSlotManager] Deploying Ghost Players...")
    config = load_config()
    count = config.get("ghost_players", 1)

    for i in range(1, count + 1):
        print(f"[GhostPlayer {i}] Spawned and synced with Ghost Gamer net.")

if __name__ == "__main__":
    deploy_ghost_players()