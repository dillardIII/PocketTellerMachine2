from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a Python code for a trading strategy. This strategy is called Moving Average Crossover, which is commonly used in trading. It generates a buy signal when the short-term moving average crosses above the long-term moving average, and a sell signal when the short-term moving average crosses below the long-term moving average.

Please note that this is a simplified example and real-world trading involves many other factors.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving average
    sma_short = calculate_sma(data, short_window)
    sma_long = calculate_sma(data, long_window)

    # Create a 'signals' DataFrame with the signal information
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Generate trading signals (buy=1, sell=-1)
    signals['signal'][short_window:] = np.where(sma_short[short_window:] > sma_long[short_window:], 1.0, -1.0)

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Fetch the data
data = web.DataReader('AAPL', data_source='yahoo', start='01-01-2020', end='01-01-2022')['Close']

# Define the short and long window
short_window = 40
long_window = 100

# Generate the trading signals
signals = trading_strategy(data, short_window, long_window)

print(signals)
```

This code fetches the historical closing prices of Apple Inc. (AAPL) from Yahoo Finance, calculates the short and long window simple moving averages, generates trading signals and orders based on the moving average crossover strategy, and prints the signals.

Please replace 'AAPL' with the ticker symbol of the stock you're interested in, and adjust the start and end dates, short window, and long window as needed.