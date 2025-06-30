from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I'll provide a simple example of a Python code implementing a basic trading strategy using Moving Average Crossover. This strategy is used to identify buying and selling opportunities based on the position of the short-term moving average in relation to the long-term moving average.

Please note that this is a basic strategy and may not necessarily increase the number of trades. The number of trades depends on the market conditions and the specific parameters of the strategy. 

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Fetching the data
def fetch_data(stock, start, end):
    df = web.DataReader(stock, 'yahoo', start, end)
    return df

# Calculating Moving Average
def calculate_MA(df, short_window, long_window):
    signals = pd.DataFrame(index=df.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Long moving average
    signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Fetching the data
df = fetch_data('AAPL', '01-01-2010', '01-01-2022')

# Calculating short window and long window moving average
signals = calculate_MA(df, 40, 100)

# Plotting the data
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

In this code, we fetch the data from Yahoo Finance for the AAPL stock. We then calculate the short-term and long-term moving averages and generate signals based on the crossover of these averages. When the short-term average is above the long-term average, it's a buy signal and when it's below, it's a sell signal. These signals are then plotted on the graph.