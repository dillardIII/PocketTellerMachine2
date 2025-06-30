from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghost_packet_router.py ===
# Routes packets between bot teams, logs handoffs

import os
import json
import shutil

INBOX = "data/inbox"
OUTBOX = "data/outbox"

def route_packets():
    if not os.path.exists(INBOX):
        os.makedirs(INBOX)

    for fname in os.listdir(INBOX):
        if not fname.endswith(".json"):
            continue

        full_path = os.path.join(INBOX, fname)
        with open(full_path, "r") as f:
            packet = json.load(f)

        destination = packet.get("to")
        if destination:
            target_dir = f"data/teams/{destination}/inbox"
            os.makedirs(target_dir, exist_ok=True)
            shutil.copy(full_path, os.path.join(target_dir, fname))
            print(f"[📡 ROUTER] Routed packet to {destination}")
        
        os.remove(full_path)

def log_event():ef drop_files_to_bridge():