from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a Python code implementing a basic moving average crossover trading strategy using pandas. This strategy generates a buy signal when the short-term moving average crosses above the long-term moving average, and a sell signal when the short-term moving average crosses below the long-term moving average.

Please note that this is a very basic strategy and in real trading scenarios, more complex strategies and risk management techniques are used.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the start and end dates for the data
start_date = '01-01-2010'
end_date = '01-01-2022'

# Fetch the data
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short-term and long-term moving averages
short_window = 50
long_window = 200

df['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1).mean()
df['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1).mean()

# Generate the trading signals 0 or 1
df['signal'] = np.where(df['short_mavg'] > df['long_mavg'], 1.0, 0.0)

# Calculate daily returns
df['returns'] = df['Close'].pct_change()

# Calculate strategy returns
df['strategy_returns'] = df['returns'] * df['signal'].shift()

# Plot the stock price, short-term and long-term moving averages and the strategy returns
plt.figure(figsize=(10,5))
plt.title('Stock Price, Moving Averages & Strategy Returns')
plt.plot(df['Close'], label='Stock Price')
plt.plot(df['short_mavg'], label='50-days SMA')
plt.plot(df['long_mavg'], label='200-days SMA')
plt.legend(loc='upper left')
plt.show()

plt.figure(figsize=(10,5))
plt.title('Strategy Returns')
plt.plot(df['strategy_returns'].cumsum(), label='Strategy Returns')
plt.legend(loc='upper left')
plt.show()
```

This script fetches the historical data for the specified stock, calculates the short-term and long-term moving averages, generates trading signals based on these moving averages, calculates the daily and strategy returns, and finally plots the stock price, moving averages and strategy returns.