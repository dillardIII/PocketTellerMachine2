from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: file_integrity_checker.py ===
# 🔒 File Integrity Checker – Validates each incoming file’s SHA-256 before install.

import os
import hashlib

BRIDGE_FOLDER = "bridge/outbox"
HASH_FILE = "bridge/expected_files.json"

def compute_sha256(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for block in iter(lambda: f.read(4096), b""):
                sha256.update(block)
        return sha256.hexdigest()
    except Exception as e:
        print(f"[IntegrityChecker] ❌ Failed to compute hash for {filepath}: {e}")
        return None

def check_integrity():
    if not os.path.exists(HASH_FILE):
        print("[IntegrityChecker] ⚠️ No expected_files.json found.")
        return

    try:
        with open(HASH_FILE, "r") as f:
            expected = json.load(f)

        for file, expected_hash in expected.items():
            path = os.path.join(BRIDGE_FOLDER, file)
            if not os.path.isfile(path):
                continue

            actual_hash = compute_sha256(path)
            if actual_hash != expected_hash:
                print(f"[IntegrityChecker] ❌ Mismatch: {file}")
            else:
                print(f"[IntegrityChecker] ✅ Verified: {file}")

    except Exception as e:
        print(f"[IntegrityChecker] ❌ Error during check: {e}")

def log_event():ef drop_files_to_bridge():