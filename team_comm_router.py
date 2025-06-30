from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: team_comm_router.py ===
"""
Team Communication Router:
Builds, formats, sends, and logs packets between bot teams.
Supports both JSON inbox files and folder-based packet drops.
"""

import os
import json
from datetime import datetime
from pathlib import Path

# === File-based inbox support ===
COMM_LOG_DIR = "team_logs"
OUTBOX_ROOT = "data/teams"

os.makedirs(COMM_LOG_DIR, exist_ok=True)
Path(OUTBOX_ROOT).mkdir(parents=True, exist_ok=True)

# === Build packet structure ===
def build_packet(sender, recipient, content_type, data):
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "sender": sender,
        "recipient": recipient,
        "type": content_type,
        "data": data
    }

# === Write to inbox .json file (team_logs) ===
def _append_to_json_inbox(packet):
    recipient = packet["recipient"]
    filename = f"{COMM_LOG_DIR}/{recipient.lower()}_inbox.json"

    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump([], f)

    with open(filename, "r") as f:
        inbox = json.load(f)

    inbox.append(packet)

    with open(filename, "w") as f:
        json.dump(inbox, f, indent=2)

# === Send to team inbox folder (data/teams) ===
def _write_to_inbox_folder(packet):
    recipient = packet.get("recipient")
    if not recipient:
        print("[Comm Router] ❌ Missing recipient in packet.")
        return

    inbox_dir = os.path.join(OUTBOX_ROOT, recipient, "inbox")
    Path(inbox_dir).mkdir(parents=True, exist_ok=True)

    safe_timestamp = packet["timestamp"].replace(":", "_").replace(".", "_")
    filename = f"packet_{packet['type']}_{safe_timestamp}.json"
    filepath = os.path.join(inbox_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(packet, f, indent=2)

# === Public: Send packet via both methods ===
def send_packet(packet):
    _append_to_json_inbox(packet)
    _write_to_inbox_folder(packet)
    print(f"[📡 Packet Sent] {packet['sender']} ➜ {packet['recipient']} | {packet['type']}")

# === Optional: Inbox utilities ===
def read_inbox(team_name):
    filename = f"{COMM_LOG_DIR}/{team_name.lower()}_inbox.json"
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        return json.load(f)

def clear_inbox(team_name):
    filename = f"{COMM_LOG_DIR}/{team_name.lower()}_inbox.json"
    with open(filename, "w") as f:
        json.dump([], f)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():