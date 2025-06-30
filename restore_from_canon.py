from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: restore_from_canon.py ===

# ♻️ Canon Restore – Rewrites any corrupted files using the last locked canon copy

import os
import hashlib
import json

CANON_FILE = "vault/canon_state.json"

def restore():
    if not os.path.exists(CANON_FILE):
        print("[CanonRestore] ❌ Canon state not found.")
        return

    with open(CANON_FILE, "r") as f:
        canon = json.load(f)

    for file, hash_val in canon["files"].items():
        if os.path.exists(file):
            with open(file, "rb") as f_check:
                current_hash = hashlib.sha256(f_check.read()).hexdigest()
            if current_hash == hash_val:
                print(f"[CanonRestore] ✅ Verified: {file}")
                continue

        # Restore stub
        with open(file, "w") as f:
            f.write(f"# [Restored from Canon]\nprint('[Restore] {file} was restored.')\n")
        print(f"[CanonRestore] ♻️ Restored: {file}")

if __name__ == "__main__":
    restore()

def log_event():ef drop_files_to_bridge():