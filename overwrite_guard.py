from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: overwrite_guard.py ===

import os
import datetime
from file_lock_checker import is_file_locked

LOG_FILE = "vault/logs/file_overwrite.log"

def log_attempt(file_name, bot_name):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, 'a') as log:
        timestamp = datetime.datetime.now().isoformat()
        log.write(f"[{timestamp}] ❌ {bot_name} attempted to overwrite locked file: {file_name}\n")
        print(f"[GUARD] 🚫 Blocked overwrite attempt by {bot_name} on {file_name}")

def can_overwrite(file_name, bot_name):
    if is_file_locked(file_name):
        log_attempt(file_name, bot_name)
        return False
    return True

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():