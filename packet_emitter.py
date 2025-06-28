# === FILE: packet_emitter.py ===
# Sends packets (build tasks, signals) to other bot teams

import json
import os
from datetime import datetime

OUTBOX_DIR = "data/outbox"

def emit_packet(target_team, payload):
    os.makedirs(OUTBOX_DIR, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
    packet = {
        "from": "ChatGPT",
        "to": target_team,
        "timestamp": timestamp,
        "payload": payload
    }

    filename = f"{OUTBOX_DIR}/packet_{target_team}_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(packet, f, indent=2)

    print(f"[📦 EMIT] Sent packet to {target_team} | {filename}")