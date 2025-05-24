Here is a simple Python code that uses a basic trading strategy called Moving Average Crossover. This strategy is widely used in trading and it's a good starting point for PTM. 

This strategy uses two moving averages, a fast moving average and a slow moving average. A buy signal is generated when the fast moving average crosses above the slow moving average, and a sell signal is generated when the fast moving average crosses below the slow moving average.

Please note, this is a basic strategy and may not be suitable for all market conditions. It's recommended to test and adjust the strategy according to specific needs.

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
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = calculate_sma(data, short_window)
    # Long moving average
    signals['long_mavg'] = calculate_sma(data, long_window)

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Fetch data
data = web.DataReader('AAPL', 'yahoo', start='01/01/2020', end='01/01/2022')

# Define the short and long windows
short_window = 40
long_window = 100

# Generate trading signals
signals = trading_strategy(data['Close'], short_window, long_window)

# Print signals
print(signals)
```

This code fetches historical price data for Apple Inc. from Yahoo Finance, calculates the short and long moving averages, and generates trading signals based on the crossover of these moving averages. The 'positions' column in the resulting DataFrame indicates the trading orders: 1.0 for buying and -1.0 for selling.