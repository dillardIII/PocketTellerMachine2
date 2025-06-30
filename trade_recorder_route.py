from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: trade_recorder_route.py ===

from flask import Blueprint, request, jsonify
import os
import json
from datetime import datetime

trade_recorder_bp = Blueprint("trade_recorder_bp", __name__)
TRADE_RECORD_FILE = "data/trade_records.json"

# === Internal helper to record a trade ===
def record_trade(trade):
    os.makedirs("data", exist_ok=True)
    history = []
    if os.path.exists(TRADE_RECORD_FILE):
        try:
            with open(TRADE_RECORD_FILE, "r") as f:
                history = json.load(f)
        except:
            history = []

    trade["timestamp"] = datetime.now().isoformat()
    history.append(trade)

    with open(TRADE_RECORD_FILE, "w") as f:
        json.dump(history[-300:], f, indent=2)  # Keep last 300 records

# === API Endpoint ===
@trade_recorder_bp.route("/api/record_trade", methods=["POST"])
def api_record_trade():
    trade = request.json
    if not trade:
        return jsonify({"status": "error", "message": "No trade data provided"}), 400

    record_trade(trade)
    return jsonify({"status": "success", "message": "Trade recorded."})

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():