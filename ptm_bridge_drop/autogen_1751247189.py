from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here's a Python script for a simple trading strategy that uses a combination of the Relative Strength Index (RSI) and the Moving Average Convergence Divergence (MACD) indicators to make buy and sell decisions. This strategy will generate buy signals when the RSI is below a certain threshold and the MACD line crosses above the signal line. It will generate sell signals when the RSI is above a certain threshold and the MACD line crosses below the signal line.

```python
import pandas as pd
import numpy as np

def calculate_rsi(prices, window=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(prices, short_window=12, long_window=26, signal_window=9):
    short_ema = prices.ewm(span=short_window, adjust=False).mean()
    long_ema = prices.ewm(span=long_window, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=signal_window, adjust=False).mean()
    histogram = macd - signal
    return macd, signal, histogram

def generate_trade_signals(prices, rsi_thresholds=(30, 70)):
    rsi = calculate_rsi(prices)
    macd, signal, _ = calculate_macd(prices)

    buy_signals = []
    sell_signals = []

    for i in range(1, len(prices)):
        if rsi[i] < rsi_thresholds[0] and macd[i] > signal[i] and macd[i - 1] <= signal[i - 1]:
            buy_signals.append(prices.index[i])
        elif rsi[i] > rsi_thresholds[1] and macd[i] < signal[i] and macd[i - 1] >= signal[i - 1]:
            sell_signals.append(prices.index[i])

    return buy_signals, sell_signals

def execute_trading_strategy(prices, rsi_thresholds=(30, 70)):
    buy_signals, sell_signals = generate_trade_signals(prices, rsi_thresholds)
    
    print("Buy signals generated at:")
    for buy in buy_signals:
        print(buy)
    
    print("\nSell signals generated at:")
    for sell in sell_signals:
        print(sell)

# Example Usage - This should be replaced with actual historical data
if __name__ == "__main__":
    # Sample data loading
    dates = pd.date_range('2023-01-01', '2023-02-01')
    prices = pd.Series(np.random.normal(100, 1, len(dates)), index=dates)

    # Execute the strategy
    execute_trading_strategy(prices)
```

Save this script to a file, for example, `trading_strategy_5.py`, and run it with your historical price data to receive buy and sell signals based on the defined logic. Replace the example price data with actual historical pricing when using it for real-world application. Adjust the RSI thresholds and the MACD/EMA windows as necessary depending on the characteristics of the market you are trading in.