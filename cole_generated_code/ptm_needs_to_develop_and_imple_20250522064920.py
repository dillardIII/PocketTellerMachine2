Sure, I can provide a simple example of a Python code that implements a basic trading strategy. This strategy is called Moving Average Crossover, which is one of the most common systematic trading strategies. 

Please note that this is a very simplistic example and real-world trading strategies involve much more considerations and complex algorithms.

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
    data['short_sma'] = calculate_sma(data['Close'], short_window)
    data['long_sma'] = calculate_sma(data['Close'], long_window)

    # Create signals based on the crossover of the short and long SMA
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_sma'][short_window:] 
                                             > data['long_sma'][short_window:], 1.0, 0.0)

    # Generate trading orders based on the signals
    data['positions'] = data['signal'].diff()

    return data

# Fetch the data
data = web.DataReader('AAPL', data_source='yahoo', start='01-01-2010', end='01-01-2022')

# Implement the strategy
trading_data = trading_strategy(data, 50, 200)

# Print the DataFrame
print(trading_data)
```

This code fetches historical price data for Apple Inc. (AAPL) from Yahoo Finance and calculates the 50-day and 200-day simple moving averages (SMA). When the 50-day SMA is above the 200-day SMA, it generates a buy signal, and when it's below, it generates a sell signal.

Please note that this is a very basic strategy and should not be used for real trading without further enhancements. Also, you need to install the pandas_datareader library if it's not already installed. You can install it using pip:

```bash
pip install pandas_datareader
```

Also, please remember to replace 'AAPL' with the ticker symbol of the stock you want to analyze.