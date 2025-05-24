Sure, here is a simple example of a Python code implementing a basic Mean Reversion trading strategy. This strategy is based on the idea that the high and low prices of an asset are a temporary phenomenon that revert to their mean value periodically.

```python
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import yfinance as yf
yf.pdr_override()

# Define the instruments to download. We would like to see Apple, Microsoft and others.
tickers = ['AAPL', 'MSFT', 'IBM', 'GOOG']

# Define which online source to use
data_source = 'yahoo'

# Define the start and end dates that we want to see
start_date = '2010-01-01'
end_date = '2020-12-31'

# Use pandas_datareader.data.DataReader to load the desired data.
panel_data = pdr.get_data_yahoo(tickers, start_date, end_date)

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
close = panel_data['Adj Close']

# Calculate the short-window simple moving average
short_rolling = close.rolling(window=20).mean()

# Calculate the long-window simple moving average
long_rolling = close.rolling(window=100).mean()

# Create a 'signal' (invested or not invested) when the short moving average crosses the long moving average
signal = short_rolling >= long_rolling

# Calculate daily returns
daily_returns = close.pct_change()

# Calculate strategy returns
strategy_returns = daily_returns * signal.shift()

# Calculate cumulative returns
cumulative_returns = (strategy_returns + 1).cumprod()

# Plot strategy returns
cumulative_returns.plot()
plt.show()
```

This is a very basic strategy and may not be profitable in real-world trading. It's recommended to use more sophisticated strategies and risk management in actual trading. Also, always backtest your strategy before live trading.