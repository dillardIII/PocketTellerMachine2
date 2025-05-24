from flask import Blueprint, jsonify, request
import os
import json
from datetime import datetime

BACKTEST_LOG_FILE = "data/market_screener_backtest_log.json"

market_screener_backtest_bp = Blueprint('market_screener_backtest', __name__)

# === Load Backtest Logs ===
def load_backtest_logs():
    if not os.path.exists(BACKTEST_LOG_FILE):
        return []
    with open(BACKTEST_LOG_FILE, "r") as f:
        return json.load(f)

# === Save Backtest Logs ===
def save_backtest_logs(logs):
    with open(BACKTEST_LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

# === API: Get Backtest Logs ===
@market_screener_backtest_bp.route('/api/backtest_logs', methods=['GET'])
def get_backtest_logs():
    logs = load_backtest_logs()
    return jsonify({"logs": logs})

# === API: Add New Backtest Result ===
@market_screener_backtest_bp.route('/api/backtest_logs', methods=['POST'])
def add_backtest_result():
    try:
        data = request.get_json()

        entry = {
            "timestamp": datetime.now().isoformat(),
            "ticker": data.get("ticker"),
            "price": data.get("price"),
            "volume": data.get("volume"),
            "rsi": data.get("rsi"),
            "signal": data.get("signal"),
            "result": data.get("result")
        }

        logs = load_backtest_logs()
        logs.append(entry)
        save_backtest_logs(logs)

        return jsonify({"status": "success", "message": "Backtest result logged."})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500