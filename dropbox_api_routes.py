# === FILE: dropbox_api_routes.py ===
from flask import Blueprint, jsonify, request
import os
import json

dropbox_api = Blueprint("dropbox_api", __name__)
DROPBOX_DIR = "team_dropboxes"

@dropbox_api.route("/api/dropbox/<team_name>")
def get_team_dropbox(team_name):
    dropbox_path = os.path.join(DROPBOX_DIR, f"{team_name}_dropbox.json")
    if not os.path.exists(dropbox_path):
        return jsonify([])
    with open(dropbox_path, "r") as f:
        data = json.load(f)
    return jsonify(data)