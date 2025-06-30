# === strategy_executor.py ===

import random
from datetime import datetime

# Dummy trade runner
def run_trade_with_strategy(task):
    print(f"[Strategy Runner] Running strategy for {task.get('symbol', 'UNKNOWN')}")
    return {
        "symbol": task.get("symbol", "UNKNOWN"),
        "timestamp": datetime.utcnow().isoformat(),
        "result": random.uniform(-50, 150)  # Simulated gain/loss
    }

# Grade the trade outcome
def analyze_trade_result(trade_result):
    result = trade_result.get("result", 0)
    if result >= 100:
        return "A"
    elif result >= 50:
        return "B"
    elif result >= 0:
        return "C"
    else:
        return "F"

# Log the trade to the GhostBrain memory
def log_trade_outcome(task, result, grade):
    print(f"[Logger] {task.get('symbol')} | Result: {result['result']} | Grade: {grade}")
    log = {
        "id": f"trade_{datetime.utcnow().timestamp()}",
        "symbol": result["symbol"],
        "result": result["result"],
        "grade": grade,
        "timestamp": result["timestamp"]
    }

    try:
        import os, json
        os.makedirs("ghost_brain", exist_ok=True)
        log_path = "ghost_brain/trade_log.json"
        if os.path.exists(log_path):
            with open(log_path, "r") as f:
                history = json.load(f)
        else:
            history = []

        history.append(log)
        with open(log_path, "w") as f:
            json.dump(history, f, indent=2)

    except Exception as e:
        print("[Logger ERROR]", e)