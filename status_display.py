from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: status_display.py ===
# 📊 Status Display – Gathers live bot status for UI and JSON calls

import json
import os

STATUS_FILE = "bot_status.json"

def get_bot_status():
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r") as f:
            return json.load(f)
    return {
        "Reflex": False,
        "Ghostwriter": False,
        "Vault": False,
        "Integrator": False,
        "DropAgent": False,
        "Watchdog": False
    }

def update_bot_status(name, state):
    status = get_bot_status()
    status[name] = state
    with open(STATUS_FILE, "w") as f:
        json.dump(status, f, indent=4)

if __name__ == "__main__":
    print(get_bot_status())

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():