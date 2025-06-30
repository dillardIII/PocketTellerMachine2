from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: file_lock_checker.py ===

import os
import hashlib
import json

HASH_LOG = "locked_file_hashes.json"
WATCH_DIR = "."

def hash_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def load_hashes():
    if not os.path.exists(HASH_LOG):
        return {}
    with open(HASH_LOG, 'r') as f:
        return json.load(f)

def is_file_locked(file_name):
    locked = load_hashes()
    full_path = os.path.join(WATCH_DIR, file_name)
    if not os.path.exists(full_path):
        return False
    current_hash = hash_file(full_path)
    return locked.get(file_name) == current_hash

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():