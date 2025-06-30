from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide you with a simple example of a trading strategy using Python. Here, I will use the Moving Average Crossover strategy which is a popular strategy used in algorithmic trading. This strategy is a good starting point to understand the basics of algorithmic trading.

Please note that this is a very basic example and real-world trading strategies involve much more complex calculations and risk management techniques.

```python
# Import necessary libraries
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt

# Fetch historical data
def fetch_data(stock, start, end):
    return pdr.get_data_yahoo(stock, start, end)

# Calculate moving averages
def calculate_moving_averages(df, short_window, long_window):
    signals = pd.DataFrame(index=df.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Long moving average
    signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   
    signals['positions'] = signals['signal'].diff()

    return signals

# Fetch data
data = fetch_data('AAPL', '2017-01-01', '2022-12-31')

# Calculate moving averages
signals = calculate_moving_averages(data, 100, 200)

# Plotting
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Price in $')
data['Close'].plot(ax=ax1, color='r', lw=2.)
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='m')

# Plot sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='k')

plt.show()
```

This script fetches historical data for Apple Inc. (AAPL) and calculates two moving averages: a short-term (100 days) and a long-term (200 days). When the short-term average is above the long-term average, it generates a buy signal, and when it's below, it generates a sell signal. These signals are then plotted on a graph.

Please note that you need to install pandas, pandas_datareader, numpy and matplotlib libraries to run this script. Also, this is a very basic trading strategy and it doesn't take into account transaction costs, slippage, risk management, etc. Always remember to backtest your strategies before live trading.