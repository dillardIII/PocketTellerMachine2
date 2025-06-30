from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can help you with that. Here's a simple Python code for EMA Crossover Analyzer using pandas library. This code assumes that you have a pandas DataFrame `df` with 'Close' prices of the stock.

```python
import pandas as pd
import numpy as np

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover(data, short_window, long_window):
    short_ema = calculate_ema(data, short_window)
    long_ema = calculate_ema(data, long_window)

    crossover_points = np.where(short_ema > long_ema, 1, 0)
    crossover_points = np.where(short_ema < long_ema, -1, crossover_points)

    return crossover_points

# Assuming df is your DataFrame and 'Close' is the column with closing prices
df['Short_EMA'] = calculate_ema(df['Close'], 12) # Short term EMA
df['Long_EMA'] = calculate_ema(df['Close'], 26) # Long term EMA

df['Crossover'] = ema_crossover(df['Close'], 12, 26)

print(df)
```

In this code, `calculate_ema` function calculates the Exponential Moving Average (EMA) for a given data with a specified window size. `ema_crossover` function calculates the crossover points. When short EMA is greater than long EMA, it's a positive crossover (indicated with 1) and when short EMA is less than long EMA, it's a negative crossover (indicated with -1).

Please replace 'Close', 12, and 26 with your actual column name and window sizes for short term and long term EMAs.