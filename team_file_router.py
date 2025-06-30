from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: team_file_router.py ===
"""
Team File Router:
Handles sending strategy files, upgrades, and feedback files
from one team to another. Supports descriptions, timestamping, and full routing logs.
"""

import os
import shutil
import json
from datetime import datetime
from pathlib import Path

# === Paths ===
TEAM_DIR = "team_files"
FILE_LOG_ROOT = "team_logs/file_transfers"
GLOBAL_LOG_FILE = "team_logs/file_transfer_log.json"

# === Ensure all folders exist ===
os.makedirs(TEAM_DIR, exist_ok=True)
os.makedirs(FILE_LOG_ROOT, exist_ok=True)
os.makedirs(os.path.dirname(GLOBAL_LOG_FILE), exist_ok=True)

# === Ensure per-team directory ===
def ensure_team_dir(team_name):
    team_dir = os.path.join(TEAM_DIR, team_name)
    Path(team_dir).mkdir(parents=True, exist_ok=True)
    return team_dir

# === Main transfer function ===
def send_file_to_team(sender, recipient, file_path, description=""):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"[FILE_ROUTER] File not found: {file_path}")

    team_dir = ensure_team_dir(recipient)
    filename = os.path.basename(file_path)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    new_filename = f"{sender}_{timestamp}_{filename}"
    destination = os.path.join(team_dir, new_filename)

    shutil.copy(file_path, destination)

    # === Log entry ===
    log_entry = {
        "timestamp": timestamp,
        "sender": sender,
        "recipient": recipient,
        "filename": filename,
        "stored_as": new_filename,
        "original_path": file_path,
        "description": description
    }

    _log_file_transfer_global(log_entry)
    _log_file_transfer_per_team(log_entry, recipient)

    print(f"[📁 FILE ROUTED] {sender} ➜ {recipient} | {new_filename}")
    return True

# === Global file log ===
def _log_file_transfer_global(entry):
    if not os.path.exists(GLOBAL_LOG_FILE):
        with open(GLOBAL_LOG_FILE, "w") as f:
            json.dump([], f)

    with open(GLOBAL_LOG_FILE, "r") as f:
        logs = json.load(f)

    logs.append(entry)

    with open(GLOBAL_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

# === Per-team routing log ===
def _log_file_transfer_per_team(entry, recipient):
    log_file = os.path.join(FILE_LOG_ROOT, f"{recipient}_incoming_log.json")
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    with open(log_file, "w") as f:
        json.dump(data, f, indent=2)

def log_event():ef drop_files_to_bridge():