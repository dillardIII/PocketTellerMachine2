from ghost_env import INFURA_KEY, VAULT_ADDRESS
To implement and test new trading strategies, we can create a simple Python script that uses a basic trading strategy as an example. Here, we will use the Moving Average Crossover strategy. This strategy is one of the most commonly used strategies in trading. It involves two moving averages, one short-term and one long-term. When the short-term average crosses above the long-term average, it signals a buy opportunity, and when it crosses below, it signals a sell opportunity.

Please note that you need to install pandas, numpy, matplotlib and yfinance libraries to run this script. You can install them using pip:
```
pip install pandas numpy matplotlib yfinance
```

Here is a simple Python script that implements this strategy:

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

# Use close price for our calculations
close = tickerDf['Close']

# Calculate the short-term moving average
short_rolling = close.rolling(window=20).mean()

# Calculate the long-term moving average
long_rolling = close.rolling(window=100).mean()

# Create signals
signals = pd.DataFrame(index=close.index)
signals['signal'] = 0.0
signals['short_ma'] = short_rolling
signals['long_ma'] = long_rolling
signals['signal'][short_rolling > long_rolling] = 1.0

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Plot everything
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Price in $')
close.plot(ax=ax1, color='r', lw=2.)
signals[['short_ma', 'long_ma']].plot(ax=ax1, lw=2.)

# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_ma[signals.positions == 1.0],
         '^', markersize=10, color='m')

# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_ma[signals.positions == -1.0],
         'v', markersize=10, color='k')

plt.show()
```

This script will download the historical price data for the Apple Inc. (AAPL) stock, calculate the short-term and long-term moving averages, generate trading signals and plot everything. The buy signals are marked with up arrows and the sell signals are marked with down arrows.

Please note that this is a very basic trading strategy and it's used here just for demonstration purposes. In real trading, you would need to consider many other factors like transaction costs, slippage, risk management, etc. Also, you would need to test your strategy with out-of-sample data to avoid overfitting.