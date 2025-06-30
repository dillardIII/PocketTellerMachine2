# === FILE: trading_engine.py ===

import datetime
import json
import os
from cole_logger import log_info

TRADE_LOG_FILE = "data/executed_trades.json"

# === Execute Trade Logic ===
def execute_trade(strategy):
    """
    Simulates trade execution using the given strategy.
    Logs execution result with timestamp.
    """
    try:
        trade_record = {
            "timestamp": str(datetime.datetime.now()),
            "strategy": strategy,
            "status": "executed",
            "notes": "Simulated execution - replace with live API logic."
        }

        # Load previous logs
        if os.path.exists(TRADE_LOG_FILE):
            with open(TRADE_LOG_FILE, "r") as f:
                trades = json.load(f)
        else:
            trades = []

        # Save new log
        trades.append(trade_record)
        os.makedirs("data", exist_ok=True)
        with open(TRADE_LOG_FILE, "w") as f:
            json.dump(trades[-500:], f, indent=2)

        log_info(f"[Trading Engine] ✅ Executed: {strategy.get('strategy', 'Unknown')}")
        return trade_record

    except Exception as e:
        log_info(f"[Trading Engine] ❌ Trade execution failed: {e}")
        return {
            "status": "fail",
            "reason": str(e)
        }