from ghost_env import INFURA_KEY, VAULT_ADDRESS
from flask import Blueprint, jsonify
import json
import os

market_screener_bp = Blueprint('market_screener', __name__)

# === Full Market Screener API ===
@market_screener_bp.route('/api/market_screener', methods=['GET'])
def market_screener():
    try:
        screener_file = "data/market_screener.json"

        if os.path.exists(screener_file):
            with open(screener_file, "r") as f:
                screener_data = json.load(f)
            return jsonify(screener_data)
        else:
            # Dummy fallback data for testing
            dummy_data = {
                "top_gainers": [
                    {"ticker": "NVDA", "name": "NVIDIA Corp", "price": 950.25, "change_percent": 3.75},
                    {"ticker": "AMD", "name": "Advanced Micro Devices", "price": 160.12, "change_percent": 2.95}
                ],
                "top_losers": [
                    {"ticker": "BABA", "name": "Alibaba Group", "price": 78.40, "change_percent": -2.15},
                    {"ticker": "NIO", "name": "NIO Inc", "price": 6.50, "change_percent": -1.75}
                ],
                "volume_leaders": [
                    {"ticker": "AAPL", "name": "Apple Inc", "volume": 120_000_000},
                    {"ticker": "TSLA", "name": "Tesla Inc", "volume": 95_000_000}
                ]
            }
            return jsonify(dummy_data)

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500