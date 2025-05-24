Sure, here's a simple example of a trading strategy using Python. This strategy is based on moving average crossover, which is a common trading strategy. We'll use the pandas library to handle our data and matplotlib to visualize our data and trading strategy.

Please note that this is a basic example and real trading strategies involve much more factors and complex algorithms.

```python
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', '^GSPC']

# Define which online source one should use
data_source = 'yahoo'

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2000-01-01'
end_date = '2016-12-31'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = web.DataReader(tickers, data_source, start_date, end_date)

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
# The index in this DataFrame is the major index of the panel_data.
close = panel_data['Adj Close']

# Getting all weekdays between 01/01/2000 and 12/31/2016
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# How do we align the existing prices in adj_close with our new set of dates?
# All we need to do is reindex close using all_weekdays as the new index
close = close.reindex(all_weekdays)

# Reindexing will insert missing values (NaN) for the dates that were not present
# in the original set. To cope with this, we can fill the missing by replacing them
# with the latest available price for each instrument.
close = close.fillna(method='ffill')

# Calculate the short and long moving averages
short_rolling = close.rolling(window=20).mean()
long_rolling = close.rolling(window=100).mean()

# Plot everything by leveraging the very powerful matplotlib package
fig, ax = plt.subplots(figsize=(16,9))

ax.plot(close.index, close, label='Adjusted closing price')
ax.plot(short_rolling.index, short_rolling, label='20 days rolling')
ax.plot(long_rolling.index, long_rolling, label='100 days rolling')

ax.set_xlabel('Date')
ax.set_ylabel('Adjusted closing price ($)')
ax.legend()

plt.show()
```

In this code, we are downloading the historical price data for Apple, Microsoft, and the S&P500 index from Yahoo Finance. We then calculate the 20-day (short-term) and 100-day (long-term) moving averages for these prices. When the short-term average crosses above the long-term average, it could be a signal to buy, and when it crosses below, it could be a signal to sell.