from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: ghostrade_option_card_route.py ===

from flask import Blueprint, jsonify
import os
import json

option_card_bp = Blueprint("option_card_bp", __name__)
OPTION_CARD_FILE = "data/option_card_config.json"

# === API: Load card configuration ===
@option_card_bp.route("/api/option_cards")
def load_option_cards():
    if not os.path.exists(OPTION_CARD_FILE):
        return jsonify([])

    with open(OPTION_CARD_FILE, "r") as f:
        try:
            data = json.load(f)
        except:
            data = []

    return jsonify(data)

# === API: Save card configuration ===
@option_card_bp.route("/api/save_option_cards", methods=["POST"])
def save_option_cards():
    from flask import request
    data = request.json or []
    os.makedirs("data", exist_ok=True)

    with open(OPTION_CARD_FILE, "w") as f:
        json.dump(data, f, indent=2)

    return jsonify({"status": "saved", "count": len(data)})

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():