# === FILE: bridge_syncer.py ===
import os
import json
from datetime import datetime

SYNC_DIR = "bridge_fabric"
os.makedirs(SYNC_DIR, exist_ok=True)

def bridge_update(sender, recipient, memory, instruction="sync"):
    sync_path = os.path.join(SYNC_DIR, f"{recipient}_sync.json")

    entry = {
        "sender": sender,
        "instruction": instruction,
        "memory": memory,
        "timestamp": datetime.utcnow().isoformat()
    }

    if os.path.exists(sync_path):
        with open(sync_path, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    with open(sync_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"[BRIDGE] {sender} → {recipient} | {instruction} | {len(str(memory))} chars")