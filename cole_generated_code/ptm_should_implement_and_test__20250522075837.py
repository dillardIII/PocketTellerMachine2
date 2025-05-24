Here is a simple Python code for a trading strategy using Moving Average Crossover. This strategy generates potential wins by buying when the short term moving average crosses above the long term moving average and selling when the short term moving average crosses below the long term moving average.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

def plot(data, signals):
    # Plot the price and moving averages
    plt.figure(figsize=(10,5))
    plt.plot(data, label='Price')
    plt.plot(signals['short_mavg'], label='Short Moving Average')
    plt.plot(signals['long_mavg'], label='Long Moving Average')
    plt.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0], '^', markersize=10, color='g', label='Buy')
    plt.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0], 'v', markersize=10, color='r', label='Sell')
    plt.title('Trading Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

# Fetch data
data = web.DataReader('AAPL', 'yahoo', start='01/01/2020', end='12/31/2020')['Close']

# Define the short and long windows
short_window = 40
long_window = 100

# Generate signals
signals = trading_strategy(data, short_window, long_window)

# Plot
plot(data, signals)
```

This code uses Yahoo Finance to fetch the historical data for Apple Inc. (AAPL) for the year 2020. The short and long windows for the moving averages are set to 40 and 100 days, respectively. The code then generates trading signals based on the moving average crossover strategy and plots the price, moving averages, and trading signals.

Please note that this is a simple trading strategy and may not always generate profits. It's always recommended to use more sophisticated strategies and risk management techniques when trading.