import os
import json
from flask import Blueprint, jsonify

market_screener_bp = Blueprint('market_screener', __name__)

@market_screener_bp.route('/api/market_screener', methods=['GET'])
def get_market_screener():
    try:
        screener_file = "data/market_screener.json"
        if os.path.exists(screener_file):
            with open(screener_file, "r") as f:
                screener_data = json.load(f)
            return jsonify(screener_data)
        else:
            # Dummy fallback data
            dummy_data = {
                "results": [
                    {"ticker": "AAPL", "price": 175.50, "volume": 12000000, "rsi": 52.3, "signal": "BUY"},
                    {"ticker": "TSLA", "price": 690.25, "volume": 8000000, "rsi": 47.8, "signal": "HOLD"}
                ]
            }
            return jsonify(dummy_data)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500