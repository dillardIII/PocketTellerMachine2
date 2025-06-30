from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from flask import Blueprint, jsonify

dashboard_congress_heatmap_bp = Blueprint('dashboard_congress_heatmap', __name__)

HISTORY_FILE = 'data/congress_influence_history.json'
WATCHLIST = ['AAPL', 'TSLA', 'MSFT', 'NVDA', 'AMZN']

@dashboard_congress_heatmap_bp.route('/api/dashboard/congress_heatmap', methods=['GET'])
def get_congress_heatmap():
    if not os.path.exists(HISTORY_FILE):
        return jsonify({"watchlist": [], "date": "No Data"})

    with open(HISTORY_FILE, 'r') as file:
        history_data = json.load(file)

    if not history_data:
        return jsonify({"watchlist": [], "date": "No Data"})

    latest_date = sorted(history_data.keys())[-1]
    result = []
    for symbol in WATCHLIST:
        score = history_data[latest_date].get(symbol, None)
        if score is not None:
            result.append({"symbol": symbol, "score": score})

    return jsonify({
        "watchlist": result,
        "date": latest_date
    })

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():