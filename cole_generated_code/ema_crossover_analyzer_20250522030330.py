from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a basic example of an EMA Crossover Analyzer using Python and the pandas library. This code assumes that you have a pandas DataFrame 'df' with 'Close' prices of a stock.

```python
import pandas as pd
import numpy as np

# Assuming df is your DataFrame and 'Close' is the column with closing prices

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover(data, short_window, long_window):
    # Calculate short and long EMA
    short_ema = calculate_ema(data, short_window)
    long_ema = calculate_ema(data, long_window)

    # Create signals
    data['short_ema'] = short_ema
    data['long_ema'] = long_ema
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(short_ema[short_window:] > long_ema[short_window:], 1.0, 0.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

    return data

# Define short and long windows
short_window = 12
long_window = 26

# Run EMA Crossover analyzer
df = ema_crossover(df['Close'], short_window, long_window)
```

This code will add 'short_ema', 'long_ema', 'signal', and 'positions' columns to your DataFrame. 'signal' column will contain 1.0 when the short EMA is above the long EMA (indicating to buy) and 0.0 otherwise (indicating to sell). 'positions' column will contain 1.0 for buying, -1.0 for selling, and 0.0 for holding.

Please note that you need to handle the trading orders based on the 'positions' column according to your trading strategy.