# trade_logger.py

import json
from pathlib import Path
from datetime import datetime

TRADE_LOG = "logs/trade_log.json"

def load_trades():
    path = Path(TRADE_LOG)
    if path.exists():
        try:
            with open(path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_trades(trades):
    with open(TRADE_LOG, "w") as f:
        json.dump(trades, f, indent=2)

def log_new_trade(trade):
    trades = load_trades()
    trade["logged_at"] = datetime.now().isoformat()
    trades.append(trade)
    save_trades(trades)

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

def log_trade_sell(trade_id, sell_price, result, notes=""):
    update = {
        "sell_price": sell_price,
        "result": result,
        "status": "closed",
        "closed_at": datetime.now().isoformat(),
        "closing_notes": notes
    }
    return update_trade(trade_id, update)