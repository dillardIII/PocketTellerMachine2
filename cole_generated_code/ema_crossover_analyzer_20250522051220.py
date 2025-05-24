Sure, here's a simple Python code that uses the `pandas` library to calculate the Exponential Moving Average (EMA) and analyze the crossover points. This code assumes that you have a pandas DataFrame `df` with a 'Close' column for the closing prices.

```python
import pandas as pd
import numpy as np

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover(data, short_window, long_window):
    short_ema = calculate_ema(data, short_window)
    long_ema = calculate_ema(data, long_window)

    buy_signals = (short_ema > long_ema) & (short_ema.shift() < long_ema.shift())
    sell_signals = (short_ema < long_ema) & (short_ema.shift() > long_ema.shift())

    return buy_signals, sell_signals

# Assuming df is your DataFrame and 'Close' is your column with closing prices
df['Short_EMA'] = calculate_ema(df['Close'], 12)  # Short term EMA
df['Long_EMA'] = calculate_ema(df['Close'], 26)  # Long term EMA

df['Buy_Signal'], df['Sell_Signal'] = ema_crossover(df['Close'], 12, 26)

print(df)
```

This code will add four new columns to your DataFrame: 'Short_EMA' and 'Long_EMA' for the short-term and long-term EMA, and 'Buy_Signal' and 'Sell_Signal' for the points where the short-term EMA crosses above or below the long-term EMA, respectively.

Please note that you need to replace the 'Close' string with the name of your column that contains the closing prices. Also, you may want to adjust the window sizes for the short-term and long-term EMA according to your needs.