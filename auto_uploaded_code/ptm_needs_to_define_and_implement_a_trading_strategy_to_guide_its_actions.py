Sure, here's a simple example of a Python code that implements a basic trading strategy. This strategy is called Moving Average Crossover, which is used to determine when to buy and sell stock.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving average
    data['short_sma'] = calculate_sma(data['Adj Close'], short_window)
    data['long_sma'] = calculate_sma(data['Adj Close'], long_window)

    # Create signals
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_sma'][short_window:] > data['long_sma'][short_window:], 1.0, 0.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

    return data

# Define the stock to be used
stock = 'AAPL'
# Load the data
data = web.DataReader(stock, 'yahoo', start='01/01/2020', end='01/01/2021')
# Implement the trading strategy
result = trading_strategy(data, 50, 200)

# Print the result
print(result)
```

In this code, we first define two helper functions to calculate the Simple Moving Average (SMA) and Exponential Moving Average (EMA). Then we define the trading strategy function which calculates the SMA for a short and long window, generates signals based on the SMA values, and generates trading orders based on these signals.

Please note that this is a very basic trading strategy and might not be profitable in real trading. Real trading strategies should consider many other factors and might be much more complex. Also, this code requires the `pandas_datareader` library to fetch the stock data, and `pandas` and `numpy` for data manipulation.