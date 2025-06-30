from ghost_env import INFURA_KEY, VAULT_ADDRESS
import json
import os
from datetime import datetime

TRADES_FILE = "data/trades.json"
RECAPS_FILE = "data/trade_recaps.json"

# === Ensure Recaps File Exists ===
def ensure_recaps_file():
    if not os.path.exists(RECAPS_FILE):
        with open(RECAPS_FILE, "w") as f:
            json.dump({"recaps": []}, f, indent=2)

# === Generate Recap from Trade ===
def generate_trade_recap(trade):
    if not trade:
        return {"error": "No trade data provided."}

    outcome = trade.get("outcome", "neutral").lower()
    symbol = trade.get("symbol", "UNKNOWN")
    profit = trade.get("profit", 0)
    strategy = trade.get("strategy", "unknown strategy")

    if outcome == "win":
        summary = f"Great job! You made ${profit:.2f} using the {strategy} on {symbol}."
    elif outcome == "loss":
        summary = f"Tough trade. You lost ${abs(profit):.2f} using the {strategy} on {symbol}."
    else:
        summary = f"You closed a neutral trade on {symbol} with the {strategy} strategy."

    return {
        "symbol": symbol,
        "strategy": strategy,
        "summary": summary,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

# === Save Recap ===
def save_recap(recap):
    ensure_recaps_file()
    with open(RECAPS_FILE, "r") as f:
        data = json.load(f)
    data["recaps"].append(recap)
    with open(RECAPS_FILE, "w") as f:
        json.dump(data, f, indent=2)

# === Generate Recap from Last Trade ===
def generate_recap_from_last_trade():
    if not os.path.exists(TRADES_FILE):
        return {"error": "No trade history found."}
    with open(TRADES_FILE, "r") as f:
        trades = json.load(f).get("trades", [])
    if not trades:
        return {"error": "No trades available."}
    last_trade = trades[-1]
    recap = generate_trade_recap(last_trade)
    save_recap(recap)
    return recap

# === Debug Run ===
if __name__ == "__main__":
    result = generate_recap_from_last_trade()
    print("Trade Recap:", result)

def log_event():ef drop_files_to_bridge():