Here is a simple Python code for implementing and testing different trading strategies using the `yfinance` and `pandas` libraries. The strategies we will test are:

1. Buy and Hold: Buy a stock and hold it for a certain period.
2. Simple Moving Average Crossover: Buy a stock when its short-term average is above its long-term average and sell when the opposite is true.

```python
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

# Buy and Hold Strategy
initial_investment = tickerDf['Close'][0]
final_value = tickerDf['Close'][-1]
profit_buy_and_hold = final_value - initial_investment
print('Profit from Buy and Hold Strategy: ', profit_buy_and_hold)

# Simple Moving Average Crossover Strategy
short_rolling = tickerDf['Close'].rolling(window=20).mean()
long_rolling = tickerDf['Close'].rolling(window=100).mean()

tickerDf['short_rolling'] = short_rolling
tickerDf['long_rolling'] = long_rolling

# Create signals
tickerDf['signal'] = 0.0
tickerDf['signal'][short_rolling > long_rolling] = 1.0
tickerDf['positions'] = tickerDf['signal'].diff()

# Calculate profit
tickerDf['market_value'] = tickerDf['Close'] * tickerDf['positions']
profit_sma_crossover = tickerDf['market_value'].sum()
print('Profit from Simple Moving Average Crossover Strategy: ', profit_sma_crossover)

# Plotting
fig, ax = plt.subplots(figsize=(16,9))

ax.plot(tickerDf.index, tickerDf['Close'], label='Price')
ax.plot(tickerDf.index, tickerDf['short_rolling'], label = '20-days SMA')
ax.plot(tickerDf.index, tickerDf['long_rolling'], label = '100-days SMA')

ax.plot(tickerDf.loc[tickerDf.positions == 1.0].index, 
         tickerDf.short_rolling[tickerDf.positions == 1.0],
         '^', markersize=10, color='m', label='buy')
         
ax.plot(tickerDf.loc[tickerDf.positions == -1.0].index, 
         tickerDf.short_rolling[tickerDf.positions == -1.0],
         'v', markersize=10, color='k', label='sell')
plt.legend()
plt.show()
```

Please note that this is a very basic implementation and real trading strategies would require much more complex algorithms, risk management and would also consider transaction costs. Also, this code assumes that you can buy fractional shares.