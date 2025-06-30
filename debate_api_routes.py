from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: debate_api_routes.py ===
from flask import Blueprint, jsonify
import os
import json

debate_api = Blueprint("debate_api", __name__)
DEBATE_LOG = "team_intel/debate_log.json"

@debate_api.route("/api/debates")
def get_debates():
    if not os.path.exists(DEBATE_LOG):
        return jsonify([])
    with open(DEBATE_LOG, "r") as f:
        debates = json.load(f)
    return jsonify(debates)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():