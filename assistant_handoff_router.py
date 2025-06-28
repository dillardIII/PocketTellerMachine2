"""
Assistant Handoff Router:
Enables bots to pass tasks, data, or requests to one another.
Part of PTM’s autonomy backbone for distributed intelligence.
"""

import json
import os

HANDOFF_FILE = "data/handoff_queue.json"

def init_handoff_queue():
    if not os.path.exists(HANDOFF_FILE):
        with open(HANDOFF_FILE, "w") as f:
            json.dump([], f)

def queue_handoff(sender, receiver, payload):
    handoff = {
        "from": sender,
        "to": receiver,
        "payload": payload,
        "status": "pending"
    }

    with open(HANDOFF_FILE, "r") as f:
        queue = json.load(f)

    queue.append(handoff)

    with open(HANDOFF_FILE, "w") as f:
        json.dump(queue, f, indent=4)

def fetch_handoffs(receiver_name):
    with open(HANDOFF_FILE, "r") as f:
        queue = json.load(f)

    tasks = [h for h in queue if h["to"] == receiver_name and h["status"] == "pending"]
    return tasks

def mark_handoff_complete(handoff):
    with open(HANDOFF_FILE, "r") as f:
        queue = json.load(f)

    for entry in queue:
        if entry == handoff:
            entry["status"] = "done"

    with open(HANDOFF_FILE, "w") as f:
        json.dump(queue, f, indent=4)