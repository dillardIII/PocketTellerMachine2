from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from flask import Blueprint, jsonify, request
from market_screener_backtest import backtest_market_screener

market_screener_backtest_bp = Blueprint('market_screener_backtest_bp', __name__)

HISTORICAL_DATA_FILE = "data/market_screener_historical_data.json"

@market_screener_backtest_bp.route('/api/market_screener_backtest', methods=['GET'])
def market_screener_backtest_api():
    if not os.path.exists(HISTORICAL_DATA_FILE):
        return jsonify({"status": "error", "message": "Historical data file not found."}), 404

    with open(HISTORICAL_DATA_FILE, "r") as f:
        historical_data = json.load(f)

    results = backtest_market_screener(historical_data)

    return jsonify({
        "status": "success",
        "backtest_results": results,
        "count": len(results)
    })

def log_event():ef drop_files_to_bridge():