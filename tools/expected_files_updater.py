# === FILE: tools/expected_files_updater.py ===

# 🔄 Expected Files Updater – Recalculates SHA-256 hashes and updates expected_files.json
# Used to keep PTM file validation accurate after changes or GhostForge rebuilds

import os
import json
import hashlib

EXPECTED_FILE = "config/expected_files.json"

def calculate_sha256(filepath):
    try:
        with open(filepath, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception as e:
        print(f"[Updater] ❌ Error hashing {filepath}: {e}")
        return None

def update_hashes():
    if not os.path.exists(EXPECTED_FILE):
        print("[Updater] ❌ expected_files.json not found.")
        return

    with open(EXPECTED_FILE, "r") as f:
        expected = json.load(f)

    updated_count = 0

    for path in expected:
        abs_path = os.path.join(".", path)
        if os.path.exists(abs_path):
            sha256 = calculate_sha256(abs_path)
            if sha256:
                expected[path]["sha256"] = sha256
                updated_count += 1
        else:
            print(f"[Updater] ⚠️ Missing: {path}")

    with open(EXPECTED_FILE, "w") as f:
        json.dump(expected, f, indent=2)

    print(f"[Updater] ✅ Updated {updated_count} file hash(es) in expected_files.json")

if __name__ == "__main__":
    update_hashes()