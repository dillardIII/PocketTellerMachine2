Sure, here is a simple Python code for a trading strategy using Moving Average Crossover. This is a very basic strategy just for illustrative purposes. In real-life scenarios, trading strategies can get very complex and they also need to consider transaction costs, risk management, etc.

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
    # Calculate the short and long window simple moving averages
    data['short_sma'] = calculate_sma(data['Adj Close'], short_window)
    data['long_sma'] = calculate_sma(data['Adj Close'], long_window)

    # Create signals based on the crossover of the short and long SMA
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_sma'][short_window:] > data['long_sma'][short_window:], 1.0, 0.0)

    # Generate trading orders based on the signals
    data['positions'] = data['signal'].diff()

    return data

# Fetch the data
data = web.DataReader('AAPL', 'yahoo', start='01/01/2010', end='01/01/2022')

# Define the short and long windows
short_window = 40
long_window = 100

# Run the trading strategy
trading_data = trading_strategy(data, short_window, long_window)

# Print the trading data
print(trading_data)
```

In this code, we first calculate the short and long window simple moving averages (SMA). Then we create signals based on the crossover of the short and long SMA. When the short SMA is greater than the long SMA, we generate a buy signal (1.0), otherwise we generate a sell signal (0.0). Finally, we generate trading orders based on the signals. When the signal changes, that's when we place a trade.

Please note that you need to install `pandas_datareader` library to fetch the data. You can install it using pip:

```
pip install pandas-datareader
```

Also, this code uses Yahoo Finance to fetch the data, so make sure it is not blocked in your network.