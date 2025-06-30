from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is one of the most commonly used strategies in trading. It involves two moving averages, one short term and one long term. When the short term moving average crosses above the long term moving average, it's a signal to buy. Conversely, when the short term moving average crosses below the long term moving average, it's a signal to sell.

Please note that this is a very basic strategy and real trading strategies can be much more complex.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long term moving averages
    data['short_mavg'] = calculate_sma(data['Close'], short_window)
    data['long_mavg'] = calculate_sma(data['Close'], long_window)

    # Create a column 'Signal' such that if the short term moving average is greater than the long term moving average
    # then set 'Signal' as 1 else 0
    data['Signal'] = np.where(data['short_mavg'] > data['long_mavg'], 1.0, 0.0)

    # Create a column 'Position' which is the difference of the 'Signal' column and its previous value
    data['Position'] = data['Signal'].diff()

    return data

# Fetch the data
data = pdr.get_data_yahoo('AAPL', '2010-01-01', '2020-12-31')

# Implement the trading strategy
trading_data = trading_strategy(data, 50, 200)

# Plot the data
plt.figure(figsize=(10,5))
plt.plot(trading_data['Close'], label='Close Price', color='blue')
plt.plot(trading_data['short_mavg'], label='50 Day SMA', color='red')
plt.plot(trading_data['long_mavg'], label='200 Day SMA', color='green')
plt.title('Apple Close Prices & Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
```

This code fetches historical data for Apple Inc. from Yahoo Finance, calculates the short term (50 days) and long term (200 days) simple moving averages, and then generates trading signals based on these moving averages. It then plots the close prices and the moving averages.

Please note that this code requires `pandas`, `numpy`, `matplotlib`, and `pandas_datareader` to be installed in your Python environment. Also, this is a very basic trading strategy and should not be used for actual trading without proper backtesting and risk management.