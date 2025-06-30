from ghost_env import INFURA_KEY, VAULT_ADDRESS
# core_memory_logger.py – PTM memory log engine

import os
import json
from datetime import datetime

LOG_DIR = "ptm_memory_logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_game_action(game_name, action, source="Unknown"):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "game": game_name,
        "action": action,
        "source": source
    }

    filename = os.path.join(LOG_DIR, f"{game_name}_log.json")
    with open(filename, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():