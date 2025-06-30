from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Bot Packet Relay:
Supports structured data handoffs between bots (strategies, plans, alerts, trade info).
Used for transmitting trade packets, status updates, and collaborative builds.
"""

import os
import json
from datetime import datetime
from pathlib import Path

RELAY_DIR = "brain/bot_packets"
Path(RELAY_DIR).mkdir(parents=True, exist_ok=True)

def send_packet(sender, receiver, packet_type, payload):
    """
    Send a structured packet from one bot to another.
    """
    timestamp = datetime.utcnow().isoformat()
    packet = {
        "sender": sender,
        "receiver": receiver,
        "packet_type": packet_type,
        "payload": payload,
        "timestamp": timestamp
    }

    filename = f"{receiver}_packets.json"
    path = os.path.join(RELAY_DIR, filename)

    existing = []
    if os.path.exists(path):
        with open(path, "r") as f:
            existing = json.load(f)

    existing.append(packet)

    with open(path, "w") as f:
        json.dump(existing, f, indent=2)

    print(f"[📦 Packet Relay] {sender} ➡ {receiver} | Type: {packet_type}")

def read_packets(receiver):
    """
    Retrieve all packets sent to a receiver.
    """
    path = os.path.join(RELAY_DIR, f"{receiver}_packets.json")
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def clear_packets(receiver):
    """
    Clear all packets for a bot.
    """
    path = os.path.join(RELAY_DIR, f"{receiver}_packets.json")
    if os.path.exists(path):
        os.remove(path)
        print(f"[🧽 Packet Relay] Cleared packets for {receiver}")

def log_event():ef drop_files_to_bridge():