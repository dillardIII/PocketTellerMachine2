from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop and implement trading strategies in Python, we need to use libraries like pandas for data manipulation, numpy for mathematical calculations, matplotlib for data visualization, and yfinance to download the stock data. Here's a simple example of a moving average crossover strategy:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for desired stocks
ticker = "AAPL"
tickerData = yf.Ticker(ticker)
data = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Calculate the short-term exponential moving average (EMA)
ShortEMA = data.Close.ewm(span=12, adjust=False).mean()

# Calculate the long-term exponential moving average (EMA)
LongEMA = data.Close.ewm(span=26, adjust=False).mean()

# Create signals based on crossover
data['Buy_Signal'] = np.where(ShortEMA > LongEMA, 1, 0)
data['Sell_Signal'] = np.where(ShortEMA < LongEMA, -1, 0)

# Calculate daily returns and strategy returns
data['Return'] = np.log(data.Close / data.Close.shift(1))
data['Strategy_Return'] = data.Return * data.Buy_Signal.shift(1)

# Plot the strategy returns
plt.figure(figsize=(10,5))
np.exp(data.Strategy_Return.cumsum()).plot()
plt.ylabel("Strategy Returns (%)")
plt.show()
```

This is a simple moving average crossover strategy where we buy the stock when the short-term EMA crosses above the long-term EMA and sell the stock when the short-term EMA crosses below the long-term EMA.

Please note that this is a very basic strategy and may not be profitable in real trading. It's always recommended to backtest the strategy with historical data before implementing it in live trading. Also, this doesn't take into account transaction costs or slippage. 

For diversification, you can run this strategy on different stocks and combine the results. This way, you're not relying on a single stock for your returns.