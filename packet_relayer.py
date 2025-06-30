from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Packet Relayer – Logs, handles, and echoes internal packets between modules

Purpose:
- Relay messages between assistant modules
- Log incoming packets
- Echo test for network communication
"""

from flask import Blueprint, request, jsonify
import datetime
import os
import json

packet_relayer = Blueprint("packet_relayer", __name__)

PACKET_LOG_DIR = "team_files/packet_logs"
os.makedirs(PACKET_LOG_DIR, exist_ok=True)

@packet_relayer.route("/api/packet/send", methods=["POST"])
def relay_packet():
    data = request.get_json()
    packet_type = data.get("type", "generic")
    payload = data.get("payload", {})
    sender = data.get("sender", "unknown")

    # Save packet
    timestamp = datetime.datetime.utcnow().isoformat()
    filename = f"{packet_type}_{timestamp.replace(':', '-')}.json"
    filepath = os.path.join(PACKET_LOG_DIR, filename)
    
    with open(filepath, "w") as f:
        json.dump({
            "timestamp": timestamp,
            "type": packet_type,
            "sender": sender,
            "payload": payload
        }, f, indent=2)

    print(f"[PacketRelayer] Packet saved: {filename}")
    return jsonify({"status": "success", "message": f"Packet {filename} saved."})

@packet_relayer.route("/api/packet/echo", methods=["GET"])
def echo_test():
    return jsonify({
        "status": "online",
        "message": "PacketRelayer operational.",
        "timestamp": datetime.datetime.utcnow().isoformat()
    })

def log_event():ef drop_files_to_bridge():