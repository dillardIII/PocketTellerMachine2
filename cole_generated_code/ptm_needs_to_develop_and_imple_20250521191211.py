from ghost_env import INFURA_KEY, VAULT_ADDRESS
Developing a trading strategy involves a lot of factors and can be quite complex. Here's a simple example of a Python code that uses a basic moving average crossover strategy for trading. This strategy buys when the short-term moving average crosses above the long-term moving average, and sells when the short-term moving average crosses below the long-term moving average.

Please note that this is a simplified example and real-world trading strategies involve much more factors and complex algorithms.

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
    # Calculate the short and long-term moving averages
    data['short_mavg'] = calculate_sma(data['Close'], short_window)
    data['long_mavg'] = calculate_sma(data['Close'], long_window)

    # Create signals
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_mavg'][short_window:] 
                                            > data['long_mavg'][short_window:], 1.0, 0.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

    return data

# Fetch the data
start_date = '2010-01-01'
end_date = '2020-12-31'
data = web.DataReader('AAPL', 'yahoo', start_date, end_date)

# Define the short and long-term windows
short_window = 40
long_window = 100

# Run the trading strategy
trading_data = trading_strategy(data, short_window, long_window)

# Print the trading signals
print(trading_data)
```

In this code:

- We use pandas_datareader to fetch historical stock price data from Yahoo Finance.
- We define two functions to calculate the simple moving average (SMA) and exponential moving average (EMA).
- We define a function 'trading_strategy' that calculates the short and long-term moving averages, generates trading signals based on these averages, and generates trading orders based on these signals.
- We fetch the historical data for Apple Inc. (AAPL) for the period from 2010 to 2020.
- We define the short and long-term windows as 40 and 100 days, respectively.
- We run the trading strategy and print the trading signals.