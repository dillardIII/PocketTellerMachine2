from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide you with a simple example of a trading strategy implemented in Python. This strategy will be a simple Moving Average Crossover strategy. 

Please note that this is a very basic strategy and in real-world trading, strategies can get very complex involving multiple factors and sophisticated algorithms.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Fetching the historical data
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2022-12-31")

# Calculating the short-window simple moving average
short_rolling = df['Close'].rolling(window=20).mean()

# Calculating the long-window simple moving average
long_rolling = df['Close'].rolling(window=100).mean()

# Creating signals
signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0
signals['short_mavg'] = short_rolling
signals['long_mavg'] = long_rolling

# Generate trading orders
signals['signal'][short_rolling > long_rolling] = 1.0

# Calculate daily portfolio value
signals['positions'] = signals['signal'].diff()

# Plotting
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Price in $')
df['Close'].plot(ax=ax1, color='r', lw=2.)
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plotting the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='m')

# Plotting the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='k')

plt.show()
```

This script fetches historical data for Apple Inc. (AAPL) and calculates two moving averages: a short one (20 days) and a long one (100 days). When the short moving average is above the long one, it generates a buy signal, and when it's below, it generates a sell signal. The script also plots the price and moving averages, with buy signals marked by up arrows and sell signals marked by down arrows.

Please note that this script requires the `pandas_datareader`, `yfinance`, `pandas`, `numpy` and `matplotlib` libraries. If you don't have them installed, you can do so with `pip install pandas_datareader yfinance pandas numpy matplotlib`.

Also, remember that this is a very basic strategy and should not be used for real trading without further enhancements.