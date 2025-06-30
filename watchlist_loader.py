from ghost_env import INFURA_KEY, VAULT_ADDRESS
import json
import os

WATCHLIST_FILE = "data/watchlist.json"

def load_watchlist():
    if os.path.exists(WATCHLIST_FILE):
        with open(WATCHLIST_FILE, "r") as f:
            return json.load(f)
    return ["AAPL"]  # fallback default

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():