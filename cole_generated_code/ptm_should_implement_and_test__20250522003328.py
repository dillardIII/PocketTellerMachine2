To implement and test new trading strategies, we can create a simple Python script that uses a basic strategy such as Moving Average Crossover. This strategy is simple and widely used in trading. It involves two moving averages, one short and one long. When the short moving average crosses above the long moving average, it's a signal to buy. When it crosses below, it's a signal to sell.

Here's a simple Python script that uses pandas to implement this strategy:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the instruments to download. We would like to see Apple, Microsoft and others.
tickers = ['AAPL', 'MSFT', 'GOOG', 'IBM', 'AMZN']

# Define which online source to use
data_source = 'yahoo'

# Define the start and end dates
start_date = '2016-01-01'
end_date = '2021-12-31'

# Use pandas_datareader.data.DataReader to load the desired data
panel_data = web.DataReader(tickers, data_source, start_date, end_date)

# Getting just the adjusted closing prices
adj_close = panel_data['Adj Close']

# Calculate the short and long moving averages
short_rolling = adj_close.rolling(window=20).mean()
long_rolling = adj_close.rolling(window=100).mean()

# Create signals
signals = pd.DataFrame(index=adj_close.index)
signals['signal'] = 0.0

# When short moving average is above long moving average, set signal to 1 (buy)
signals['signal'][short_rolling > long_rolling] = 1.0

# When short moving average is below long moving average, set signal to -1 (sell)
signals['signal'][short_rolling < long_rolling] = -1.0

# Print the signals
print(signals)

# Plotting
fig, ax = plt.subplots(figsize=(16,9))

ax.plot(adj_close.index, adj_close, label='Adj Close')
ax.plot(short_rolling.index, short_rolling, label='20 days rolling')
ax.plot(long_rolling.index, long_rolling, label='100 days rolling')

ax.legend(loc='best')
ax.set_ylabel('Price in $')
plt.show()
```

This script downloads historical data for several stocks, calculates their short and long moving averages, and generates buy and sell signals based on these averages. It also plots the prices and moving averages for visualization.

Please note that this is a very basic strategy and may not be profitable in real trading. It's recommended to use more sophisticated strategies and risk management techniques in actual trading. Also, this script assumes that the data is available and clean, which may not always be the case in real-world scenarios.