from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Fake Crash Injector – Simulates a bot failure so PTM can test fallback recovery.

Used to trigger a self-patch test cycle by logging a fake crash event
into the error_watch.json file.
"""

import json
import os
import time

ERROR_LOG_FILE = "logs/error_watch.json"

def inject_crash(persona="MoCash"):
    fake_error = {
        "timestamp": time.time(),
        "source": persona,
        "type": "Crash",
        "message": "Simulated failure in trade logic."
    }

    if os.path.exists(ERROR_LOG_FILE):
        with open(ERROR_LOG_FILE, "r") as f:
            errors = json.load(f)
    else:
        errors = []

    errors.append(fake_error)

    with open(ERROR_LOG_FILE, "w") as f:
        json.dump(errors, f, indent=4)

    print(f"[TEST] Injected fake crash for: {persona}")

if __name__ == "__main__":
    inject_crash()

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():