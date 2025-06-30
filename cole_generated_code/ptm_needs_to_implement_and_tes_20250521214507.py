from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that implements a basic trading strategy using moving averages. This strategy is known as the Moving Average Crossover Strategy. It's a simple strategy where you buy when the short term moving average crosses above the long term moving average and sell when the short term moving average crosses below the long term moving average.

Please note that this is a very basic strategy and may not be profitable in real trading. It's just an example to show how to implement a trading strategy in Python.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window).mean()
    return ema

def implement_strategy(data, short_window, long_window):
    # Calculate the short and long term moving averages
    sma_short = calculate_sma(data, short_window)
    sma_long = calculate_sma(data, long_window)
    
    # Create a 'signals' DataFrame with the signal information
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    signals['short_mavg'] = sma_short
    signals['long_mavg'] = sma_long
    
    # Generate signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)
    
    # Generate trading orders
    signals['positions'] = signals['signal'].diff()
    
    return signals

# Get the data
start_date = '2010-01-01'
end_date = '2020-12-31'
data = web.get_data_yahoo('AAPL', start_date, end_date)['Adj Close']

# Implement the strategy
short_window = 40
long_window = 100
signals = implement_strategy(data, short_window, long_window)

# Plot the data and the strategy
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Price in $')
data.plot(ax=ax1, color='r', lw=2.)
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)
ax1.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0], '^', markersize=10, color='m')
ax1.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0], 'v', markersize=10, color='k')
plt.show()
```

This code fetches the historical data for Apple Inc. from Yahoo Finance, calculates the short term (40 days) and long term (100 days) simple moving averages, generates trading signals and plots the data and the strategy. The green triangles represent the buy signals and the red triangles represent the sell signals.