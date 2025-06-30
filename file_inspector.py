from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: file_inspector.py ===
# 🧐 Empire File Inspector – checks for duplicate files & content

import os
import hashlib
from collections import defaultdict

WORKSPACE_DIR = "."
hash_map = defaultdict(list)

def compute_file_hash(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def inspect_files():
    print("[Inspector] 🔍 Scanning for all .py files...")
    for root, dirs, files in os.walk(WORKSPACE_DIR):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                file_hash = compute_file_hash(full_path)
                hash_map[file_hash].append(full_path)

    # Print duplicate hashes
    found_duplicates = False
    for file_hash, paths in hash_map.items():
        if len(paths) > 1:
            print(f"[Inspector] ⚠️ Duplicate content detected in files with hash {file_hash}:")
            for p in paths:
                print(f"    - {p}")
            found_duplicates = True

    if not found_duplicates:
        print("[Inspector] ✅ No duplicate files found by content.")

    # Simple name check
    name_map = defaultdict(list)
    for root, dirs, files in os.walk(WORKSPACE_DIR):
        for file in files:
            if file.endswith(".py"):
                name_map[file].append(os.path.join(root, file))

    for name, paths in name_map.items():
        if len(paths) > 1:
            print(f"[Inspector] ⚠️ Multiple files with name '{name}':")
            for p in paths:
                print(f"    - {p}")

    print("[Inspector] 📝 Inspection complete.")

if __name__ == "__main__":
    inspect_files()

def log_event():ef drop_files_to_bridge():