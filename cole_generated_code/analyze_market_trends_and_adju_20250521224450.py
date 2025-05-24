Analyzing market trends and adjusting trading strategies is a complex task that involves machine learning and data analysis. Below is a simplified example of how you might start to approach this task using Python. This example uses a simple moving average strategy, which is a common strategy in stock trading.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Collect data on this ticker
tickerData = pdr.get_data_yahoo(tickerSymbol, start='2010-1-1', end='2020-12-31')

# Calculate the short-window simple moving average
short_rolling = tickerData.rolling(window=20).mean()

# Calculate the long-window simple moving average
long_rolling = tickerData.rolling(window=100).mean()

# Create signals
signals = pd.DataFrame(index=tickerData.index)
signals['signal'] = 0.0
signals['short_mavg'] = short_rolling['Close']
signals['long_mavg'] = long_rolling['Close']
signals['signal'][short_rolling['Close'] > long_rolling['Close']] = 1.0

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print `signals`
print(signals)
```

This script will fetch historical stock data for Apple Inc. from Yahoo Finance, calculate short and long-window simple moving averages, generate trading signals based on these averages, and generate trading orders based on these signals.

Please note that this is a very basic trading strategy and is not guaranteed to be profitable. Real-world trading involves much more complex strategies, risk management, and regulatory compliance.