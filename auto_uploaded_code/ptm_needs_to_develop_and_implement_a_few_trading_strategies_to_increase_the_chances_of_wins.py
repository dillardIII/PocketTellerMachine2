Sure, here's a simple example of a Python code for a trading strategy using Moving Average Crossover. This strategy is one of the most commonly used strategies in the trading world. It's based on the principle that when a short-term moving average crosses a long-term moving average, it's a signal to buy or sell.

Please note that this is a simplified example and real-world trading strategies can be much more complex. Also, this example assumes that you have historical stock price data in a pandas DataFrame called `df`.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assuming df is your DataFrame and 'Close' is the column with closing prices

# Calculate short-term simple moving average
short_sma = df['Close'].rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = df['Close'].rolling(window=100).mean()

# Create a column 'Signal' such that if short-term SMA is greater than long-term SMA then Signal is 1 else 0
df['Signal'] = 0.0  
df['Signal'][short_sma > long_sma] = 1.0

# Generate trading orders
df['Position'] = df['Signal'].diff()

# Print the DataFrame
print(df)

# Plotting
plt.figure(figsize=(10,5))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(short_sma, label='Short-term SMA', color='red')
plt.plot(long_sma, label='Long-term SMA', color='green')
plt.plot(df.loc[df.Position == 1.0].index, 
         df.short_sma[df.Position == 1.0],
         '^', markersize=10, color='m', label='buy')
plt.plot(df.loc[df.Position == -1.0].index, 
         df.short_sma[df.Position == -1.0],
         'v', markersize=10, color='k', label='sell')
plt.ylabel('Price')
plt.xlabel('Date')
plt.title('Stock Price with Moving Average Crossover Trading Signals')
plt.legend()
plt.grid()
plt.show()
```

In this code, `short_sma` and `long_sma` are the short-term and long-term simple moving averages respectively. When `short_sma` is greater than `long_sma`, it's a signal to buy (we mark it as 1 in 'Signal' column) and when `short_sma` is less than `long_sma`, it's a signal to sell (we mark it as 0 in 'Signal' column). The 'Position' column is used to mark the points where we need to place buy/sell orders. The points where 'Signal' changes (from 0 to 1 or 1 to 0) are the points where we need to place orders.

Please note that you'll need to replace `df` with your actual DataFrame name and 'Close' with the actual column name that contains the closing prices. Also, you'll need to adjust the window sizes for short-term and long-term SMAs according to your strategy.