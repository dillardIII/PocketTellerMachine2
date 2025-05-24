Sure, I can provide a simple example of a trading strategy using Python. In this example, we'll use a simple moving average crossover strategy. This strategy is one of the most common systematic strategies used in trading. It uses two moving averages, one short and one long. When the short moving average crosses above the long moving average, it's a signal to buy. When the short moving average crosses below the long moving average, it's a signal to sell.

Please note that this is a simplified example and real trading strategies would need to consider many more factors.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Collect data on this ticker
tickerData = pdr.get_data_yahoo(tickerSymbol, start='2020-01-01', end='2022-12-31')

# Calculate short/long simple moving averages
short_sma = tickerData['Close'].rolling(window=20).mean()
long_sma = tickerData['Close'].rolling(window=100).mean()

# Create signals based on crossover
tickerData['signal'] = 0.0
tickerData['signal'][short_sma > long_sma] = 1.0
tickerData['signal'][short_sma < long_sma] = -1.0

# Generate trading orders
tickerData['positions'] = tickerData['signal'].diff()

# Print the DataFrame
print(tickerData)
```

This script will print a DataFrame that includes the original data of the ticker (Open, High, Low, Close, Adj Close, Volume), the calculated short and long moving averages, the generated signals and the trading positions.

Please note that this script uses the Yahoo Finance API to fetch the data, and pandas_datareader and yfinance libraries to handle the data. Make sure to install these libraries before running the script.