from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop and implement trading strategies, we can use Python with the help of libraries like pandas for data manipulation, numpy for numerical computations, and matplotlib for visualizations. We can also use the yfinance library to download historical market data from Yahoo finance.

Here is a simple Python code that implements a moving average crossover strategy, which is one of the most common systematic trading strategies.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for required stocks
data = yf.download('AAPL','2016-01-01','2021-12-31')

# Calculate short-term simple moving average
ShortEMA = data.Close.ewm(span=12, adjust=False).mean()

# Calculate long-term simple moving average
LongEMA = data.Close.ewm(span=26, adjust=False).mean()

# Create signals based on crossover
data['Buy_Signal'] = np.where(ShortEMA > LongEMA, 1, 0)
data['Sell_Signal'] = np.where(ShortEMA < LongEMA, -1, 0)

# Create trading orders
data['Buy_Trade'] = np.where(data['Buy_Signal'] > data['Buy_Signal'].shift(1), data['Close'], np.nan)
data['Sell_Trade'] = np.where(data['Sell_Signal'] < data['Sell_Signal'].shift(1), data['Close'], np.nan)

# Plotting
plt.figure(figsize=(12,5))
plt.plot(data['Close'], label='Close Price', color='blue', alpha=0.35)
plt.plot(ShortEMA, label='Short/Fast EMA', color='red', alpha=0.35)
plt.plot(LongEMA, label='Long/Slow EMA', color='green', alpha=0.35)
plt.scatter(data.index, data['Buy_Trade'], color='green', marker='^', alpha=1)
plt.scatter(data.index, data['Sell_Trade'], color='red', marker='v', alpha=1)
plt.title('Apple Close Price and Trade Signals')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()
```

This code downloads the historical data for Apple Inc. from Yahoo Finance, calculates the short-term and long-term exponential moving averages (EMA), generates buy and sell signals based on the crossover of these EMAs, and plots the close price along with the trade signals.

Please note that this is a very basic trading strategy and might not be profitable in real trading. It's always recommended to backtest any strategy before live trading. Also, this strategy doesn't take into account transaction costs or slippage.