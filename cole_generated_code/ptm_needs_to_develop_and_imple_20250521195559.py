from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a Python code for a basic trading strategy. This strategy is based on moving averages. When the short-term average crosses the long-term average, it could be a signal to buy or sell.

Please note that this is a very basic strategy and real-world trading strategies can be much more complex and need to take into account many other factors.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the ticker list
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

# Fetch the data
data = pdr.get_data_yahoo(tickers_list, start="2017-01-01", end="2021-12-31")['Adj Close']

# Print first 5 rows of the data
print(data.head())

# Calculate the short-term simple moving average (SMA)
short_rolling = data.rolling(window=20).mean()

# Calculate the long-term SMA
long_rolling = data.rolling(window=100).mean()

# Create signals
signals = pd.DataFrame(index=data.index)
signals['signal'] = 0.0

# Create signal when short SMA is above long SMA
signals['signal'][short_rolling['AAPL'] > long_rolling['AAPL']] = 1.0

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print the signals
print(signals)
```

This code fetches the historical price data for a list of tickers using Yahoo Finance, calculates the short-term and long-term simple moving averages, generates trading signals based on these moving averages, and generates trading orders based on these signals.

Please remember that this is a very basic trading strategy and should not be used for real trading without further improvements and testing.