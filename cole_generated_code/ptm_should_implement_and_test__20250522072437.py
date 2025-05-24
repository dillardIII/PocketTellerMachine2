Sure, here is a simple example of a Python code implementing a basic trading strategy using Moving Average Crossover. Please note that you need to install pandas_datareader and matplotlib libraries to run this code. 

```python
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window).mean()
    return ema

def implement_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving averages
    data['short_sma'] = calculate_sma(data['Close'], short_window)
    data['long_sma'] = calculate_sma(data['Close'], long_window)

    # Create signals based on the crossover of the short and long sma
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_sma'][short_window:] > data['long_sma'][short_window:], 1.0, 0.0)

    # Generate trading orders based on the signals
    data['positions'] = data['signal'].diff()

    return data

# Fetch data
data = web.DataReader('AAPL', 'yahoo', start='01/01/2020', end='01/01/2022')

# Implement the strategy
short_window = 40
long_window = 100
data = implement_strategy(data, short_window, long_window)

# Plot the data
plt.figure(figsize=(10,5))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['short_sma'], label='40-days SMA', color='red')
plt.plot(data['long_sma'], label='100-days SMA', color='green')
plt.plot(data.loc[data.positions == 1.0].index, data.short_sma[data.positions == 1.0], '^', markersize=10, color='m')
plt.plot(data.loc[data.positions == -1.0].index, data.short_sma[data.positions == -1.0], 'v', markersize=10, color='k')
plt.title('Apple Inc. - Moving Average Crossover')
plt.legend()
plt.grid()
plt.show()
```

This code fetches historical data for Apple Inc. from Yahoo Finance, calculates the 40-day and 100-day simple moving averages, generates trading signals based on the crossover of these moving averages, and plots the results. The magenta and black markers represent the buy and sell signals respectively.

Please note that this is a simple strategy and may not be profitable in real trading. Always backtest your strategies before live trading.