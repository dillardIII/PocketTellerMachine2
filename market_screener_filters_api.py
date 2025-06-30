from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from flask import Blueprint, jsonify, request

market_screener_filters_bp = Blueprint('market_screener_filters', __name__)

FILTERS_FILE = "data/market_screener_filters.json"

# === Get Current Screener Filters ===
@market_screener_filters_bp.route('/api/screener_filters', methods=['GET'])
def get_screener_filters():
    if os.path.exists(FILTERS_FILE):
        with open(FILTERS_FILE, "r") as f:
            filters = json.load(f)
        return jsonify(filters)
    else:
        return jsonify({})

# === Update Screener Filters ===
@market_screener_filters_bp.route('/api/screener_filters', methods=['POST'])
def update_screener_filters():
    try:
        new_filters = request.get_json()

        with open(FILTERS_FILE, "w") as f:
            json.dump(new_filters, f, indent=2)

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def log_event():ef drop_files_to_bridge():