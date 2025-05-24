Sure, I can provide a simple Python code that simulates a basic trading strategy. In this example, we'll use a simple moving average crossover strategy. This strategy is based on the idea that if the short term moving average crosses the long term moving average, it may be a signal of future price movements.

Please note that this is a very basic strategy and in real-world trading, you would need to consider many other factors such as trading fees, slippage, and market impact. Also, you would need to use real-time data and this code would need to be integrated with a trading platform.

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

# Calculate short-term simple moving average
short_sma = data.rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = data.rolling(window=100).mean()

# Create signals DataFrame
signals = pd.DataFrame(index=data.index)
signals['signal'] = 0.0

# Generate trading signals based on crossover
signals['signal'][short_sma > long_sma] = 1.0

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print the signals
print(signals)
```

This code fetches historical prices for a list of stocks, calculates their short-term and long-term simple moving averages, generates trading signals based on the crossover of these averages, and then generates trading orders based on these signals. The resulting DataFrame contains the trading signals and orders for each stock on each trading day.