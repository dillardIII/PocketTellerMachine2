# === FILE: packet_api_routes.py ===
from flask import Blueprint, jsonify
import os
import json

packet_api = Blueprint("packet_api", __name__)
INBOX_DIR = "bridge_packets"

@packet_api.route("/api/inbox_packets")
def inbox_packets():
    packets = []
    for fname in os.listdir(INBOX_DIR):
        if fname.endswith(".json"):
            fpath = os.path.join(INBOX_DIR, fname)
            with open(fpath, "r") as f:
                data = json.load(f)
            packets.append({
                "filename": fname,
                "sender": data.get("sender"),
                "recipient": data.get("recipient"),
                "task_name": data.get("task_name"),
                "instructions": data.get("instructions"),
                "file_count": len(data.get("files", {}))
            })
    return jsonify(packets)