from flask import Blueprint, jsonify
import os
import json

trade_log_bp = Blueprint('trade_log', __name__)

@trade_log_bp.route('/api/trade_log', methods=['GET'])
def get_trade_log():
    try:
        trade_log_path = os.path.join("data", "trades.json")
        if os.path.exists(trade_log_path):
            with open(trade_log_path, "r") as f:
                trades = json.load(f)
        else:
            trades = []
        return jsonify({"trades": trades})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500