from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: response_api_routes.py ===
from flask import Blueprint, jsonify
import os
import json

response_api = Blueprint("response_api", __name__)
RESPONSE_DIR = "bridge_responses"

@response_api.route("/api/packet_responses")
def packet_responses():
    responses = []
    for fname in os.listdir(RESPONSE_DIR):
        if fname.endswith(".json"):
            path = os.path.join(RESPONSE_DIR, fname)
            with open(path, "r") as f:
                data = json.load(f)
            responses.append({
                "filename": fname,
                "responder": data.get("responder"),
                "original_sender": data.get("original_sender"),
                "task": data.get("response_to"),
                "status": data.get("status"),
                "notes": data.get("notes"),
                "timestamp": data.get("timestamp")
            })
    return jsonify(responses)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():