Sure, here is a simple implementation of a moving average crossover strategy using Python. This strategy is one of the most common systematic trading strategies that uses two moving averages, one short and one long. When the short moving average crosses above the long moving average, it could be a buy signal, and when it crosses below, it could be a sell signal.

```python
import pandas as pd
import numpy as np
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

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
close_data = panel_data['Adj Close']

# Calculate the short and long moving averages
short_rolling = close_data.rolling(window=20).mean()
long_rolling = close_data.rolling(window=100).mean()

# Create signals
signals = pd.DataFrame(index=close_data.index)
signals['signal'] = 0.0

# When short moving average is above long moving average, set signal to 1
signals['signal'][short_rolling > long_rolling] = 1.0

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print the DataFrame
print(signals)

# Plotting
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Price in $')
close_data['AAPL'].plot(ax=ax1, color='r', lw=2.)
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)
ax1.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='m')
ax1.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='k')
plt.show()
```

Please note that this is a simplified example and real-world trading involves many other factors like transaction costs, risk management, etc. Also, the historical performance of a strategy does not guarantee its future performance.