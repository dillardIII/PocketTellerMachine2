"""
Bridge Commander – PTM's AI-to-AI Communication Nexus

This module controls the communication bridges between AI assistants,
modules, and devices. Handles task dispatching, message passing,
and inter-AI protocol for autonomous collaboration.
"""

import json
import os
from datetime import datetime

BRIDGE_LOG_FILE = "logs/bridge_log.json"
BRIDGE_QUEUE_FILE = "data/bridge_queue.json"

def log_bridge_event(source, destination, event, payload=None):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "from": source,
        "to": destination,
        "event": event,
        "payload": payload
    }

    if not os.path.exists(BRIDGE_LOG_FILE):
        with open(BRIDGE_LOG_FILE, "w") as f:
            json.dump([], f)

    with open(BRIDGE_LOG_FILE, "r") as f:
        logs = json.load(f)

    logs.append(log_entry)

    with open(BRIDGE_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)


def send_bridge_packet(source, destination, payload):
    packet = {
        "from": source,
        "to": destination,
        "payload": payload,
        "status": "pending",
        "timestamp": datetime.utcnow().isoformat()
    }

    if not os.path.exists(BRIDGE_QUEUE_FILE):
        with open(BRIDGE_QUEUE_FILE, "w") as f:
            json.dump([], f)

    with open(BRIDGE_QUEUE_FILE, "r") as f:
        queue = json.load(f)

    queue.append(packet)

    with open(BRIDGE_QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=4)

    log_bridge_event(source, destination, "packet_sent", payload)


def fetch_bridge_packets(receiver_name):
    if not os.path.exists(BRIDGE_QUEUE_FILE):
        return []

    with open(BRIDGE_QUEUE_FILE, "r") as f:
        queue = json.load(f)

    packets = [p for p in queue if p["to"] == receiver_name and p["status"] == "pending"]
    return packets


def mark_packet_complete(packet):
    with open(BRIDGE_QUEUE_FILE, "r") as f:
        queue = json.load(f)

    for entry in queue:
        if entry == packet:
            entry["status"] = "complete"

    with open(BRIDGE_QUEUE_FILE, "w") as f:
        json.dump(queue, f, indent=4)

    log_bridge_event(packet["from"], packet["to"], "packet_complete", packet["payload"])