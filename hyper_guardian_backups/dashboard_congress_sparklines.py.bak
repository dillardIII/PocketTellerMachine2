import os
import json
from flask import Blueprint, jsonify, request

dashboard_congress_sparklines_bp = Blueprint('dashboard_congress_sparklines', __name__)

HISTORY_FILE = 'data/congress_influence_history.json'
WATCHLIST = ['AAPL', 'TSLA', 'MSFT', 'NVDA', 'AMZN']

@dashboard_congress_sparklines_bp.route('/api/dashboard/congress_sparklines', methods=['GET'])
def get_congress_sparklines():
    if not os.path.exists(HISTORY_FILE):
        return jsonify({"data": []})

    with open(HISTORY_FILE, 'r') as file:
        history_data = json.load(file)

    result = []
    dates = sorted(history_data.keys())
    for symbol in WATCHLIST:
        scores = []
        for date in dates:
            score = history_data[date].get(symbol, None)
            if score is not None:
                scores.append({"date": date, "score": score})
        if scores:
            result.append({"symbol": symbol, "history": scores})

    return jsonify({"data": result})