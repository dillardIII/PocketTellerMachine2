from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bridge_sync_engine.py ===
# 🌉 AI Bridge Sync Engine – Syncs files, thoughts, and directives between Replit, ChatGPT, and PTM

import json
from datetime import datetime
from pathlib import Path

BRIDGE_FILE = "state/bridge_status.json"
Path("state").mkdir(exist_ok=True)

BRIDGE_TEMPLATE = {
    "last_updated": None,
    "connected_agents": {
        "ChatGPT_Commander": "active",
        "Replit_Commander": "active",
        "PTM_Commander": "active"
    },
    "transfer_log": [],
    "errors": [],
    "last_file_transferred": None,
    "relay_sync_mode": "handshake"
}

def load_bridge_state():
    if not Path(BRIDGE_FILE).exists():
        with open(BRIDGE_FILE, "w", encoding="utf-8") as f:
            json.dump(BRIDGE_TEMPLATE, f, indent=2)
    with open(BRIDGE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def update_bridge_state(agent_from, agent_to, file_path, status="success", error=None):
    state = load_bridge_state()
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    state["last_updated"] = timestamp
    state["last_file_transferred"] = file_path

    log_entry = {
        "from": agent_from,
        "to": agent_to,
        "file": file_path,
        "status": status,
        "timestamp": timestamp
    }

    state["transfer_log"].append(log_entry)
    if error:
        state["errors"].append({"error": error, "timestamp": timestamp, "file": file_path})

    with open(BRIDGE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

    print(f"[BRIDGE] 🌐 Transfer {status.upper()} from {agent_from} to {agent_to}: {file_path}")
    return state

def get_bridge_status():
    return load_bridge_state()

def log_event():ef drop_files_to_bridge():