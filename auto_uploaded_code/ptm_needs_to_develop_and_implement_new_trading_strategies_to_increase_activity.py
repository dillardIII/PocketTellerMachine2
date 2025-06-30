from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a Python code for a trading strategy. This is a basic moving average crossover strategy. 

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
    # Calculate the short and long window simple moving averages
    data['short_sma'] = calculate_sma(data['Adj Close'], short_window)
    data['long_sma'] = calculate_sma(data['Adj Close'], long_window)

    # Create a column 'Signal' such that if the short window SMA is greater than long window SMA then buy else sell
    data['Signal'] = 0.0  
    data['Signal'][short_window:] = np.where(data['short_sma'][short_window:] > data['long_sma'][short_window:], 1.0, 0.0)   

    # Generate trading orders using the 'Signal' column, if signal changes from 1 to 0 then sell, if changes from 0 to 1 then buy
    data['Position'] = data['Signal'].diff()

    return data

def plot_graph(data):
    # Plot the adjusted closing price, short window and long window simple moving averages
    plt.figure(figsize=(10,5))
    plt.plot(data['Adj Close'], label='Adj Close')
    plt.plot(data['short_sma'], label='Short Window SMA')
    plt.plot(data['long_sma'], label='Long Window SMA')
    plt.plot(data.loc[data.Position == 1.0].index, data.short_sma[data.Position == 1.0], '^', markersize=10, color='g', label='buy')
    plt.plot(data.loc[data.Position == -1.0].index, data.short_sma[data.Position == -1.0], 'v', markersize=10, color='r', label='sell')
    plt.title('PTM Trading Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()

# Fetch data
ticker = "AAPL"
data = web.DataReader(ticker, "yahoo", start="01-01-2019", end="31-12-2019")

# Define short and long windows
short_window = 40
long_window = 100

# Apply trading strategy
trading_data = trading_strategy(data, short_window, long_window)

# Plot trading strategy graph
plot_graph(trading_data)
```

This script fetches historical stock price data for Apple Inc. (AAPL) for the year 2019, calculates the short window (40 days) and long window (100 days) simple moving averages (SMA), and generates trading signals based on the crossover of these SMAs. It then plots the adjusted closing price, SMAs, and trading signals on a graph.

Please note that this is a very basic trading strategy and is not recommended for actual trading. It's always important to backtest any strategy before live trading. Also, this code does not take into account trading fees or market impact.