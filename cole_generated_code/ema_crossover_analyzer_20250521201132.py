Sure, here is a simple Python code using pandas library to analyze EMA crossover. This code assumes that you already have a pandas DataFrame `df` with a 'Close' column for closing prices.

```python
import pandas as pd
import numpy as np

# Assuming df is your DataFrame and 'Close' is the column with closing prices

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover(data, short_window, long_window):
    short_ema = calculate_ema(data, short_window)
    long_ema = calculate_ema(data, long_window)
    
    # Create signals
    data['short_ema'] = short_ema
    data['long_ema'] = long_ema
    data['signal'] = 0.0
    data['signal'][short_ema > long_ema] = 1.0
    data['crossover'] = data['signal'].diff()
    
    return data

# Define the short and long windows
short_window = 12
long_window = 26

# Run EMA crossover analysis
df = ema_crossover(df['Close'], short_window, long_window)

# Print data
print(df)
```

This code will add two columns to the DataFrame: 'signal' and 'crossover'. 'signal' will be 1.0 when the short EMA is above the long EMA and 0.0 otherwise. 'crossover' will indicate the points where the 'signal' changes, i.e., where the EMAs cross each other.

Please replace `df` and `'Close'` with your actual DataFrame and the column name for closing prices. Also, adjust the short and long window periods as per your requirements.