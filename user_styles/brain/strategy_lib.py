from ghost_env import INFURA_KEY, VAULT_ADDRESS
# strategy_lib.py
"""
Module to evaluate a trading strategy using basic logic.
"""

def evaluate_strategy(data):
    """
    Evaluates a basic trade outcome based on strategy rules.
    Example input:
    {
        "strategy": "covered_call",
        "symbol": "TSLA",
        "entry_price": 180,
        "exit_price": 200
    }
    """
    strategy = data.get("strategy", "unknown")
    entry = data.get("entry_price")
    exit = data.get("exit_price")
    symbol = data.get("symbol", "UNKNOWN")

    if entry is None or exit is None:
        return {"error": "Missing price values"}

    profit = round(exit - entry, 2)
    status = "profitable" if profit > 0 else "loss" if profit < 0 else "neutral"

    return {
        "symbol": symbol,
        "strategy": strategy,
        "entry_price": entry,
        "exit_price": exit,
        "profit": profit,
        "outcome": status
    }