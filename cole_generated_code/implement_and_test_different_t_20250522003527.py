Sure, I can provide you with a simple example of how to implement and test different trading strategies using Python. For this example, let's use two strategies: a simple moving average crossover strategy and a buy and hold strategy.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', '^GSPC']

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2000-01-01'
end_date = '2016-12-31'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = pdr.get_data_yahoo(tickers, start_date, end_date)

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


# Define the number of days for moving average
window = 50

# Calculate the moving average
sma = close.rolling(window=window).mean()

# Define a signal threshold
threshold = 5

# Generate trading signals based on the moving average crossover
signals = np.where(close > sma + threshold, 1, 0)

# Calculate the daily returns of the stocks
returns = close.pct_change()

# Define the strategy
strategy_returns = returns * signals

# Calculate the cumulative returns
cumulative_returns = (1 + strategy_returns).cumprod()

# Plot the cumulative returns
plt.figure(figsize=(12,8))
plt.plot(cumulative_returns)
plt.title('Cumulative Returns of Trading Strategy')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()

# Buy and hold strategy
buy_and_hold_returns = (1 + returns).cumprod()

# Plot the cumulative returns of buy and hold strategy
plt.figure(figsize=(12,8))
plt.plot(buy_and_hold_returns)
plt.title('Cumulative Returns of Buy and Hold Strategy')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()
```

Please note that this is a simple example and real trading strategies involve much more considerations and complex calculations. Also, it's important to remember that past performance is not indicative of future results.