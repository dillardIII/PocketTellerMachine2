# auto_repair_bot.py

import os
import json
from datetime import datetime
from file_autowriter import write_file

# Define default content templates here or load from templates directory
DEFAULT_TEMPLATES = {
    "ptm_brain.json": "{}",
    "cole_watchlist.json": "[]",
    "ghostshade_core.json": json.dumps({
        "name": "Ghostshade the Unseen",
        "title": "Phantom Recon Officer",
        "missions": [],
        "last_activity": None
    }, indent=2)
}


def check_and_repair(file_path):
    """
    Checks if a file exists and is valid JSON.
    If not, restores from DEFAULT_TEMPLATES or creates a blank file.
    """
    if not os.path.exists(file_path):
        print(f"[REPAIR] Missing file: {file_path} — attempting to create...")
        return restore_default(file_path)

    try:
        with open(file_path, 'r') as f:
            json.load(f)
        print(f"[REPAIR] {file_path} is valid.")
        return True
    except Exception as e:
        print(f"[REPAIR WARNING] {file_path} is corrupted: {str(e)}")
        return restore_default(file_path)


def restore_default(file_path):
    """
    Restores a default version of a file using write_file()
    """
    filename = os.path.basename(file_path)
    default_content = DEFAULT_TEMPLATES.get(filename, "{}")
    success = write_file(file_path, default_content)
    if success:
        log_repair(file_path)
    return success


def log_repair(file_path):
    """
    Logs the repair attempt to /memory/repair_log.json
    """
    log_file = "memory/repair_log.json"
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    entry = {
        "file": file_path,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "status": "repaired"
    }

    try:
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                data = json.load(f)
        else:
            data = []

        data.append(entry)
        with open(log_file, 'w') as f:
            json.dump(data, f, indent=2)

        print(f"[REPAIR LOGGED] {file_path}")
    except Exception as e:
        print(f"[REPAIR LOG ERROR] {str(e)}")