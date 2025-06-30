from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple implementation of an EMA Crossover Analyzer using Python and the pandas library. This code assumes that you have a pandas DataFrame `df` with a 'Close' column for closing prices.

```python
import pandas as pd
import numpy as np

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover_analyzer(df, short_window, long_window):
    # Calculate short and long EMA
    short_ema = calculate_ema(df['Close'], short_window)
    long_ema = calculate_ema(df['Close'], long_window)

    # Create signals
    df['short_ema'] = short_ema
    df['long_ema'] = long_ema
    df['signal'] = np.where(short_ema > long_ema, 1.0, 0.0)
    df['crossover'] = df['signal'].diff()

    return df

# Use the function
df = ema_crossover_analyzer(df, short_window=12, long_window=26)
```

This code will add four new columns to the DataFrame:

- `short_ema`: The short-term EMA.
- `long_ema`: The long-term EMA.
- `signal`: 1.0 when the short EMA is above the long EMA (indicating a bullish signal), and 0.0 otherwise.
- `crossover`: Indicates when a crossover occurs. A value of 1.0 means a bullish crossover (the short EMA has moved above the long EMA), and a value of -1.0 means a bearish crossover (the short EMA has moved below the long EMA).

Please replace `df` with your actual DataFrame and adjust the short and long window parameters as per your requirements.