# === FILE: repo_comm_channel.py ===
# Handles communication from PTM Squad to REPO Squad and vice versa

import json
import os
from datetime import datetime

REPO_REQUESTS_FILE = "repo_requests.json"
REPO_LOG_FILE = "logs/repo_comm_log.json"
REPO_SYNC_FILE = "bridge_sync.json"

os.makedirs("logs", exist_ok=True)

def send_to_repo(packet):
    """
    Simulates sending a JSON packet to REPO Squad.
    Logs the outgoing message for audit purposes.
    """
    packet["sent_at"] = datetime.utcnow().isoformat()
    log_repo_message("outgoing", packet)

    with open(REPO_SYNC_FILE, "w") as f:
        json.dump(packet, f, indent=2)

    print("[REPO COMM] 📤 Sent packet to REPO bridge.")

def get_repo_status():
    """
    Retrieves current REPO-side needs or commands.
    """
    if not os.path.exists(REPO_REQUESTS_FILE):
        return {}

    try:
        with open(REPO_REQUESTS_FILE, "r") as f:
            data = json.load(f)
            log_repo_message("incoming", data)
            return data
    except Exception as e:
        print(f"[REPO COMM] ⚠️ Error reading REPO requests: {e}")
        return {}

def log_repo_message(direction, data):
    """
    Logs all REPO communications to a persistent file.
    """
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "direction": direction,
        "data": data
    }

    if os.path.exists(REPO_LOG_FILE):
        with open(REPO_LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(entry)

    # Limit to last 200 entries
    logs = logs[-200:]

    with open(REPO_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)