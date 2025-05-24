import os
import json
from pathlib import Path
from datetime import datetime

from grade_utils import calculate_grade
from cole_memory_brain import log_memory_event
from strategy_leaderboard import update_leaderboard_with_trade  # NEW

# === Paths ===
TRADE_LOG = "logs/trade_log.json"
DATA_LOG = "data/trades.json"

# === Ensure folders exist ===
os.makedirs("logs", exist_ok=True)
os.makedirs("data", exist_ok=True)

# === Load Trades from logs/trade_log.json ===
def load_trades():
    path = Path(TRADE_LOG)
    if path.exists():
        try:
            with open(path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

# === Save to logs/trade_log.json ===
def save_trades(trades):
    with open(TRADE_LOG, "w") as f:
        json.dump(trades, f, indent=2)

# === Log New Trade to logs/trade_log.json ===
def log_new_trade(trade):
    trades = load_trades()
    trade["logged_at"] = datetime.now().isoformat()
    trades.append(trade)
    save_trades(trades)

# === Update Specific Trade by ID ===
def update_trade(trade_id, updates):
    trades = load_trades()
    found = False
    for trade in trades:
        if trade.get("id") == trade_id:
            trade.update(updates)
            found = True
            break
    save_trades(trades)
    return found

# === Log a Closed Trade ===
def log_trade_sell(trade_id, sell_price, result, notes=""):
    update = {
        "sell_price": sell_price,
        "result": result,
        "status": "closed",
        "closed_at": datetime.now().isoformat(),
        "closing_notes": notes
    }
    return update_trade(trade_id, update)

# === Log to data/trades.json (used by dashboards) ===
def log_trade(data):
    if os.path.exists(DATA_LOG):
        with open(DATA_LOG, "r") as f:
            trades = json.load(f)
    else:
        trades = []

    trades.append(data)
    with open(DATA_LOG, "w") as f:
        json.dump(trades, f, indent=2)

    update_leaderboard_with_trade(data)  # NEW HOOK
    print(f"[TRADE LOG] {data['symbol']} | {data['result']} | Grade {data['grade']}")

# === Smart Trade Logger — fusion with memory + grading ===
def log_trade_to_memory(trade_data):
    result = trade_data.get("result", 0)
    grade = calculate_grade(result)
    trade_entry = {
        "id": trade_data.get("id"),
        "symbol": trade_data.get("symbol"),
        "strategy": trade_data.get("strategy"),
        "result": result,
        "grade": grade,
        "timestamp": datetime.now().isoformat(),
        "voice_summary": trade_data.get("voice_summary", f"Executed {trade_data.get('strategy')} on {trade_data.get('symbol')} with result {result}.")
    }

    log_memory_event("trades", trade_entry)
    update_leaderboard_with_trade(trade_entry)  # NEW HOOK
    print(f"[TRADE LOGGED & GRADED]: {trade_entry}")
    return trade_entry