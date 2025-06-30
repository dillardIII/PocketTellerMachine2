from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop and implement trading strategies, we can use Python's Pandas library for data analysis and manipulation, Matplotlib for data visualization, and NumPy for numerical computation. We can also use the yfinance library to download historical market data from Yahoo Finance.

Here is a simple Python code for a moving average crossover strategy. This strategy is one of the most common systematic trading strategies that uses two moving averages, one short (fast) and one long (slow). When the short moving average crosses above the long moving average, it could be a buy signal, and when it crosses below, it could be a sell signal.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Use close price for our analysis
close = tickerDf['Close']

# Calculate the short and long moving averages
short_window = 40
long_window = 100

signals = pd.DataFrame(index=close.index)
signals['signal'] = 0.0

# Short moving average
signals['short_mavg'] = close.rolling(window=short_window, min_periods=1, center=False).mean()

# Long moving average
signals['long_mavg'] = close.rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print DataFrame
print(signals)

# Plotting
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Price in $')
close.plot(ax=ax1, color='r', lw=2.)
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='m')

# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='k')

plt.show()
```

This code will plot the close price, short moving average, and long moving average of the stock, and mark the buy and sell signals. Please replace 'AAPL' with the ticker symbol of the stock you want to analyze.

Please note that this is a very simple trading strategy and may not always result in wins. It's important to consider other factors and strategies when making trading decisions.