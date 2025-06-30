from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code for a trading strategy using moving averages. This strategy is based on the idea that if the short term moving average is above the long term moving average, it's a good time to buy. Conversely, if the short term moving average is below the long term moving average, it's a good time to sell.

Please note that this is a very basic strategy and real-world trading strategies can be much more complex and require more sophisticated algorithms and risk management techniques.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long moving averages
    sma_short = calculate_sma(data, short_window)
    sma_long = calculate_sma(data, long_window)

    # Create a 'signal' (invested or not invested) data series
    signal = pd.Series(index=data.index)
    signal[short_window:] = np.where(sma_short[short_window:] > sma_long[short_window:], 1.0, 0.0)   

    # Generate trading orders
    orders = signal.diff()

    return orders

# Fetch the data
data = web.DataReader('AAPL', 'yahoo', start='01/01/2010', end='01/01/2022')

# Implement the trading strategy
orders = trading_strategy(data['Close'], 50, 200)

# Plot the stock price and the buy/sell signals
plt.figure(figsize=(15, 10))
plt.plot(data['Close'], color='black', label='Close Price')
plt.plot(calculate_sma(data['Close'], 50), color='blue', label='50-day SMA')
plt.plot(calculate_sma(data['Close'], 200), color='red', label='200-day SMA')

plt.plot(orders.loc[orders == 1.0].index, 
         data['Close'][orders == 1.0], 
         '^', markersize=10, color='g', label='buy')

plt.plot(orders.loc[orders == -1.0].index, 
         data['Close'][orders == -1.0], 
         'v', markersize=10, color='r', label='sell')

plt.title('AAPL: Moving Average Crossover Trading Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='best')
plt.grid(True)
plt.show()
```

This code will fetch the historical data for Apple Inc. (AAPL) from Yahoo Finance, calculate the 50-day and 200-day simple moving averages (SMA), generate trading signals based on the crossover of these two SMAs, and plot the stock price along with the buy/sell signals.