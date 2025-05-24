In order to develop and implement new trading strategies, we first need to define what kind of strategies we are going to use. For this example, let's use a simple moving average crossover strategy. This strategy is based on two moving averages, a "fast" and a "slow" moving average. When the fast moving average crosses above the slow moving average, it's a signal to buy. When it crosses below, it's a signal to sell.

Here is a simple implementation of this strategy using Python and the pandas library:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window).mean()
    return ema

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving averages
    data['short_sma'] = calculate_sma(data['Adj Close'], short_window)
    data['long_sma'] = calculate_sma(data['Adj Close'], long_window)

    # Create a column for the trading signals
    data['signal'] = 0.0

    # Generate trading signals (1 for buy, -1 for sell)
    data['signal'][short_window:] = np.where(data['short_sma'][short_window:] > data['long_sma'][short_window:], 1.0, -1.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

    return data

# Fetch the data
start_date = '2010-01-01'
end_date = '2020-12-31'
data = web.DataReader('AAPL', 'yahoo', start_date, end_date)

# Implement the strategy
trading_data = trading_strategy(data, 50, 200)
```

This code fetches historical data for Apple Inc. from Yahoo Finance, calculates the 50-day and 200-day simple moving averages, generates trading signals based on the crossover of these moving averages, and generates trading orders based on these signals.

Please note that this is a very basic trading strategy and is not guaranteed to be profitable. It's always important to backtest any strategy before using it in live trading. Also, this strategy does not take into account trading costs or slippage.