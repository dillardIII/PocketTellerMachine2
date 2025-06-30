from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a Python code for a trading strategy using Moving Average Crossover. Please note that this is a simplified version and real-world trading strategies can be much more complex and require more sophisticated models.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving averages
    data['short_sma'] = calculate_sma(data['Close'], short_window)
    data['long_sma'] = calculate_sma(data['Close'], long_window)

    # Create a column for the trading signals
    data['signal'] = 0.0

    # Generate trading signals (1 for buy, -1 for sell)
    data['signal'][short_window:] = np.where(data['short_sma'][short_window:] > data['long_sma'][short_window:], 1.0, -1.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

    return data

# Fetch the data
start_date = '2020-01-01'
end_date = '2021-12-31'
ticker = 'AAPL'
df = web.DataReader(ticker, 'yahoo', start_date, end_date)

# Apply the trading strategy
trading_data = trading_strategy(df, 50, 200)

# Plot the data
plt.figure(figsize=(10,5))
plt.plot(trading_data['Close'], label='Close Price', color='blue')
plt.plot(trading_data['short_sma'], label='50-Day SMA', color='red')
plt.plot(trading_data['long_sma'], label='200-Day SMA', color='green')
plt.title('Apple Close Prices & SMA Crossover')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
```

This code fetches historical data for Apple Inc. from Yahoo Finance, calculates the 50-day and 200-day simple moving averages (SMA), generates trading signals based on the crossover of these SMAs, and plots the close prices along with the SMAs. 

Please note that you need to install `pandas_datareader` library if not already installed. You can install it using pip:
```
pip install pandas_datareader
```

Also, this is a very basic strategy and might not be profitable in real trading. Always backtest your strategy before live trading.