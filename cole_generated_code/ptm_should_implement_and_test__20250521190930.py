Sure, I can provide a simple Python code example of a trading strategy. This example will be a simple Moving Average Crossover strategy. This strategy is used to identify points on a chart where a short-term average crosses above or below a long-term average, signaling potential market trend shifts.

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
    data['short_sma'] = calculate_sma(data['Close'], short_window)
    data['long_sma'] = calculate_sma(data['Close'], long_window)
    
    # Create signals
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_sma'][short_window:] 
                                             > data['long_sma'][short_window:], 1.0, 0.0)
   
    # Generate trading orders
    data['positions'] = data['signal'].diff()
    
    return data

def plot_data(data, ticker):
    # Plot the closing price, short-term and long-term moving averages and the buy/sell signals
    fig = plt.figure()
    ax1 = fig.add_subplot(111, ylabel='Price in $')
    data[['Close', 'short_sma', 'long_sma']].plot(ax=ax1, lw=2.)
    ax1.plot(data.loc[data.positions == 1.0].index, 
             data.short_sma[data.positions == 1.0],
             '^', markersize=10, color='m')
    ax1.plot(data.loc[data.positions == -1.0].index, 
             data.short_sma[data.positions == -1.0],
             'v', markersize=10, color='k')
    plt.title(f'{ticker} Moving Average Crossover Trading Strategy')
    plt.show()

# Define the ticker list
tickers_list = ['AAPL']

# Fetch the data
data = web.get_data_yahoo(tickers_list[0], start="2020-01-01", end="2022-12-31")

# Use the trading strategy
data = trading_strategy(data, 50, 200)

# Plot the data
plot_data(data, tickers_list[0])
```

This script fetches historical data for a given ticker (in this case, AAPL), calculates the short-term and long-term simple moving averages, generates trading signals and positions based on the crossover strategy, and plots the closing price, moving averages and trading signals.

Please note that this is a very simple trading strategy and is not guaranteed to be profitable. It's important to thoroughly backtest any strategy before live trading. Also, this script does not take into account trading fees or slippage.