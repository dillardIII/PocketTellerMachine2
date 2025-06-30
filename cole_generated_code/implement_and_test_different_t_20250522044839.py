from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that uses the `yfinance` library to download stock data and `pyfolio` library to analyze trading strategies. In this example, we will implement and test two simple trading strategies: 

1. Buy and Hold: This strategy involves buying a stock and holding it for a long period.
2. Simple Moving Average Crossover: This strategy involves buying a stock when its short-term moving average crosses above its long-term moving average, and selling the stock when the short-term moving average crosses below the long-term moving average.

```python
import yfinance as yf
import pyfolio as pf
import pandas as pd
import numpy as np

# Download historical data for desired stocks
tickers = ['AAPL', 'MSFT', 'GOOGL']
data = yf.download(tickers, start="2020-01-01", end="2022-12-31")['Adj Close']

def buy_and_hold(data, ticker):
    prices = data[ticker]
    return np.log(prices / prices.shift(1))

def sma_crossover(data, ticker, short_window=20, long_window=100):
    prices = data[ticker]
    short_sma = prices.rolling(window=short_window, min_periods=1).mean()
    long_sma = prices.rolling(window=long_window, min_periods=1).mean()
    buy_signal = short_sma > long_sma
    sell_signal = short_sma < long_sma
    return np.log(prices[1:] / prices[:-1]) * buy_signal.shift(1) - np.log(prices[1:] / prices[:-1]) * sell_signal.shift(1)

# Test strategies
for ticker in tickers:
    bh_returns = buy_and_hold(data, ticker).dropna()
    sma_returns = sma_crossover(data, ticker).dropna()

    print(f"Performance for {ticker}")
    print("Buy and Hold")
    pf.create_simple_tear_sheet(bh_returns)
    print("SMA Crossover")
    pf.create_simple_tear_sheet(sma_returns)
```

Please note that this is a simple example and real-world trading strategies can be much more complex. Also, the performance of these strategies can vary greatly depending on the time period and the stocks chosen. Always do your own research and consider the risks before trading.