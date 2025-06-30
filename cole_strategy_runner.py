from ghost_env import INFURA_KEY, VAULT_ADDRESS
# === FILE: cole_strategy_runner.py ===

import datetime
import json
import os
from strategy_scorer import recommend_best_strategy
from cole_executor import run_trade_with_strategy, analyze_trade_result, log_trade_outcome
from cole_brain import log_strategy_reason
from voice_recap_engine import recap_trade  # Optional voice recap (if enabled):
:
TRADE_LOG_FILE = "data/trade_history.json"

def execute_best_strategy():
    strategy_info = recommend_best_strategy()

    strategy = strategy_info.get("strategy")
    reason = strategy_info.get("reason", "No reason provided.")

    if not strategy:
        print("[Strategy Runner] No strategy available.")
        return

    log_strategy_reason(strategy, reason)  # ✅ Fix: Pass both arguments
    print(f"[Strategy Runner] Executing strategy: {strategy}")

    # === Simulate trade ===
    result = run_trade_with_strategy(strategy)
    analysis = analyze_trade_result(result)

    trade_log = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "strategy": strategy,
        "result": result,
        "grade": analysis.get("grade", "N/A"),
        "symbol": analysis.get("symbol", "AAPL")
    }

    log_trade_outcome(trade_log)
    _save_to_history(trade_log)

    recap_trade(trade_log)  # Optional: voice recap

    print(f"[Strategy Runner] Trade completed and logged.")
    return trade_log

def _save_to_history(entry):
    os.makedirs("data", exist_ok=True)
    if os.path.exists(TRADE_LOG_FILE):
        with open(TRADE_LOG_FILE, "r") as f:
            try:
                history = json.load(f)
            except:
                history = []
    else:
        history = []

    history.append(entry)

    with open(TRADE_LOG_FILE, "w") as f:
        json.dump(history[-500:], f, indent=2)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():