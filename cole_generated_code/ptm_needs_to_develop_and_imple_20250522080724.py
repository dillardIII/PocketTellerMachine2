Sure, here's a simple example of a Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is used to identify buying and selling points based on the crossover of short-term and long-term moving averages.

Please note that this is a very basic strategy and in real-world trading, you'd need to consider many other factors like transaction costs, risk management, etc. Also, you'd need to use APIs provided by your broker to fetch real-time data and execute trades.

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
    # Calculate short term and long term moving averages
    data['short_mavg'] = calculate_sma(data['Close'], short_window)
    data['long_mavg'] = calculate_sma(data['Close'], long_window)

    # Create signals
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_mavg'][short_window:] > data['long_mavg'][short_window:], 1.0, 0.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

    return data

# Fetch data
data = web.get_data_yahoo('AAPL', start='01-01-2020', end='31-12-2020')

# Implement the trading strategy
trading_data = trading_strategy(data, 50, 200)

# Print data
print(trading_data)
```

In this code, we're fetching historical data for Apple Inc. (AAPL) for the year 2020. We're then calculating short-term (50 days) and long-term (200 days) simple moving averages. If the short-term moving average is above the long-term moving average, we generate a buy signal (1.0), otherwise, we generate a sell signal (0.0). We then calculate the difference in signals to generate trading orders. A positive difference indicates a buy order and a negative difference indicates a sell order.