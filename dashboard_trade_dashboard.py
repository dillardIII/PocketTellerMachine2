from ghost_env import INFURA_KEY, VAULT_ADDRESS
from flask import Blueprint, jsonify
import os
import json

trade_dashboard_bp = Blueprint('trade_dashboard', __name__)

@trade_dashboard_bp.route('/api/trade_dashboard', methods=['GET'])
def get_trade_dashboard():
    try:
        file_path = os.path.join("data", "trades.json")
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                trades = json.load(f)
        else:
            trades = []
        return jsonify({"dashboard": trades})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

def log_event():ef drop_files_to_bridge():