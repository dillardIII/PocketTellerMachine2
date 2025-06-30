from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from flask import Blueprint, jsonify

market_scan_bp = Blueprint('market_scan', __name__)

@market_scan_bp.route('/api/market_movers', methods=['GET'])
def get_market_movers():
    try:
        movers_file = "data/market_movers.json"
        if os.path.exists(movers_file):
            with open(movers_file, "r") as f:
                movers_data = json.load(f)
            return jsonify(movers_data)
        else:
            # Dummy fallback data
            dummy_data = {
                "movers": [
                    {"ticker": "AAPL", "name": "Apple Inc.", "change_percent": 2.35},
                    {"ticker": "TSLA", "name": "Tesla Inc.", "change_percent": -1.58}
                ]
            }
            return jsonify(dummy_data)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():