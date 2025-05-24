from flask import Blueprint, jsonify
import json
import os

market_backtest_bp = Blueprint('market_backtest_bp', __name__)

BACKTEST_DATA_FILE = "data/market_backtest_results.json"

@market_backtest_bp.route('/api/market_backtest', methods=['GET'])
def get_market_backtest():
    try:
        if os.path.exists(BACKTEST_DATA_FILE):
            with open(BACKTEST_DATA_FILE, 'r') as f:
                results = json.load(f)
            return jsonify({"status": "success", "results": results})
        else:
            # Dummy fallback data
            dummy_results = [
                {"ticker": "AAPL", "strategy": "RSI Reversal", "win_rate": 73.2, "avg_return": 5.1},
                {"ticker": "MSFT", "strategy": "Volume Breakout", "win_rate": 65.7, "avg_return": 4.4},
                {"ticker": "TSLA", "strategy": "Momentum Rider", "win_rate": 59.3, "avg_return": 6.9}
            ]
            return jsonify({"status": "success", "results": dummy_results})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})