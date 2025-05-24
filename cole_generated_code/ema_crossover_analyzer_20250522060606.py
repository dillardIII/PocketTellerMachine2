Sure, I will write a simple Python code using pandas library to calculate the Exponential Moving Averages (EMA) and identify the crossover points. 

Please note that you need to have historical price data in a pandas DataFrame for this code to work. The DataFrame should have a 'Close' column which represents the closing price of the stock.

```python
import pandas as pd
import numpy as np

# Assuming df is your DataFrame and it has a 'Close' column
# df = pd.read_csv('your_file.csv')

def calculate_ema(df, short_span=12, long_span=26):
    df['Short_EMA'] = df.Close.ewm(span=short_span, adjust=False).mean()
    df['Long_EMA'] = df.Close.ewm(span=long_span, adjust=False).mean()
    return df

def identify_crossovers(df):
    # Create an empty column for our signals
    df['Signal'] = 0.0
    # Generate trading signals (1 for buy, -1 for sell)
    df['Signal'][short_span:] = np.where(df['Short_EMA'][short_span:] > df['Long_EMA'][short_span:], 1.0, -1.0)
    # Generate trading orders
    df['Positions'] = df['Signal'].diff()
    return df

short_span = 12
long_span = 26

df = calculate_ema(df, short_span, long_span)
df = identify_crossovers(df)

# Print DataFrame
print(df)
```

In this code, `Short_EMA` and `Long_EMA` are the short term and long term exponential moving averages respectively. The `Signal` column gives the trading signal at each point in time (1 for buy, -1 for sell). The `Positions` column indicates the points where the EMA crossover occurs (1 for crossover from below, -1 for crossover from above).