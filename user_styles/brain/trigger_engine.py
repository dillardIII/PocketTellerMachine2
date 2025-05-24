# trigger_engine.py
"""
Module to check whether a trade alert condition is met.
"""

def check_trade_trigger(data):
    """
    Checks if a trade price condition has been triggered.

    Example input:
    {
        "symbol": "NFLX",
        "price": 500,
        "target": 510,
        "condition": "above"
    }
    """
    price = data.get("price")
    target = data.get("target")
    condition = data.get("condition", "").lower()
    symbol = data.get("symbol", "UNKNOWN")

    if price is None or target is None:
        return {"error": "Missing price or target"}

    triggered = False

    if condition == "above":
        triggered = price > target
    elif condition == "below":
        triggered = price < target
    elif condition == "equal":
        triggered = price == target
    else:
        return {"error": f"Unsupported condition: {condition}"}

    return {
        "symbol": symbol,
        "condition": condition,
        "price": price,
        "target": target,
        "triggered": triggered
    }