from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple Python code that uses the `pandas` library to calculate the Exponential Moving Average (EMA) and identify crossover points. This code assumes that you have a `pandas` DataFrame `df` with a 'Close' column for closing prices.

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

    # Create column to hold the Buy/Sell signals
    data['Buy_Signal'] = np.where(short_ema > long_ema, 1, 0)
    data['Sell_Signal'] = np.where(short_ema < long_ema, -1, 0)

    return data

# Assume df is your DataFrame with 'Close' prices
df = pd.DataFrame({
    'Close': [1,2,3,4,5,6,7,8,9,10]
})

# Call the function with short_window=2 and long_window=3
df = ema_crossover(df, 2, 3)

print(df)
```

This code will add 'Short_EMA' and 'Long_EMA' columns to your DataFrame, as well as 'Buy_Signal' and 'Sell_Signal' columns. A 'Buy_Signal' of 1 means the short EMA is above the long EMA (bullish signal), and a 'Sell_Signal' of -1 means the short EMA is below the long EMA (bearish signal). 

Please replace the DataFrame `df` with your actual data. Also, adjust the `short_window` and `long_window` parameters as per your requirements.