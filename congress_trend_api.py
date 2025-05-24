import os
import json
from flask import Blueprint, jsonify, request

congress_trend_bp = Blueprint('congress_trend', __name__)

HISTORY_FILE = 'data/congress_influence_history.json'

# === API to get historical influence data ===
@congress_trend_bp.route('/api/congress_trend', methods=['GET'])
def congress_trend():
    symbol = request.args.get('symbol', 'AAPL').upper()

    if not os.path.exists(HISTORY_FILE):
        return jsonify({"error": "No history data found."}), 404

    with open(HISTORY_FILE, 'r') as file:
        history_data = json.load(file)

    trend_data = []
    for date, scores in history_data.items():
        if symbol in scores:
            trend_data.append({"date": date, "score": scores[symbol]})

    trend_data.sort(key=lambda x: x['date'])

    return jsonify({"symbol": symbol, "trend": trend_data})