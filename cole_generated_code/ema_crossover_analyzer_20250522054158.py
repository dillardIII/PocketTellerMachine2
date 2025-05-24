Sure, here is a simple Python code to analyze EMA crossover using the pandas library. This code assumes that you have a pandas DataFrame `df` with 'Close' prices of a stock.

```python
import pandas as pd
import numpy as np

# Assuming df is your DataFrame and it has a column 'Close'
# Calculate the EMA for short and long windows
def calculate_ema(df, short_window, long_window):
    short_ema = df['Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = df['Close'].ewm(span=long_window, adjust=False).mean()
    return short_ema, long_ema

# Identify where the crossover happens
def identify_crossovers(df, short_ema, long_ema):
    # Create a column 'Signal' such that if short EMA is greater than long EMA then 1 else 0
    df['Signal'] = np.where(short_ema > long_ema, 1.0, 0.0)
    # Generate trading orders using diff function
    df['Position'] = df['Signal'].diff()
    return df

# Define the short and long windows
short_window = 12
long_window = 26

# Calculate the short and long EMA
short_ema, long_ema = calculate_ema(df, short_window, long_window)

# Identify crossovers
df = identify_crossovers(df, short_ema, long_ema)

# Print the DataFrame
print(df)
```

In this code, the `calculate_ema` function calculates the short and long EMA. The `identify_crossovers` function creates a 'Signal' column that is 1 if the short EMA is greater than the long EMA and 0 otherwise. It also creates a 'Position' column that identifies where the crossover happens. A value of 1 in 'Position' means a buy signal (short EMA crosses above long EMA) and a value of -1 means a sell signal (short EMA crosses below long EMA).

Please replace `df` with your actual DataFrame and make sure that it has a 'Close' column. Adjust the short and long window periods as per your requirements.