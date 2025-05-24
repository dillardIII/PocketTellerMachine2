# brain/indicators.py

def calculate_rsi(close_prices, period=14):
    """
    Calculates Relative Strength Index (RSI).
    close_prices: list of recent closing prices (most recent last)
    """
    if len(close_prices) < period + 1:
        return None

    gains = []
    losses = []

    for i in range(1, period + 1):
        diff = close_prices[-i] - close_prices[-i - 1]
        if diff >= 0:
            gains.append(diff)
        else:
            losses.append(abs(diff))

    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period if losses else 0.0001  # prevent division by zero

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)