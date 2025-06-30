from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code to analyze EMA crossover using pandas library. This code assumes that you have a pandas DataFrame `df` with 'Close' prices of a stock.

```python
import pandas as pd
import numpy as np

# Assuming df is your DataFrame and 'Close' is the column with closing prices

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover(data, short_window, long_window):
    short_ema = calculate_ema(data, short_window)
    long_ema = calculate_ema(data, long_window)
    
    crossover = np.where(short_ema > long_ema, 1, 0)
    crossover_signal = pd.Series(crossover, index=data.index)
    
    return crossover_signal

# Use the function
short_window = 12
long_window = 26
df['EMA_Crossover_Signal'] = ema_crossover(df['Close'], short_window, long_window)
```

This code calculates the EMA (Exponential Moving Average) for a short window and a long window, and then creates a signal when the short EMA crosses above the long EMA (represented as 1). When the short EMA is below the long EMA, the signal is 0. 

Please replace 'Close' with the actual column name in your DataFrame that represents the closing prices. Also, you may want to adjust the short and long window periods according to your trading strategy.

Remember, this is a simple EMA crossover strategy. In real trading scenarios, you may need to consider other factors and indicators as well.