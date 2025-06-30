from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is one of the most commonly used strategies in trading. It involves two moving averages, one short-term and one long-term. When the short-term moving average crosses above the long-term moving average, it's a signal to buy. When it crosses below, it's a signal to sell.

Please note that this is a very simplified version of a trading strategy and in real-world scenarios, trading strategies can get very complex involving multiple indicators and parameters.

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
    # Calculate the short and long-term moving averages
    data['short_mavg'] = calculate_sma(data['Close'], short_window)
    data['long_mavg'] = calculate_sma(data['Close'], long_window)

    # Create a column 'Signal' such that if the short-term moving average is greater than the long-term moving average, 
    # then set 'Signal' as 1 else 0
    data['Signal'] = np.where(data['short_mavg'] > data['long_mavg'], 1.0, 0.0)

    # Create a column 'Position' which is the difference of the 'Signal' column and its previous row
    data['Position'] = data['Signal'].diff()

    return data

# Get the stock data
stock_data = web.get_data_yahoo('AAPL', start='01-01-2020', end='31-12-2020')

# Implement the trading strategy
trading_data = trading_strategy(stock_data, 50, 200)

# Plot the data
plt.figure(figsize=(10,5))
plt.plot(trading_data['Close'], label='Close Price', color='blue')
plt.plot(trading_data['short_mavg'], label='50 Day SMA', color='red')
plt.plot(trading_data['long_mavg'], label='200 Day SMA', color='green')
plt.scatter(trading_data.index, trading_data['Position'], color='black')  # Plot the buy/sell signals
plt.legend()
plt.show()
```

This code will plot the close price, short-term moving average, long-term moving average and the buy/sell signals for the given stock (in this case, Apple Inc.) for the year 2020. 

Please note that you need to install `pandas_datareader`, `matplotlib`, `numpy` and `pandas` Python packages to run this code. Also, this is a very basic strategy and should not be used for actual trading without proper backtesting and strategy optimization.