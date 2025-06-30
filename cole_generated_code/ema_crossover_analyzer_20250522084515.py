from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that uses the `pandas` library to calculate the Exponential Moving Average (EMA) and analyze the crossover points. This code assumes that you have a DataFrame `df` with a 'Close' column for closing prices.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your DataFrame and 'Close' is the column with closing prices
# Calculate short-term (e.g., 12 periods) EMA
short_ema = df['Close'].ewm(span=12, adjust=False).mean()

# Calculate long-term (e.g., 26 periods) EMA
long_ema = df['Close'].ewm(span=26, adjust=False).mean()

# Create a column for the signal
df['Signal'] = 0.0
df['Signal'][short_ema > long_ema] = 1.0
df['Signal'][short_ema < long_ema] = -1.0

# Create a column for positions
df['Position'] = df['Signal'].diff()

# Print the DataFrame
print(df)

# Plot EMA and signals
plt.figure(figsize=(12,5))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(short_ema, label='Short EMA', color='red')
plt.plot(long_ema, label='Long EMA', color='green')
plt.plot(df[df['Position'] == 1].index, df['Close'][df['Position'] == 1], '^', markersize=10, color='m')
plt.plot(df[df['Position'] == -1].index, df['Close'][df['Position'] == -1], 'v', markersize=10, color='k')
plt.ylabel('Price')
plt.xlabel('Date')
plt.legend(loc='best')
plt.grid()
plt.show()
```

This code will plot the closing prices, the short-term EMA, and the long-term EMA. It will also mark the points where the EMA crossover occurs. A pink upward-pointing triangle indicates a point where the short-term EMA crosses above the long-term EMA (a potential buy signal), and a black downward-pointing triangle indicates a point where the short-term EMA crosses below the long-term EMA (a potential sell signal).

Please note that you need to replace the 'Close' with the actual column name in your DataFrame that contains the closing prices. Also, you might need to adjust the span parameters in the `ewm()` function calls to match the periods you want to use for the short-term and long-term EMAs.