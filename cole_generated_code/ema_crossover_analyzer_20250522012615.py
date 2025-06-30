from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code using the `pandas` library to analyze EMA (Exponential Moving Average) crossovers. This code assumes that you have a `pandas DataFrame` called `df` with a `Close` column for closing prices.

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

    data['Buy_Signal'] = np.where(short_ema > long_ema, 1, 0)
    data['Sell_Signal'] = np.where(short_ema < long_ema, -1, 0)

    return data

# Assuming df is your DataFrame and it has a 'Close' column
df = ema_crossover(df, 12, 26)
```

In this code, `calculate_ema` function calculates the EMA for a given window. `ema_crossover` function calculates short term and long term EMA and adds them to the DataFrame. It also adds 'Buy_Signal' and 'Sell_Signal' columns to the DataFrame. 'Buy_Signal' is 1 when short term EMA is greater than long term EMA and 'Sell_Signal' is -1 when short term EMA is less than long term EMA.

Please replace `df` with your actual DataFrame and adjust the short and long window parameters as per your requirements. Also, please make sure that your DataFrame has a 'Close' column with closing prices.