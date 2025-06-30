from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a trading strategy using Python. In this example, we will use a simple moving average crossover strategy. This strategy is based on the idea that if the short term moving average crosses the long term moving average, it may be a signal of future price movement.

Please note that this is a very basic strategy and in real trading scenarios, strategies can get very complex involving many more factors.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long term moving averages
    short_moving_avg = calculate_sma(data, short_window)
    long_moving_avg = calculate_sma(data, long_window)

    # Create a 'signal' (invested or not invested) when the short moving average crosses the long moving average
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(short_moving_avg[short_window:] > long_moving_avg[short_window:], 1.0, 0.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

    return data

# Fetch the data
start_date = '2010-01-01'
end_date = '2020-12-31'
data = web.DataReader('AAPL', 'yahoo', start_date, end_date)

# Implement the trading strategy
trading_data = trading_strategy(data['Close'], 50, 200)

# Plot the data
plt.figure(figsize=(10,5))
plt.plot(trading_data['Close'], label='Close Price', color='blue')
plt.plot(trading_data['signal'], label='Trading Signals', color='red')
plt.legend()
plt.show()
```

This script fetches historical data for Apple Inc. from Yahoo Finance, calculates the short and long term moving averages, generates trading signals and plots the data.

Remember, this is a simple example and doesn't take into account trading fees, slippage, and many other factors that could affect the performance of a trading strategy. Always backtest your strategy with historical data before live trading.