# === FILE: vote_api_routes.py ===
from flask import Blueprint, jsonify
import os
import json

vote_api = Blueprint("vote_api", __name__)
VOTE_LOG = "evolution/vote_log.json"

@vote_api.route("/api/build_votes")
def build_votes():
    if not os.path.exists(VOTE_LOG):
        return jsonify([])
    with open(VOTE_LOG, "r") as f:
        data = json.load(f)
    return jsonify(data)