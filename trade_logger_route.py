from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: trade_logger_route.py ===

from flask import Blueprint, request, jsonify
import os
import json
from datetime import datetime

trade_logger_bp = Blueprint("trade_logger_bp", __name__)
TRADE_LOG_FILE = "data/trade_log.json"

# === Helper to log a trade ===
def log_trade(trade_data):
    os.makedirs("data", exist_ok=True)
    log = []
    if os.path.exists(TRADE_LOG_FILE):
        with open(TRADE_LOG_FILE, "r") as f:
            try:
                log = json.load(f)
            except:
                log = []

    trade_data["timestamp"] = datetime.now().isoformat()
    log.append(trade_data)

    with open(TRADE_LOG_FILE, "w") as f:
        json.dump(log[-500:], f, indent=2)  # Keep last 500 trades max

# === API to receive and store a trade ===
@trade_logger_bp.route("/api/log_trade", methods=["POST"])
def api_log_trade():
    trade = request.json
    if not trade:
        return jsonify({"status": "error", "message": "No trade data provided"}), 400

    log_trade(trade)
    return jsonify({"status": "success", "message": "Trade logged."})

def log_event():ef drop_files_to_bridge():