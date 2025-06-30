from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a trading strategy implemented in Python. For this example, I'll use a simple Moving Average Crossover strategy. This strategy is one of the most commonly used strategies in trading. It involves two moving averages, one short-term and one long-term. When the short-term moving average crosses above the long-term moving average, it indicates a buy signal. Conversely, when the short-term moving average crosses below the long-term moving average, it indicates a sell signal.

Here is a simple implementation of this strategy using Python and pandas:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Download historical data as dataframe
df = web.DataReader(stock, data_source='yahoo', start='01-01-2010')

# Create short simple moving average over the short window
df['short_mavg'] = df['Close'].rolling(window=20, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
df['long_mavg'] = df['Close'].rolling(window=100, min_periods=1, center=False).mean()

# Create signals
df['signal'] = np.where(df['short_mavg'] > df['long_mavg'], 1.0, 0.0)

# Generate trading orders
df['positions'] = df['signal'].diff()

# Print DataFrame
print(df)

# Plotting
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Price in $')
df['Close'].plot(ax=ax1, color='r', lw=2.)
df[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)
ax1.plot(df.loc[df.positions == 1.0].index, df.short_mavg[df.positions == 1.0], '^' , markersize=10, color='m')
ax1.plot(df.loc[df.positions == -1.0].index, df.short_mavg[df.positions == -1.0], 'v' , markersize=10, color='k')
plt.show()
```

This script will download historical data for Apple (AAPL) from Yahoo Finance, calculate the short-term and long-term moving averages, generate trading signals and plot the results.

Please note that this is a very basic trading strategy and is not guaranteed to be profitable. It's always recommended to thoroughly backtest any strategy before live trading. Also, this script does not take into account trading fees or slippage. 

Please replace 'AAPL' with the stock you want to test the strategy on and adjust the start date as needed.