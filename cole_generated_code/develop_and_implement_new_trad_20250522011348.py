from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is one of the most commonly used strategies in trading. It involves two moving averages, one short period and one long period. When the short period moving average crosses above the long period moving average, it's a signal to buy. Conversely, when the short period moving average crosses below the long period moving average, it's a signal to sell.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Download the historical data
df = web.DataReader(stock, data_source='yahoo', start='01-01-2010')

# Calculate the short-term simple moving average (SMA)
short_sma = df.Close.rolling(window=20).mean()

# Calculate the long-term SMA
long_sma = df.Close.rolling(window=100).mean()

# Create signals based on the crossover of short and long SMA
df['Buy_Signal'] = np.where(short_sma > long_sma, 1, 0)
df['Sell_Signal'] = np.where(short_sma < long_sma, -1, 0)

# Generate trading orders
df['Trade'] = df['Buy_Signal'] + df['Sell_Signal']

# Plot the stock price and the two SMA
plt.figure(figsize=(12,5))
plt.title('Stock Price with Trading Strategy')
plt.plot(df['Close'], label='Stock Price', color='blue')
plt.plot(short_sma, label='Short-term SMA', color='red')
plt.plot(long_sma, label='Long-term SMA', color='green')
plt.legend(loc='upper left')
plt.show()
```

Please note that this is a very basic trading strategy and it's not guaranteed to always make profit. You should always backtest your strategy before using it in live trading. Also, this strategy doesn't take into account transaction costs. If you're trading frequently, transaction costs could significantly affect your profits.