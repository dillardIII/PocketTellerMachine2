# 💀 GhostVaultLoader – resurrects old Ghost modules from the vault
# Scans vault dir for ghost_*.py files and restores them to main workspace

import os
import shutil
import time

VAULT_DIR = "vault"
WORKSPACE_DIR = "."

def restore_ghost_modules():
    print("[GhostVaultLoader] 👻 Scanning vault for ghost modules...")
    for root, dirs, files in os.walk(VAULT_DIR):
        for file in files:

# === MELD BREAK ===
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