Sure, I can provide a simple example of a Python code that implements a basic trading strategy. This strategy will be based on a simple moving average (SMA). When the price is above the SMA, it will signal to buy, and when it's below the SMA, it will signal to sell.

Please note that this is a very basic strategy and real-world trading strategies can be much more complex and take into account many other factors.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the lookback period for the SMA
lookback = 20

# Get the stock data
df = web.DataReader(stock, data_source='yahoo', start='01-01-2010')

# Calculate the SMA
df['SMA'] = df['Adj Close'].rolling(window=lookback).mean()

# Create a column to hold the trading signals
df['Signal'] = 0.0

# Generate trading signals based on the SMA
df['Signal'][lookback:] = np.where(df['Adj Close'][lookback:] > df['SMA'][lookback:], 1.0, 0.0)

# Generate trading orders based on the signals
df['Position'] = df['Signal'].diff()

# Print the DataFrame
print(df)

# Plot the stock price, SMA and trading signals
plt.figure(figsize=(10,5))
plt.plot(df['Adj Close'], label=stock)
plt.plot(df['SMA'], label='SMA')
plt.plot(df[df['Position'] == 1].index, df['SMA'][df['Position'] == 1], '^', markersize=10, color='g', label='buy')
plt.plot(df[df['Position'] == -1].index, df['SMA'][df['Position'] == -1], 'v', markersize=10, color='r', label='sell')
plt.ylabel('Price')
plt.xlabel('Date')
plt.legend(loc='best')
plt.show()
```

This code uses the `pandas_datareader` package to fetch stock data from Yahoo Finance. It then calculates the simple moving average (SMA) of the stock price and generates trading signals based on whether the price is above or below the SMA. Finally, it plots the stock price, the SMA, and the trading signals.

Please note that you need to install the `pandas_datareader` package if it's not installed yet. You can install it using pip: `pip install pandas-datareader`.

Also, this is a simple example and doesn't take into account transaction costs and other important factors. Always do your own research and consider consulting with a financial advisor before implementing a trading strategy.