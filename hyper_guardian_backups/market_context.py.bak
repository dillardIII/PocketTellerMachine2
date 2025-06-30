# === FILE: market_context.py ===

def detect_market_context(rsi, sma, price):
    """
    Determine market context using RSI and price relative to SMA.

    Returns:
        'bullish', 'bearish', or 'sideways'
    """
    if rsi >= 65 and price > sma:
        return "bullish"
    elif rsi <= 35 and price < sma:
        return "bearish"
    else:
        return "sideways"