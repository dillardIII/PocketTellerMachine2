Sure, here is a simple Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is one of the most commonly used by traders. It involves two moving averages, one short term and one long term. When the short term moving average crosses above the long term moving average, it's a signal to buy. Conversely, when the short term moving average crosses below the long term moving average, it's a signal to sell.

Please note that this is a very simplified version of a trading strategy and real-world trading strategies can be much more complex and take into account many more factors.

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
    # Calculate the short and long term moving averages
    short_mavg = calculate_sma(data, short_window)
    long_mavg = calculate_sma(data, long_window)

    # Create a 'signals' DataFrame with the signal information
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Generate trading signals based on moving averages
    signals['short_mavg'] = short_mavg
    signals['long_mavg'] = long_mavg

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Fetch some data
start_date = '2010-01-01'
end_date = '2020-12-31'
data = web.DataReader('AAPL', 'yahoo', start_date, end_date)

# Implement the trading strategy
signals = trading_strategy(data['Close'], 40, 100)
print(signals)
```

In this code, we first define functions to calculate the Simple Moving Average (SMA) and Exponential Moving Average (EMA). We then define our trading strategy function which calculates the short and long term moving averages, generates trading signals based on these averages, and generates trading orders based on these signals. Finally, we fetch some historical data for Apple Inc. from Yahoo Finance and implement our trading strategy on this data.