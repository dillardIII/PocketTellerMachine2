from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I will provide a simple example of a Python code for a mean reversion trading strategy. This strategy assumes that the price of a stock will revert to its mean over time. If the price is above the mean, it's expected to decrease, if it's below the mean, it's expected to increase.

Please note that this is a simplified example and real-world trading strategies are much more complex and involve risk management, transaction costs, and other factors.

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime

# Download historical data for desired stocks
ticker = "AAPL"
ohlcv = yf.download(ticker, start="2020-01-01", end=datetime.today().strftime('%Y-%m-%d'))

# Compute the mean of the last N days 
N = 20
ohlcv['SMA'] = ohlcv['Adj Close'].rolling(window=N).mean()

# Create a column 'Position' where we will store our position
ohlcv['Position'] = None

# If the price is above the SMA, we will short the stock, else we will long the stock
for i in range(N, len(ohlcv)):
    if ohlcv['Adj Close'][i] > ohlcv['SMA'][i]: 
        ohlcv['Position'][i] = -1
    elif ohlcv['Adj Close'][i] < ohlcv['SMA'][i]: 
        ohlcv['Position'][i] = 1

# Forward fill our position column to simulate holding our position
ohlcv['Position'].fillna(method='ffill',inplace=True)

# Calculate the daily market return and multiply that by the position to determine strategy returns
ohlcv['Market Return'] = np.log(ohlcv['Adj Close'] / ohlcv['Adj Close'].shift(1))
ohlcv['Strategy Return'] = ohlcv['Market Return'] * ohlcv['Position']

# Calculate the cumulative product of the strategy returns
ohlcv['Strategy Cumulative Return'] = (1 + ohlcv['Strategy Return']).cumprod()

print(ohlcv)
```

This code will download the historical data for the desired stock (in this case, Apple), calculate the mean of the last 20 days, and decide whether to long or short the stock based on whether the price is below or above the mean. Then, it calculates the return of the strategy and the cumulative return.

Please note that this is a very simplified trading strategy and is not recommended for actual trading. For real trading, you should consider transaction costs, risk management, different types of orders and many other factors.