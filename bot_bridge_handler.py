from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: bot_bridge_handler.py ===
"""
Bot Bridge Handler:
Manages secure task and file transfers between PTM bots.
Supports bridge routing, handoffs, message queuing, and follow-ups.
"""

import os
import json
from datetime import datetime
from pathlib import Path

BRIDGE_DIR = "bridges"
Path(BRIDGE_DIR).mkdir(exist_ok=True)

def get_bridge_file(sender, receiver):
    return os.path.join(BRIDGE_DIR, f"{sender}_to_{receiver}.json")

def init_bridge(sender, receiver):
    path = get_bridge_file(sender, receiver)
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump({"messages": []}, f, indent=2)
        print(f"[🌉 Bot Bridge] Initialized: {sender} ➡ {receiver}")

def send_to_bot(sender, receiver, payload, task="review", file=None):
    path = get_bridge_file(sender, receiver)
    if not os.path.exists(path):
        init_bridge(sender, receiver)

    with open(path, "r") as f:
        bridge_data = json.load(f)

    message = {
        "timestamp": datetime.utcnow().isoformat(),
        "from": sender,
        "to": receiver,
        "task": task,
        "payload": payload,
        "file": file,
        "status": "pending"
    }

    bridge_data["messages"].append(message)

    with open(path, "w") as f:
        json.dump(bridge_data, f, indent=2)

    print(f"[📨 Bot Bridge] Task sent from {sender} to {receiver} — task: {task}")

def read_bridge(receiver):
    """
    Returns list of pending messages for the receiver.
    """
    results = []
    for fname in os.listdir(BRIDGE_DIR):
        if fname.endswith(".json") and f"_to_{receiver}" in fname:
            with open(os.path.join(BRIDGE_DIR, fname), "r") as f:
                data = json.load(f)
                pending = [msg for msg in data["messages"] if msg["status"] == "pending"]:
                results.extend(pending)
    return results

def mark_task_complete(sender, receiver, timestamp):
    path = get_bridge_file(sender, receiver)
    if not os.path.exists(path):
        return

    with open(path, "r") as f:
        bridge_data = json.load(f)

    for msg in bridge_data["messages"]:
        if msg["timestamp"] == timestamp:
            msg["status"] = "done"
            break

    with open(path, "w") as f:
        json.dump(bridge_data, f, indent=2)
    print(f"[✅ Bot Bridge] Task marked complete: {timestamp}")

# === Optional Test ===
if __name__ == "__main__":
    send_to_bot("MoCash", "Mentor", {"symbol": "AAPL", "rating": 90}, task="review", file="AAPL_strategy_v1.py")
    print(read_bridge("Mentor"))

def log_event():ef drop_files_to_bridge():