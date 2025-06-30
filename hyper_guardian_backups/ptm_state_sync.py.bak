# === FILE: ptm_state_sync.py ===

# 🧠 PTM State Sync – Tracks active state for AI bots and writes sync files

import os
import json
from datetime import datetime

def write_state(name, state_data):
    path = f"vault/state_{name}.json"
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "state": state_data
    }

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"[PTM State] 💾 Synced: {name}")