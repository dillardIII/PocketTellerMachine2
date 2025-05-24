Sure, here's a simple example of a Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is not a recommendation for real trading, it's just an example for educational purposes. 

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

def calculate_SMA(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_EMA(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def implement_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving averages
    data['short_SMA'] = calculate_SMA(data['Close'], short_window)
    data['long_SMA'] = calculate_SMA(data['Close'], long_window)

    # Create signals based on the crossover of the short and long SMA
    data['signal'] = 0.0  
    data['signal'][short_window:] = np.where(data['short_SMA'][short_window:] > data['long_SMA'][short_window:], 1.0, 0.0)

    # Generate trading orders based on the signals
    data['positions'] = data['signal'].diff()

    return data

# Get the data
data = web.DataReader('AAPL', data_source='yahoo', start='01-01-2010', end='01-01-2022')

# Implement the strategy
data = implement_strategy(data, 50, 200)

# Plot the data
plt.figure(figsize=(10,5))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['short_SMA'], label='50-Day SMA', color='red')
plt.plot(data['long_SMA'], label='200-Day SMA', color='green')
plt.plot(data.loc[data.positions == 1.0].index, data.short_SMA[data.positions == 1.0], '^', markersize=10, color='m')
plt.plot(data.loc[data.positions == -1.0].index, data.short_SMA[data.positions == -1.0], 'v', markersize=10, color='k')
plt.title('AAPL: Moving Average Crossover Trading Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()
```

This code implements a simple moving average crossover strategy where a long position is taken whenever the short-term average crosses above the long-term average, and a short position is taken when the short-term average crosses below the long-term average. The strategy is visualized on a plot.

Please note that this is a very basic trading strategy and doesn't take into account transaction costs, slippage, risk management, or other important factors for a real trading strategy. Always do thorough backtesting and risk assessment before implementing any trading strategy.