To implement and test new trading strategies, we first need to define what those strategies are. For simplicity, let's consider two simple strategies: 

1. Buy Low, Sell High: This strategy involves buying a stock when its price is low and selling it when its price is high.
2. Moving Average Crossover: This strategy involves using two moving averages, one short-term and one long-term. When the short-term average crosses above the long-term average, it's a signal to buy. When it crosses below, it's a signal to sell.

Here is a simple Python code to implement these strategies:

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

# Implementing Buy Low, Sell High Strategy
def buy_low_sell_high(data, ticker):
    # Calculate daily returns
    returns = data[ticker].pct_change()

    # Define signals
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    signals['signal'][returns < returns.mean()] = 1.0   # buy signal
    signals['signal'][returns > returns.mean()] = -1.0  # sell signal

    return signals

# Implementing Moving Average Crossover Strategy
def moving_average_crossover(data, ticker, short_window=5, long_window=20):
    # Calculate moving averages
    short_mavg = data[ticker].rolling(window=short_window, min_periods=1, center=False).mean()
    long_mavg = data[ticker].rolling(window=long_window, min_periods=1, center=False).mean()

    # Define signals
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    signals['signal'][short_mavg > long_mavg] = 1.0   # buy signal
    signals['signal'][short_mavg < long_mavg] = -1.0  # sell signal

    return signals

# Test the strategies
for ticker in tickers_list:
    buy_low_sell_high_signals = buy_low_sell_high(data, ticker)
    moving_average_crossover_signals = moving_average_crossover(data, ticker)

    print(f"{ticker} Buy Low, Sell High Signals:")
    print(buy_low_sell_high_signals)
    print(f"{ticker} Moving Average Crossover Signals:")
    print(moving_average_crossover_signals)
```

Please note that this is a simplified example and real trading strategies would be much more complex, taking into account many other factors. Also, this code assumes that you have the necessary Python packages installed and that you have a valid Yahoo Finance API key.