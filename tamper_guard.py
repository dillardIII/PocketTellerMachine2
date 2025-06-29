# === FILE: tamper_guard.py ===
# 🛡️ Tamper Guard – Protects your AI from reverse engineering or unauthorized tampering.
# 💀 If violated, will shred itself immediately.

import hashlib
import os
import sys
import time

# === CONFIG: Files to watch ===
WATCH_FILES = ["ghost_autogenesis.py", "quantum_auto_scaler.py", "auto_start.py"]
CHECKSUMS = {}

# === SELF-HASH (for direct reverse-engine protection) ===
SAFE_HASH = "to_be_set_at_deploy"

# === Compute file checksum ===
def compute_checksum(file_path):
    try:
        with open(file_path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except FileNotFoundError:
        return None

# === Initialize baseline checksums ===
def init_checksums():
    for file in WATCH_FILES:
        if os.path.exists(file):
            CHECKSUMS[file] = compute_checksum(file)
        else:
            CHECKSUMS[file] = None

# === Check watched files ===
def check_integrity():
    for file in WATCH_FILES:
        if os.path.exists(file):
            current = compute_checksum(file)
            if CHECKSUMS.get(file) and current != CHECKSUMS[file]:
                print(f"[TamperGuard] 🚨 Tamper detected in {file}! Wiping...")
                try:
                    os.remove(file)
                except:
                    pass
        elif CHECKSUMS.get(file) is not None:
            print(f"[TamperGuard] ⚠️ Expected file missing: {file}")

# === Direct self-integrity check ===
def verify_self_integrity():
    try:
        with open(sys.argv[0], "rb") as f:
            self_hash = hashlib.sha256(f.read()).hexdigest()
        if self_hash != SAFE_HASH and SAFE_HASH != "to_be_set_at_deploy":
            print("[TamperGuard] 🚨 SELF-CHECK FAILED – SHREDDING SELF")
            os.remove(sys.argv[0])
            sys.exit(1)
    except Exception as e:
        print(f"[TamperGuard] ERROR during self-check: {e}")

# === Start protection ===
print("[TamperGuard] 🛡️ Tamper protection engaged.")
init_checksums()
verify_self_integrity()

while True:
    check_integrity()
    verify_self_integrity()
    time.sleep(30)