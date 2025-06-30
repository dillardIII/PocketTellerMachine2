from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can help with that. Here's a basic implementation of an EMA Crossover Analyzer using Python and the pandas library. This code assumes you have a pandas DataFrame `df` with a 'Close' column for closing prices.

```python
import pandas as pd
import numpy as np

# Define EMA periods
short_period = 12
long_period = 26

# Calculate short-term EMA
df['Short_EMA'] = df['Close'].ewm(span=short_period, adjust=False).mean()

# Calculate long-term EMA
df['Long_EMA'] = df['Close'].ewm(span=long_period, adjust=False).mean()

# Create column for EMA crossover
df['EMA_Crossover'] = df['Short_EMA'] - df['Long_EMA']

# Function to determine when crossover occurs
def ema_crossover(df):
    Buy_Signal = []
    Sell_Signal = []
    
    for i in range(len(df)):
        if df['EMA_Crossover'][i] > 0:
            Buy_Signal.append(np.nan)
            if df['EMA_Crossover'][i-1] < 0:
                Sell_Signal.append(df['Close'][i])
            else:
                Sell_Signal.append(np.nan)
        elif df['EMA_Crossover'][i] < 0:
            Sell_Signal.append(np.nan)
            if df['EMA_Crossover'][i-1] > 0:
                Buy_Signal.append(df['Close'][i])
            else:
                Buy_Signal.append(np.nan)
        else:
            Buy_Signal.append(np.nan)
            Sell_Signal.append(np.nan)
            
    return (Buy_Signal, Sell_Signal)

# Apply function to df
df['Buy_Signal_Price'], df['Sell_Signal_Price'] = ema_crossover(df)

print(df)
```

This code will add two new columns to your DataFrame: 'Buy_Signal_Price' and 'Sell_Signal_Price'. These columns will contain the closing price at the time of each EMA crossover. A buy signal is generated when the short-term EMA crosses above the long-term EMA, and a sell signal is generated when the short-term EMA crosses below the long-term EMA.