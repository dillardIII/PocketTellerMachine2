from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple Python code that simulates a basic trading strategy. Here, we will use a simple moving average crossover strategy. This strategy is based on two moving averages, one short and one long. When the short moving average crosses above the long moving average, it's a signal to buy. When the short moving average crosses below the long moving average, it's a signal to sell.

Please note that this is a very basic strategy and real-world trading strategies are much more complex and take into account many other factors.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the start and end dates of the trading period
start_date = '01-01-2020'
end_date = '31-12-2020'

# Get the stock data
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short and long moving averages
short_ma = df['Close'].rolling(window=20).mean()
long_ma = df['Close'].rolling(window=100).mean()

# Create signals based on the crossover of the short and long moving averages
df['Buy_Signal'] = np.where(short_ma > long_ma, 1, 0)
df['Sell_Signal'] = np.where(short_ma < long_ma, -1, 0)

# Plot the stock price and the buy and sell signals
plt.figure(figsize=(12,5))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(short_ma, label='Short MA', color='red')
plt.plot(long_ma, label='Long MA', color='green')
plt.scatter(df.index, df[df['Buy_Signal'] == 1]['Close'], color='green', marker='^', alpha=1)
plt.scatter(df.index, df[df['Sell_Signal'] == -1]['Close'], color='red', marker='v', alpha=1)
plt.title('Stock Price with Buy & Sell Signals')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()
```

This code will plot the stock price, the short and long moving averages, and the buy and sell signals. The green arrows represent the buy signals and the red arrows represent the sell signals.