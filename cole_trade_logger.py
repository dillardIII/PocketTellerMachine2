from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
import json
from datetime import datetime

TRADES_FILE = "data/trades.json"

# === Ensure file exists ===
def ensure_trade_file():
    if not os.path.exists(TRADES_FILE):
        with open(TRADES_FILE, "w") as f:
            json.dump({"trades": []}, f, indent=2)

# === Log a new trade ===
def log_trade(trade_data):
    ensure_trade_file()

    with open(TRADES_FILE, "r") as f:
        data = json.load(f)

    trade_entry = {
        "id": trade_data.get("id"),
        "symbol": trade_data.get("symbol"),
        "strategy": trade_data.get("strategy"),
        "entry_price": trade_data.get("entry_price"),
        "exit_price": trade_data.get("exit_price"),
        "profit": trade_data.get("profit"),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "status": trade_data.get("status", "closed"),
        "outcome": trade_data.get("outcome", "win"),
        "comments": trade_data.get("comments", ""),
    }

    data["trades"].append(trade_entry)

    with open(TRADES_FILE, "w") as f:
        json.dump(data, f, indent=2)

# === Load all trades ===
def load_all_trades():
    ensure_trade_file()
    with open(TRADES_FILE, "r") as f:
        return json.load(f).get("trades", [])

# === Debug Preview ===
if __name__ == "__main__":
    sample = {
        "id": "T-001",
        "symbol": "AAPL",
        "strategy": "Covered Call",
        "entry_price": 180,
        "exit_price": 185,
        "profit": 5,
        "status": "closed",
        "outcome": "win",
        "comments": "Nice premium collected."
    }
    log_trade(sample)
    print("Trades:", load_all_trades())

def log_event():ef drop_files_to_bridge():