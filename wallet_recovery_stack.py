# === FILE: wallet_recovery_stack.py ===
# 🪙 Wallet Recovery Stack - hunts, recombines, and tests key fragments from vault
# Runs as a persistent process to constantly attempt key recovery.

import json
import os
import time
from datetime import datetime

VAULT_PATH = "./vault/"
PARTIAL_KEYS_FILE = os.path.join(VAULT_PATH, "partial_keys.json")
FOUND_KEYS_FILE = os.path.join(VAULT_PATH, "recovered_keys.json")
LOG_FILE = os.path.join(VAULT_PATH, "wallet_recovery_log.txt")

def load_json(path):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def save_json(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def append_log(message):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def recombine_keys(partials):
    # Simulated brute attempt - combines every pair
    found = []
    for i in range(len(partials)):
        for j in range(i+1, len(partials)):
            combined = partials[i] + partials[j]
            if len(combined) == 64:  # pretend valid private key length
                found.append(combined)
                append_log(f"Recovered key from {partials[i]} + {partials[j]}")
    return found

def main():
    append_log("🚀 Wallet Recovery Stack started.")
    while True:
        partials = load_json(PARTIAL_KEYS_FILE)
        recovered = load_json(FOUND_KEYS_FILE)
        new_keys = recombine_keys(partials)
        for key in new_keys:
            if key not in recovered:
                recovered.append(key)
                append_log(f"✅ New recovered key: {key}")
        save_json(recovered, FOUND_KEYS_FILE)
        time.sleep(10)  # loop every 10 sec

if __name__ == "__main__":
    main()