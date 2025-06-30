from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here's a simple Python code that implements a Moving Average Crossover strategy using Pandas. This strategy is one of the most common systematic trading strategies that uses two moving averages, one short and one long. When the short moving average crosses above the long moving average, it's a signal to buy, and when it crosses below, it's a signal to sell.

```python
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for required stocks
data = yf.download('AAPL','2016-01-01','2021-12-31')

# Calculate short-term simple moving average
data['SMA_20'] = data['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Create a 'Signal' (invested or not invested) data series
data['Signal'] = 0.0  
data['Signal'][data['SMA_20'] > data['SMA_50']] = 1.0

# Generate trading orders
data['Position'] = data['Signal'].diff()

# Print the DataFrame
print(data)

# Plotting
plt.figure(figsize = (20,10))
# plot close price, short-term and long-term moving averages 
data['Close'].plot(color = 'k', lw = 1)
data['SMA_20'].plot(color = 'b', lw = 1)
data['SMA_50'].plot(color = 'r', lw = 1)
# plot ‘buy’ signals
plt.plot(data[data['Position'] == 1].index, 
         data['SMA_20'][data['Position'] == 1], 
         '^', markersize = 15, color = 'g', lw = 1)
# plot ‘sell’ signals
plt.plot(data[data['Position'] == -1].index, 
         data['SMA_20'][data['Position'] == -1], 
         'v', markersize = 15, color = 'r', lw = 1)
plt.ylabel('Price in $', fontsize = 15 )
plt.xlabel('Date', fontsize = 15 )
plt.title('Apple Inc. - Moving Average Crossover Trading Signals', fontsize = 20)
plt.legend(['Close Price','20-Day SMA','50-Day SMA','Buy Signal','Sell Signal'])
plt.grid()
plt.show()
```

This code uses Yahoo Finance to download the historical data, calculates the short-term and long-term moving averages, generates trading orders and plots the close price, moving averages and trading signals.

Please note that this is a very basic trading strategy and doesn't take into account transaction costs, slippage, risk management, etc. It's recommended to use this as a starting point and build more complex strategies that fit your risk/reward appetite.