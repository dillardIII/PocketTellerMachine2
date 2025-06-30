from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: canon_mode_lock.py ===

# 🔐 Canon Mode – Locks current working files as "known good" state

import os
import hashlib
import json
import datetime

CANON_FILE = "vault/canon_state.json"
WATCH_DIR = "."

def hash_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def lock_canon(files):
    canon = {
        "locked_at": datetime.datetime.now().isoformat(),
        "files": {}
    }

    for file in files:
        if os.path.exists(file):
            canon["files"][file] = hash_file(file)
            print(f"[CanonMode] 🔒 Locked: {file}")
        else:
            print(f"[CanonMode] ⚠️ Missing: {file}")

    with open(CANON_FILE, "w") as f:
        json.dump(canon, f, indent=4)

if __name__ == "__main__":
    files_to_lock = [
        "main.py", "meta_dispatcher.py", "file_exec_engine.py",
        "ghost_evolution_engine.py", "reflex_mutator.py",
        "mission_generator.py", "ghostmind_core.py"
    ]
    lock_canon(files_to_lock)

def log_event():ef drop_files_to_bridge():