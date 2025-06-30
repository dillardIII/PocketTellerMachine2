from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a trading strategy using Python. For this example, I will use a simple moving average crossover strategy. This strategy buys when the short-term moving average crosses above the long-term moving average, and sells when the short-term moving average crosses below the long-term moving average.

Please note that this is a very basic strategy and should not be used for real trading without further enhancements and testing. Also, you need to install pandas_datareader and matplotlib libraries to run this code.

```python
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the instruments to download. We would like to see Apple, Microsoft and others.
tickers = ['AAPL', 'MSFT']

# Define which online source to use
data_source = 'yahoo'

# Define the start and end dates
start_date = '2015-01-01'
end_date = '2020-12-31'

# Use pandas_datareader.data.DataReader to load the desired data
panel_data = web.DataReader(tickers, data_source, start_date, end_date)

# Calculate the short-term simple moving average
short_rolling = panel_data['Close'].rolling(window=20).mean()

# Calculate the long-term simple moving average
long_rolling = panel_data['Close'].rolling(window=100).mean()

# Create a 'signals' DataFrame with the `signal` column
signals = pd.DataFrame(index=panel_data.index)
signals['signal'] = 0.0

# Create signals
signals['short_mavg'] = short_rolling
signals['long_mavg'] = long_rolling
signals['signal'][short_rolling > long_rolling] = 1.0

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Plot everything by leveraging the very powerful matplotlib package
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Price in $')

panel_data['Close'].plot(ax=ax1, color='r', lw=2.)
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='m')

# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='k')

plt.show()
```

This code will plot the closing prices of the stocks, the short-term and long-term moving averages, and the buy and sell signals.