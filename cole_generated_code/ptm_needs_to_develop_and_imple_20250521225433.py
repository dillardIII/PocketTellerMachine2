To develop a trading strategy, we can use a simple moving average (SMA) crossover strategy. This strategy is based on two moving averages, a "fast" moving average and a "slow" moving average. When the fast moving average crosses above the slow moving average, it generates a buy signal. When the fast moving average crosses below the slow moving average, it generates a sell signal.

Here is a simple Python code using pandas library to implement this strategy:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

def calculate_sma(data, window):
    return data.rolling(window=window).mean()

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long moving averages
    data["short_mavg"] = calculate_sma(data["Close"], short_window)
    data["long_mavg"] = calculate_sma(data["Close"], long_window)

    # Create signals
    data["signal"] = 0.0
    data["signal"][short_window:] = np.where(data["short_mavg"][short_window:] > data["long_mavg"][short_window:], 1.0, 0.0)

    # Generate trading orders
    data["positions"] = data["signal"].diff()

# Fetch data
data = web.DataReader('AAPL', 'yahoo', start='01/01/2010', end='01/01/2022')

# Implement the trading strategy
trading_strategy(data, 50, 200)

# Plot the data
plt.figure(figsize=(10,5))
plt.plot(data["Close"], label="Close Price")
plt.plot(data["short_mavg"], label="50-days SMA")
plt.plot(data["long_mavg"], label="200-days SMA")
plt.plot(data.loc[data.positions == 1.0].index, data.short_mavg[data.positions == 1.0], '^', markersize=10, color='g', label='buy')
plt.plot(data.loc[data.positions == -1.0].index, data.short_mavg[data.positions == -1.0], 'v', markersize=10, color='r', label='sell')
plt.title('AAPL SMA Crossover Trading Signals')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()
```

This code fetches historical data for Apple Inc. (AAPL) from Yahoo Finance, calculates the 50-day and 200-day simple moving averages, generates trading signals based on the crossover of these moving averages, and plots the close price, moving averages and trading signals.

Please note that this is a simple trading strategy and may not always result in potential wins. It's always recommended to use more sophisticated strategies and consider other factors like trading fees and market volatility.