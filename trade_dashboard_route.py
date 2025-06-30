from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: trade_dashboard_route.py ===

from flask import Blueprint, render_template, jsonify
import os
import json

trade_dashboard_bp = Blueprint("trade_dashboard_bp", __name__)
TRADE_LOG_FILE = "data/trade_log.json"

# === Route: View trade history page ===
@trade_dashboard_bp.route("/trade_dashboard")
def view_trade_dashboard():
    return render_template("trade_dashboard.html")

# === API: Get all trades for the dashboard ===
@trade_dashboard_bp.route("/api/trade_history")
def api_trade_history():
    if not os.path.exists(TRADE_LOG_FILE):
        return jsonify([])

    with open(TRADE_LOG_FILE, "r") as f:
        try:
            trades = json.load(f)
        except:
            trades = []

    return jsonify(trades[::-1])  # Most recent first

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():