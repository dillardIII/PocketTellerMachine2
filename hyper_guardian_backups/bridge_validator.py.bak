# === FILE: bridge_validator.py ===
# 🛡️ Bridge Validator – Confirms delivery and integrity of modules at each bridge drop point

import os
import hashlib

# Define where to validate
BRIDGE_DIRS = [
    "bridge/replit_drop/",
    "bridge/predator_drop/",
    "bridge/zfold6_drop/",
    "bridge/s10ultra_drop/"
]

# Generate SHA-256 hash of file contents
def hash_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

# Validate that files match across all bridges using a reference directory
def validate_bridges(reference_dir):
    results = {}
    ref_hashes = {f: hash_file(os.path.join(reference_dir, f))
                  for f in os.listdir(reference_dir) if f.endswith(".py")}
    for bridge in BRIDGE_DIRS:
        bridge_hashes = {f: hash_file(os.path.join(bridge, f))
                         for f in os.listdir(bridge) if f.endswith(".py")}
        mismatches = []
        for f, h in ref_hashes.items():
            if f not in bridge_hashes:
                mismatches.append(f"{f} missing in {bridge}")
            elif bridge_hashes[f] != h:
                mismatches.append(f"{f} hash mismatch in {bridge}")
        results[bridge] = mismatches if mismatches else ["✅ All files match"]
    return results