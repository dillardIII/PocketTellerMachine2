from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that uses the `pandas` library to calculate the Exponential Moving Average (EMA) and analyze the crossover points. This code assumes that you have a pandas DataFrame `df` with a 'Close' column for closing prices.

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

# Assuming df is your DataFrame and 'Close' is your column with closing prices
df['Short_EMA'] = calculate_ema(df['Close'], 12) # Short term EMA
df['Long_EMA'] = calculate_ema(df['Close'], 26) # Long term EMA

df['Crossover'] = ema_crossover(df['Close'], 12, 26)

# Print DataFrame
print(df)
```

This code will add two new columns to the DataFrame: 'Short_EMA' and 'Long_EMA' for the short-term and long-term EMA respectively. It will also add a 'Crossover' column which will contain 1 for points where the short EMA crosses above the long EMA (bullish signal), -1 where the short EMA crosses below the long EMA (bearish signal), and 0 elsewhere.

Please ensure to adjust the short and long window parameters as per your requirements. Also, you would need to handle the trading signals (1 and -1) as per your trading strategy.