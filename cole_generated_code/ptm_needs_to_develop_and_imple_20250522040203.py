from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a basic example of a trading strategy using Python. This strategy will be a simple moving average crossover strategy. 

Before we start, please make sure you have the following Python libraries installed: pandas, yfinance, matplotlib, and numpy.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Calculate the short-term simple moving average
short_sma = tickerDf.Close.rolling(window=20).mean()

# Calculate the long-term simple moving average
long_sma = tickerDf.Close.rolling(window=100).mean()

# Create a column in the dataframe to hold the trading signals
tickerDf['signal'] = 0.0

# Generate trading signals based on the crossover of the short-term and long-term moving averages
tickerDf['signal'][20:] = np.where(short_sma[20:] > long_sma[20:], 1.0, 0.0)

# Generate trading orders based on the change in signals
tickerDf['positions'] = tickerDf['signal'].diff()

# Plot the closing price, short-term and long-term moving averages and buy/sell signals
plt.figure(figsize=(20,10))
plt.plot(tickerDf.Close, label='Close Price', color='blue', alpha=0.35)
plt.plot(short_sma, label='20-day SMA', color='red',alpha=0.35)
plt.plot(long_sma, label='100-day SMA', color='green', alpha=0.35)
plt.plot(tickerDf.positions[tickerDf.positions == 1.0].index, 
         short_sma[tickerDf.positions == 1.0], '^' , markersize=10, color='m')
plt.plot(tickerDf.positions[tickerDf.positions == -1.0].index, 
         short_sma[tickerDf.positions == -1.0], 'v' , markersize=10, color='k')
plt.ylabel('Price in $')
plt.xlabel('Trade Date')
plt.title('Historical Trading Signals')
plt.legend(loc='best')
plt.grid(True)
plt.show()
```

This script will download the historical prices for Apple Inc. (AAPL) from 2010 to 2020, calculate the 20-day and 100-day simple moving averages, generate trading signals based on the crossover of these moving averages, and plot the closing price, moving averages and trading signals.

Please note that this is a very basic trading strategy and should not be used for actual trading without further enhancements and testing.