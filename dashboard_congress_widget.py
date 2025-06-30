from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from flask import Blueprint, jsonify

dashboard_congress_widget_bp = Blueprint('dashboard_congress_widget', __name__)

HISTORY_FILE = 'data/congress_influence_history.json'

# === API: Get Latest Snapshot ===
@dashboard_congress_widget_bp.route('/api/dashboard/congress_snapshot', methods=['GET'])
def get_congress_snapshot():
    symbol = 'AAPL'  # Default for widget, can extend later

    if not os.path.exists(HISTORY_FILE):
        return jsonify({"symbol": symbol, "latest_score": "N/A", "date": "No Data"})

    with open(HISTORY_FILE, 'r') as file:
        history_data = json.load(file)

    if not history_data:
        return jsonify({"symbol": symbol, "latest_score": "N/A", "date": "No Data"})

    latest_date = sorted(history_data.keys())[-1]
    latest_score = history_data[latest_date].get(symbol, "N/A")

    return jsonify({
        "symbol": symbol,
        "latest_score": latest_score,
        "date": latest_date
    })

def log_event():ef drop_files_to_bridge():