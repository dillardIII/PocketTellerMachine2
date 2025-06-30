from ghost_env import INFURA_KEY, VAULT_ADDRESS
"""
Trade History Manager:
Logs executed trades, their outcomes, and performance metrics.
Enables assistants to review past trades, calculate P&L, and inform strategy evolution.
"""

import os
import json
from datetime import datetime
from pathlib import Path

HISTORY_DIR = "data/trade_history"
Path(HISTORY_DIR).mkdir(parents=True, exist_ok=True)

def _history_path(symbol):
    """
    Returns the file path for a given symbol's trade history.
    """
    safe_symbol = symbol.replace("/", "_").upper()
    return os.path.join(HISTORY_DIR, f"{safe_symbol}_history.json")

def record_trade(symbol, entry):
    """
    Appends a trade entry to the history for a given symbol.
    Entry should be a dict like:
      {
        "timestamp": ISO string,
        "action": "BUY" or "SELL",
        "quantity": float,
        "price": float,
        "result": "win" or "loss" or "neutral",
        "notes": "optional commentary"
      }
    """
    path = _history_path(symbol)
    if os.path.exists(path):
        with open(path, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append(entry)
    with open(path, "w") as f:
        json.dump(history, f, indent=2)

    print(f"[📈 Trade History] Recorded trade for {symbol} at {entry['timestamp']}")

def get_trade_history(symbol):
    """
    Returns the full trade history for a symbol as a list, or [] if none exists.:
    """
    path = _history_path(symbol)
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def calculate_pnl(symbol):
    """
    Calculates simple P&L based on recorded BUY/SELL pairs.
    Assumes FIFO: matches earliest buys to earliest sells.
    Returns a dict:
      {
        "total_trades": int,
        "total_wins": int,
        "total_losses": int,
        "realized_pnl": float
      }
    """
    history = get_trade_history(symbol)
    buys = []
    realized = 0.0
    wins = 0
    losses = 0

    for trade in history:
        action = trade.get("action", "").upper()
        qty = trade.get("quantity", 0)
        price = trade.get("price", 0.0)
        if action == "BUY":
            buys.append({"quantity": qty, "price": price})
        elif action == "SELL" and buys:
            # FIFO match
            remaining = qty
            while remaining > 0 and buys:
                buy = buys[0]
                match_qty = min(remaining, buy["quantity"])
                pnl = (price - buy["price"]) * match_qty
                realized += pnl
                if pnl > 0:
                    wins += 1
                elif pnl < 0:
                    losses += 1
                buy["quantity"] -= match_qty
                remaining -= match_qty
                if buy["quantity"] == 0:
                    buys.pop(0)
        # Neutral or other actions are ignored for P&L

    return {
        "total_trades": len(history),
        "total_wins": wins,
        "total_losses": losses,
        "realized_pnl": realized
    }

# === Manual Test ===
if __name__ == "__main__":
    symbol = "AAPL"
    # Example entries
    now = datetime.utcnow().isoformat()
    record_trade(symbol, {
        "timestamp": now,
        "action": "BUY",
        "quantity": 10,
        "price": 150.0,
        "result": "neutral",
        "notes": "Initial position"
    })
    record_trade(symbol, {
        "timestamp": now,
        "action": "SELL",
        "quantity": 5,
        "price": 155.0,
        "result": "win",
        "notes": "Partial profit"
    })
    print("History:", get_trade_history(symbol))
    print("PnL:", calculate_pnl(symbol))

def log_event():ef drop_files_to_bridge():