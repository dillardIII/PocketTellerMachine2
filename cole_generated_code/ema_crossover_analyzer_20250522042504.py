from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can help you with that. Here's a simple Python code that uses the `pandas` library to calculate the Exponential Moving Average (EMA) and analyze the crossover points. 

Please note that this code assumes that you have a pandas DataFrame `df` that contains the price data with 'Close' prices.

```python
import pandas as pd
import numpy as np

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover(data, short_window, long_window):
    short_ema = calculate_ema(data['Close'], short_window)
    long_ema = calculate_ema(data['Close'], long_window)

    data['Short_EMA'] = short_ema
    data['Long_EMA'] = long_ema

    # Create signals
    data['Buy_Signal'] = np.where(short_ema > long_ema, 1, 0)
    data['Sell_Signal'] = np.where(short_ema < long_ema, -1, 0)

    return data

# Assuming df is your DataFrame with 'Close' prices
short_window = 12
long_window = 26

df_with_signals = ema_crossover(df, short_window, long_window)

# Print DataFrame
print(df_with_signals)
```

This code first calculates the short and long EMA for the closing prices. Then it creates two new columns in the DataFrame: 'Buy_Signal' and 'Sell_Signal'. 'Buy_Signal' is 1 when the short EMA is greater than the long EMA (indicating a potential buying point), and 'Sell_Signal' is -1 when the short EMA is less than the long EMA (indicating a potential selling point).

Please replace `df` with your actual DataFrame, and adjust the `short_window` and `long_window` variables as per your needs.