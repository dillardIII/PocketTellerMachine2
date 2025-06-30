from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: sync_bridge_routes.py ===
from flask import Blueprint, jsonify
import os
import json

sync_routes = Blueprint("sync_routes", __name__)
SYNC_DIR = "bridge_fabric"

@sync_routes.route("/api/bridge/<team_name>")
def get_bridge_updates(team_name):
    file_path = os.path.join(SYNC_DIR, f"{team_name}_sync.json")
    if not os.path.exists(file_path):
        return jsonify([])
    with open(file_path, "r") as f:
        return jsonify(json.load(f))

def log_event():ef drop_files_to_bridge():