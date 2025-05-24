import os
import json
from flask import Blueprint, jsonify

dashboard_congress_summary_bp = Blueprint('dashboard_congress_summary', __name__)

HISTORY_FILE = 'data/congress_influence_history.json'
WATCHLIST = ['AAPL', 'TSLA', 'MSFT', 'NVDA', 'AMZN']

@dashboard_congress_summary_bp.route('/api/dashboard/congress_summary', methods=['GET'])
def get_congress_summary():
    if not os.path.exists(HISTORY_FILE):
        return jsonify({"summary": {}, "date": "No Data"})

    with open(HISTORY_FILE, 'r') as file:
        history_data = json.load(file)

    if not history_data:
        return jsonify({"summary": {}, "date": "No Data"})

    latest_date = sorted(history_data.keys())[-1]
    scores = []
    for symbol in WATCHLIST:
        score = history_data[latest_date].get(symbol, None)
        if score is not None:
            scores.append({"symbol": symbol, "score": score})

    if not scores:
        return jsonify({"summary": {}, "date": latest_date})

    best = max(scores, key=lambda x: x['score'])
    worst = min(scores, key=lambda x: x['score'])
    average = round(sum(s['score'] for s in scores) / len(scores), 2)

    summary = {
        "best": best,
        "worst": worst,
        "average": average
    }

    return jsonify({"summary": summary, "date": latest_date})