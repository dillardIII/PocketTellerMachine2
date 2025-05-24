Sure, here is a simple example of how you could analyze market trends using Python. This example uses the `pandas` library to handle data and the `yfinance` library to download stock price data from Yahoo Finance.

```python
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

# Use Yahoo Finance to get stock price data
yf.pdr_override()

# Define the ticker list
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

# Fetch the data
data = pdr.get_data_yahoo(tickers_list, start="2020-01-01", end="2021-12-31")

# Print first 5 rows of the data
print(data.head())

# Calculate daily returns
data['AAPL_Return'] = data['Adj Close']['AAPL'].pct_change()
data['WMT_Return'] = data['Adj Close']['WMT'].pct_change()
data['IBM_Return'] = data['Adj Close']['IBM'].pct_change()
data['MU_Return'] = data['Adj Close']['MU'].pct_change()
data['BA_Return'] = data['Adj Close']['BA'].pct_change()
data['AXP_Return'] = data['Adj Close']['AXP'].pct_change()

# Identify potential profitable trades
# For simplicity, let's say a trade is considered profitable if the daily return is more than 2%
profitable_trades = data[(data['AAPL_Return'] > 0.02) | (data['WMT_Return'] > 0.02) | (data['IBM_Return'] > 0.02) | (data['MU_Return'] > 0.02) | (data['BA_Return'] > 0.02) | (data['AXP_Return'] > 0.02)]

print(profitable_trades)
```

This is a very basic example and real world trading algorithms would be much more complex, taking into account many other factors. Also, note that past performance is not indicative of future results. This code is for illustrative purposes only and should not be used for real trading without proper backtesting and risk management.