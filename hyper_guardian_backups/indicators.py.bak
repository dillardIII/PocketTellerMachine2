import numpy as np
import pandas as pd  # Required for MACD logic using ewm

# === Simple Moving Average (SMA) ===
def calc_sma(prices, window=14):
    if len(prices) < window:
        return np.mean(prices) if prices else 0
    return np.mean(prices[-window:])

# === Relative Strength Index (RSI) ===
def calc_rsi(prices, window=14):
    if len(prices) < window + 1:
        return 50  # Neutral RSI
    diffs = np.diff(prices[-(window + 1):])
    gains = np.where(diffs > 0, diffs, 0)
    losses = np.where(diffs < 0, -diffs, 0)
    avg_gain = np.mean(gains)
    avg_loss = np.mean(losses)
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

# === Exponential Moving Average (EMA) ===
def calc_ema(prices, window=14):
    if not prices or len(prices) < window:
        return np.mean(prices)
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    a = np.convolve(prices, weights, mode='full')[:len(prices)]
    return a[-1]

# === MACD (Moving Average Convergence Divergence) ===
def calc_macd(prices, short_period=12, long_period=26, signal_period=9):
    prices = pd.Series(prices)

    # Exponential moving averages
    short_ema = prices.ewm(span=short_period, adjust=False).mean()
    long_ema = prices.ewm(span=long_period, adjust=False).mean()

    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    macd_histogram = macd_line - signal_line

    return macd_line.iloc[-1], signal_line.iloc[-1], macd_histogram.iloc[-1]

# === Bollinger Bands ===
def calc_bollinger_bands(prices, period=20, num_std=2):
    prices = np.array(prices)

    if len(prices) < period:
        return None, None  # Not enough data

    # Simple Moving Average
    sma = np.mean(prices[-period:])
    std_dev = np.std(prices[-period:])

    upper_band = sma + num_std * std_dev
    lower_band = sma - num_std * std_dev

    return lower_band, upper_band