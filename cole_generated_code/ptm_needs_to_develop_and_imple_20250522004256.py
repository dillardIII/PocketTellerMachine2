Sure, I can provide a simple example of a trading strategy using Python. This strategy will be based on a simple Moving Average Crossover, which is a popular strategy in algorithmic trading.

Please note that this is a very basic example and real-world trading strategies can be much more complex and involve sophisticated statistical and machine learning techniques.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

def calculate_SMA(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_EMA(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving average
    data['short_SMA'] = calculate_SMA(data['Adj Close'], short_window)
    data['long_SMA'] = calculate_SMA(data['Adj Close'], long_window)
    
    # Create signals based on the crossover of short and long SMA
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_SMA'][short_window:] > data['long_SMA'][short_window:], 1.0, 0.0)
    
    # Generate trading orders based on signals
    data['positions'] = data['signal'].diff()
    
    return data

# Fetch data
data = web.DataReader('AAPL', 'yahoo', start='01/01/2020', end='01/01/2021')
short_window = 40
long_window = 100

# Implement the strategy
trading_data = trading_strategy(data, short_window, long_window)

# Print the DataFrame
print(trading_data)
```

In this code, we first fetch historical data for Apple Inc. from Yahoo Finance. We then calculate the short and long window simple moving averages (SMA) for the adjusted closing prices. We generate trading signals based on the crossover of these SMAs. A buy signal is generated when the short SMA crosses above the long SMA, and a sell signal is generated when the short SMA crosses below the long SMA.

Please note that you will need to install the `pandas_datareader` library to fetch the data from Yahoo Finance. You can install it using pip:

```
pip install pandas_datareader
```

Also, please remember that this is a simple example and doesn't take into account trading costs, slippage, market impact, or other factors that could affect performance. Always backtest your strategies before live trading.