from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: strategy_thread_logger.py ===
"""
Strategy Thread Logger:
Tracks the full evolution of a strategy — reviewers, upgrades, forks, and comments.
Used for reflection, learning, and building future versions automatically.
"""

import os
import json
from datetime import datetime
from pathlib import Path

THREAD_LOG_DIR = "brain/strategy_threads"
Path(THREAD_LOG_DIR).mkdir(parents=True, exist_ok=True)

def get_thread_log_path(file_name):
    thread_id = file_name.replace(".py", "").replace(" ", "_")
    return os.path.join(THREAD_LOG_DIR, f"{thread_id}_thread.json")

def init_thread(file_name, originator, notes=""):
    """
    Starts a new thread log for a strategy if one doesn't exist.:
    """
    path = get_thread_log_path(file_name)
    if os.path.exists(path):
        return  # Already exists

    thread = {
        "thread_id": file_name,
        "created": datetime.utcnow().isoformat(),
        "originator": originator,
        "history": [{
            "version": "v1",
            "submitted_by": originator,
            "timestamp": datetime.utcnow().isoformat(),
            "notes": notes
        }]
    }

    with open(path, "w") as f:
        json.dump(thread, f, indent=2)
    print(f"[🧠 Thread Init] Created thread for: {file_name}")

def append_to_thread(file_name, version, reviewer, notes=""):
    """
    Appends a new comment, upgrade, or fork entry to a strategy thread.
    """
    path = get_thread_log_path(file_name)
    if not os.path.exists(path):
        print(f"[⚠️ Thread Logger] No thread found for {file_name}. Initializing.")
        init_thread(file_name, reviewer)

    with open(path, "r") as f:
        thread = json.load(f)

    thread["history"].append({
        "version": version,
        "submitted_by": reviewer,
        "timestamp": datetime.utcnow().isoformat(),
        "notes": notes
    })

    with open(path, "w") as f:
        json.dump(thread, f, indent=2)

    print(f"[📝 Thread Update] Logged: {reviewer} on {version}")

def read_thread(file_name):
    path = get_thread_log_path(file_name)
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return json.load(f)

def dump_all_threads():
    all_logs = {}
    for fname in os.listdir(THREAD_LOG_DIR):
        if fname.endswith("_thread.json"):
            with open(os.path.join(THREAD_LOG_DIR, fname), "r") as f:
                all_logs[fname] = json.load(f)
    return all_logs

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():