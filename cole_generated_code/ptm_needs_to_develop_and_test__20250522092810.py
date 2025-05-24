Sure, here's a simple example of a trading strategy in Python using the pandas library. This strategy is called the Moving Average Crossover Strategy. It's a very basic strategy often used for illustrative purposes.

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

# Fetch data
ticker = 'AAPL'
data = web.DataReader(ticker, 'yahoo', start='01-01-2015', end='31-12-2020')

# Implement the strategy
short_window = 40
long_window = 100
data = trading_strategy(data, short_window, long_window)

# Plot the data
plt.figure(figsize=(10,5))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['short_sma'], label='40-days SMA', color='red')
plt.plot(data['long_sma'], label='100-days SMA', color='green')
plt.plot(data.loc[data.positions == 1.0].index, 
         data.short_sma[data.positions == 1.0],
         '^', markersize=10, color='m')
plt.plot(data.loc[data.positions == -1.0].index, 
         data.short_sma[data.positions == -1.0],
         'v', markersize=10, color='k')
plt.title('AAPL Moving Average Crossover Trading Signals')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()
```

In this strategy, we calculate two moving averages: a short-term (40 days) and a long-term (100 days). When the short-term average crosses above the long-term average, it generates a buy signal (denoted by a magenta up-arrow in the plot). When the short-term average crosses below the long-term average, it generates a sell signal (denoted by a black down-arrow in the plot).

Please note that this is a very basic strategy and might not be profitable in real trading. It's recommended to use more sophisticated strategies and consider transaction costs, slippage, etc. in real trading.