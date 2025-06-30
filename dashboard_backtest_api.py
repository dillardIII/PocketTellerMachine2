from ghost_env import INFURA_KEY, VAULT_ADDRESS
from flask import Blueprint, jsonify
import json
import os

BACKTEST_LOG_FILE = "data/market_backtest_logs.json"

market_backtest_api = Blueprint('market_backtest_api', __name__)

@market_backtest_api.route("/api/backtest_logs", methods=["GET"])
def get_backtest_logs():
    if os.path.exists(BACKTEST_LOG_FILE):
        with open(BACKTEST_LOG_FILE, "r") as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify({"logs": [], "status": "No log file found."}), 404

def log_event():ef drop_files_to_bridge():