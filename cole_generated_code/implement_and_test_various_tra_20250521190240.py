Sure, I'll provide a basic example of a simple moving average crossover strategy using Python and the pandas library. This strategy is not guaranteed to be profitable and is just for illustrative purposes. You should always backtest and adjust your strategies based on your own research and risk tolerance.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for desired ticker symbol
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2022-01-01')

# Calculate short-term simple moving average
short_sma = data['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = data['Close'].rolling(window=100).mean()

# Create signals based on crossover
data['signal'] = 0.0
data['signal'][short_sma > long_sma] = 1.0

# Generate trading orders
data['position'] = data['signal'].diff()

# Plot data
plt.figure(figsize=(20,10))
data['Close'].plot(color='blue', lw=2.)
short_sma.plot(color='red', lw=2.)
long_sma.plot(color='green', lw=2.)
plt.plot(data.loc[data.position == 1.0].index, 
         short_sma[data.position == 1.0],
         '^', markersize=10, color='m')
plt.plot(data.loc[data.position == -1.0].index, 
         short_sma[data.position == -1.0],
         'v', markersize=10, color='k')
plt.ylabel('Price in $')
plt.xlabel('Date')
plt.legend(["Price","Short SMA","Long SMA","Buy","Sell"])
plt.grid()
plt.show()
```

This script downloads historical price data for Apple Inc. (AAPL) from Yahoo Finance, calculates the 20-day and 100-day simple moving averages, and generates trading signals based on when these averages cross over each other. It then plots the price data and trading signals.

Please note that this is a very basic trading strategy and is unlikely to be profitable without further refinement. It also does not take into account trading costs or taxes, which could significantly impact the profitability of a strategy.