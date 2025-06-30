from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop and test new trading strategies, we can use Python libraries like pandas for data manipulation, numpy for numerical computation, matplotlib for visualization, and yfinance to fetch historical market data. Here's a simple example of a moving average crossover strategy.

```python
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Fetch historical market data
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Calculate the short-term simple moving average
short_sma = data['Close'].rolling(window=20).mean()

# Calculate the long-term simple moving average
long_sma = data['Close'].rolling(window=100).mean()

# Create a 'signal' column where 1 indicates to buy and 0 indicates to sell
data['signal'] = 0.0
data['signal'][short_sma > long_sma] = 1.0

# Create a 'positions' column showing the market position
data['positions'] = data['signal'].diff()

# Plot the closing price, short-term and long-term moving averages and buy/sell signals
plt.figure(figsize=(10,7))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(short_sma, label='20-day SMA', color='red')
plt.plot(long_sma, label='100-day SMA', color='green')
plt.plot(data.loc[data.positions == 1.0].index, 
         data.short_sma[data.positions == 1.0],
         '^', markersize=10, color='m', label='buy')
plt.plot(data.loc[data.positions == -1.0].index, 
         data.short_sma[data.positions == -1.0],
         'v', markersize=10, color='k', label='sell')
plt.ylabel('Price in $')
plt.xlabel('Date')
plt.title('AAPL: Moving Average Crossover Trading Strategy')
plt.legend()
plt.grid()
plt.show()
```

This code fetches historical data for AAPL, calculates short-term and long-term simple moving averages, generates buy/sell signals based on these averages, and plots the results. This is a very basic strategy and should be further developed and backtested before live trading.

Please note that this is a simple demonstration and not financial advice. Always do your own research before trading.