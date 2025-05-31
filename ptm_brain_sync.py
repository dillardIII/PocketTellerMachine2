# ptm_brain_sync.py

import json
import os
from datetime import datetime

def sync_recon_result(agent_name, result_data):
    """
    Syncs recon result into ptm_brain.json under the recon_logs key.
    agent_name = "Ghostshade", "Cole", etc.
    result_data = {
        "target": "screeps",
        "status": "success",
        "screenshot": "screenshots/dashboard_capture.png",
        "details": "Login confirmed. Dashboard reached.",
        "tool_used": "selenium_wire",
        "timestamp": "ISO-8601 string"
    }
    """
    brain_path = "memory/ptm_brain.json"
    os.makedirs(os.path.dirname(brain_path), exist_ok=True)

    if not os.path.exists(brain_path):
        ptm_brain = {}
    else:
        with open(brain_path, "r") as f:
            try:
                ptm_brain = json.load(f)
            except json.JSONDecodeError:
                ptm_brain = {}

    if "recon_logs" not in ptm_brain:
        ptm_brain["recon_logs"] = []

    result_data["agent"] = agent_name
    result_data["timestamp"] = result_data.get("timestamp", datetime.utcnow().isoformat() + "Z")

    ptm_brain["recon_logs"].append(result_data)

    with open(brain_path, "w") as f:
        json.dump(ptm_brain, f, indent=2)

    print(f"[PTM BRAIN SYNC] Logged recon from {agent_name}")