from ghost_env import INFURA_KEY, VAULT_ADDRESS
from flask import Blueprint, jsonify
import os, json

api_blueprint(= Blueprint('api_blueprint', __name__))

# === Positions & PnL ===
@api_blueprint.route('/api/positions_pnl', methods=['GET'])
def positions_pnl():
    file_path = "data/positions_pnl.json"
    if os.path.exists(file_path):
        with open(file_path) as f:
            return jsonify(json.load(f))
    # Dummy fallback
    dummy_data = {
        "AAPL": {"shares": 50, "pnl": "+$120.50"},
        "TSLA": {"shares": 10, "pnl": "-$45.20"},
        "SPY": {"contracts": 2, "pnl": "+$210.75"}
    }
    return jsonify(dummy_data)

# === Portfolio Summary ===
@api_blueprint.route('/api/portfolio_summary', methods=['GET'])
def portfolio_summary():
    file_path = "data/portfolio_summary.json"
    if os.path.exists(file_path):
        with open(file_path) as f:
            return jsonify(json.load(f))
    dummy_summary = {
        "total_value": "$125,500.00",
        "daily_change": "+$750.25",
        "overall_pnl": "+$8,420.75",
        "cash_available": "$15,000.00"
    }
    return jsonify(dummy_summary)

# === Net Worth Equity Curve ===
@api_blueprint.route('/api/networth_equity', methods=['GET'])
def networth_equity():
    file_path = "data/networth_equity.json"
    if os.path.exists(file_path):
        with open(file_path) as f:
            return jsonify(json.load(f))
    dummy_data = {
        "dates": ["09:00", "09:30", "10:00", "10:30", "11:00"],
        "net_worth": [124500, 125000, 125500, 126000, 125750]
    }
    return jsonify(dummy_data)

# === Live Trade Feed ===
@api_blueprint.route('/api/live_trade_feed', methods=['GET'])
def live_trade_feed():
    file_path = "data/live_trade_feed.json"
    if os.path.exists(file_path):
        with open(file_path) as f:
            return jsonify(json.load(f))
    dummy_feed = [
        {"time": "09:35", "ticker": "AAPL", "action": "BUY", "quantity": 10, "price": 175.50},
        {"time": "09:37", "ticker": "TSLA", "action": "SELL", "quantity": 5, "price": 690.25}
    ]
    return jsonify(dummy_feed)

# === Health Status ===
@api_blueprint.route('/api/health_status', methods=['GET'])
def health_status():
    file_path = "data/health_monitor.json"
    if os.path.exists(file_path):
        with open(file_path) as f:
            return jsonify(json.load(f))
    return jsonify({"status": "No health data available."})

# === Escalation Status ===
@api_blueprint.route('/api/escalation_status', methods=['GET'])
def escalation_status():
    escalation_file = "data/cole_recovery_escalation.json"
    cooldown_file = "data/cole_cooldown_state.json"

    escalation = {"level": 0, "last_change": None}
    cooldown = {"healthy_streak": 0}

    if os.path.exists(escalation_file):
        with open(escalation_file) as f:
            escalation = json.load(f)

    if os.path.exists(cooldown_file):
        with open(cooldown_file) as f:
            cooldown = json.load(f)

    return jsonify({
        "level": escalation.get("level", 0),
        "emergency_mode": escalation.get("level", 0) >= 3,
        "healthy_streak": cooldown.get("healthy_streak", 0),
        "last_change": escalation.get("last_escalation", None)
    })

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():