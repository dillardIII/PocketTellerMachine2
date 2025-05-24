from flask import Blueprint, jsonify
import os
import json

backtest_log_bp = Blueprint('backtest_log', __name__)

@backtest_log_bp.route('/api/backtest_log', methods=['GET'])
def get_backtest_log():
    try:
        log_path = os.path.join("data", "backtest_log.json")
        if os.path.exists(log_path):
            with open(log_path, "r") as f:
                logs = json.load(f)
        else:
            logs = []
        return jsonify({"logs": logs})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500