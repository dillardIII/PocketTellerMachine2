from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code for a trading strategy using Moving Average Crossover. This strategy is based on two moving averages, a "fast" and a "slow" moving average. When the fast moving average crosses above the slow moving average, it's a signal to buy. When it crosses below, it's a signal to sell.

This is a simple strategy and doesn't take into account many factors that could influence trading decisions in real-world scenarios. Please note that this is a simulation and should not be used for real trading without proper adjustments and strategy validation.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the lookback periods for the fast and slow moving averages
fast_period = 10
slow_period = 50

# Get the stock data
df = web.DataReader(stock, data_source='yahoo', start='01-01-2010')

# Calculate the fast and slow moving averages
df['Fast_MA'] = df['Close'].rolling(window=fast_period).mean()
df['Slow_MA'] = df['Close'].rolling(window=slow_period).mean()

# Create a column for the trading signals
df['Buy_Signal'] = np.where(df['Fast_MA'] > df['Slow_MA'], 1, 0)
df['Sell_Signal'] = np.where(df['Fast_MA'] < df['Slow_MA'], -1, 0)

# Combine the signals
df['Signal'] = df['Buy_Signal'] + df['Sell_Signal']

# Plot the stock close price and the moving averages
plt.figure(figsize=(12,5))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(df['Fast_MA'], label='Fast MA', color='red')
plt.plot(df['Slow_MA'], label='Slow MA', color='green')
plt.title('Stock Price with Moving Averages')
plt.legend()
plt.show()

# Print the DataFrame
print(df)
```

This code will print a DataFrame with the stock close prices, the fast and slow moving averages, and the trading signals. It will also plot the stock close price and the moving averages.