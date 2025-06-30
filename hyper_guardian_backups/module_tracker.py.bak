"""
Module Tracker:
Tracks which modules have been executed by Cole or other PTM bots.
Used for deduplication and smart module reloads.
"""

import os
import json
import hashlib
from datetime import datetime

EXECUTION_TRACKER_FILE = "data/executed_modules.json"

# === Ensure data directory exists ===
os.makedirs(os.path.dirname(EXECUTION_TRACKER_FILE), exist_ok=True)

# === UTILITY: Hash File Contents ===
def hash_file(file_path):
    """
    Returns a SHA-256 hash of the file contents.
    """
    with open(file_path, "rb") as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()

# === LOAD LOG ===
def get_executed_hashes():
    """
    Loads all previously executed module hashes.
    Returns a dictionary: { "module_name.py": "hash" }
    """
    if not os.path.exists(EXECUTION_TRACKER_FILE):
        return {}
    with open(EXECUTION_TRACKER_FILE, "r") as f:
        return json.load(f)

# === UPDATE LOG ===
def update_executed_hash(module_name, file_hash):
    """
    Saves/updates the execution hash for a specific module.
    """
    hashes = get_executed_hashes()
    hashes[module_name] = {
        "hash": file_hash,
        "timestamp": datetime.utcnow().isoformat()
    }

    with open(EXECUTION_TRACKER_FILE, "w") as f:
        json.dump(hashes, f, indent=2)

# === CHECK FOR REPEAT ===
def is_duplicate_execution(module_name, file_hash):
    """
    Checks if the given file hash already exists in the log.
    Returns True if identical module hash already executed.
    """
    hashes = get_executed_hashes()
    existing = hashes.get(module_name, {}).get("hash")
    return existing == file_hash

# === TEST ===
if __name__ == "__main__":
    test_file = "ghostbox/modules/test_script.py"
    if os.path.exists(test_file):
        h = hash_file(test_file)
        is_dupe = is_duplicate_execution("test_script.py", h)
        print("Duplicate?", is_dupe)
        if not is_dupe:
            update_executed_hash("test_script.py", h)