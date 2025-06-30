from ghost_env import INFURA_KEY, VAULT_ADDRESS
To accomplish the task, we need to have some data to work with. I'll assume that we have a pandas DataFrame `df` with a 'Close' column for closing prices. We'll calculate two EMAs (Exponential Moving Averages), one short (e.g., 12 periods) and one long (e.g., 26 periods). When the short EMA crosses above the long EMA, it's a bullish signal (buy), and when it crosses below, it's a bearish signal (sell). 

Here is the Python code:

```python
import pandas as pd
import numpy as np

# Assuming df is your DataFrame and it has a 'Close' column

# Calculate short and long EMA
df['short_EMA'] = df['Close'].ewm(span=12, adjust=False).mean()
df['long_EMA'] = df['Close'].ewm(span=26, adjust=False).mean()

# Create a column to hold the buy (1) and sell (-1) signals
df['signal'] = 0
df['signal'][df['short_EMA'] > df['long_EMA']] = 1
df['signal'][df['short_EMA'] < df['long_EMA']] = -1

# Create a column to hold the crossover points
df['crossover'] = df['signal'].diff()

# Print the DataFrame
print(df)
```

This code will add two columns to the DataFrame: 'signal' and 'crossover'. The 'signal' column will contain 1 when the short EMA is above the long EMA (indicating a buy signal) and -1 when it's below (indicating a sell signal). The 'crossover' column will contain the points where the signal changes (i.e., where the EMAs cross each other).

Please note that this is a very simplistic strategy and should not be used for real trading without further enhancements and testing.