Sure, I can provide a simple example of a Python code that uses a simple moving average crossover strategy. This is a common strategy used in trading. Please note that this is a very basic example and real trading strategies can get much more complex.

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
    data['short_sma'] = calculate_sma(data['Close'], short_window)
    data['long_sma'] = calculate_sma(data['Close'], long_window)

    # Create signals
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_sma'][short_window:] > data['long_sma'][short_window:], 1.0, 0.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()
    
    return data

# Fetch data
ticker = 'AAPL'
data = web.DataReader(ticker, 'yahoo', start='01-01-2015', end='31-12-2020')

# Use the trading strategy
short_window = 40
long_window = 100
data = trading_strategy(data, short_window, long_window)

# Print data
print(data)
```

In this code, we fetch historical stock price data for Apple Inc. from Yahoo Finance. Then we calculate the short and long window simple moving averages (SMA) of the closing prices. We generate a signal when the short SMA is greater than the long SMA. A trading order is generated when the signal changes. A positive change in the signal indicates a buy order and a negative change in the signal indicates a sell order.

Please note that this is a very basic trading strategy and it doesn't consider transaction costs, slippage, risk management, etc. Also, using historical data to test trading strategies can lead to overfitting and it doesn't guarantee future performance. Always use proper risk management and consult with a financial advisor before live trading.