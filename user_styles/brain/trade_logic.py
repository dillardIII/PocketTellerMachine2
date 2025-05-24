# trade_logic.py
"""
This module contains the logic to analyze trades for insights,
warnings, or tagging purposes.
"""

def analyze_trade(trade):
    """
    Analyzes a single trade and returns insights based on the result, size, or type.
    """
    result = trade.get("result", "").lower()
    size = trade.get("size", 0)
    symbol = trade.get("symbol", "Unknown")
    trade_type = trade.get("type", "Unknown")

    analysis = {
        "symbol": symbol,
        "type": trade_type,
        "result": result,
        "message": "",
        "risk_level": "Moderate"
    }

    # Determine outcome message
    if result == "win":
        analysis["message"] = f"Good trade on {symbol}!"
    elif result == "loss":
        analysis["message"] = f"Review your strategy for {symbol}."
    else:
        analysis["message"] = f"No clear result recorded for {symbol}."

    # Risk logic based on size
    if isinstance(size, (int, float)):
        if size > 10000:
            analysis["risk_level"] = "High"
        elif size < 1000:
            analysis["risk_level"] = "Low"
    else:
        analysis["risk_level"] = "Unknown"

    return analysis