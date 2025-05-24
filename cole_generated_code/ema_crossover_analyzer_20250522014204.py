Sure, here's a simple Python code using pandas library to calculate EMA (Exponential Moving Average) and detect crossover points. This code assumes that you have a pandas DataFrame `df` with 'Close' prices of a stock.

```python
import pandas as pd
import numpy as np

# Assuming df is your DataFrame and 'Close' is the column with closing prices
# Calculate short-term (e.g., 12-day) EMA
short_term_EMA = df['Close'].ewm(span=12, adjust=False).mean()

# Calculate long-term (e.g., 26-day) EMA
long_term_EMA = df['Close'].ewm(span=26, adjust=False).mean()

# Create a DataFrame to store the EMA data
ema_df = pd.DataFrame()
ema_df['Short Term EMA'] = short_term_EMA
ema_df['Long Term EMA'] = long_term_EMA

# Function to detect crossover
def detect_crossover(ema_df):
    # Initialize 'Buy_Signal' and 'Sell_Signal' columns with zeros
    ema_df['Buy_Signal'] = np.zeros(len(ema_df))
    ema_df['Sell_Signal'] = np.zeros(len(ema_df))

    # Generate signals
    for i in range(2, len(ema_df)):
        if ema_df['Short Term EMA'][i] > ema_df['Long Term EMA'][i] and ema_df['Short Term EMA'][i-1] < ema_df['Long Term EMA'][i-1]:
            ema_df['Buy_Signal'][i] = 1
        elif ema_df['Short Term EMA'][i] < ema_df['Long Term EMA'][i] and ema_df['Short Term EMA'][i-1] > ema_df['Long Term EMA'][i-1]:
            ema_df['Sell_Signal'][i] = 1

    return ema_df

# Detect crossover
ema_df = detect_crossover(ema_df)

# Print DataFrame
print(ema_df)
```

This code calculates the 12-day and 26-day EMA of the closing prices, then it detects the crossover points. When the short-term EMA crosses above the long-term EMA, it generates a buy signal. Conversely, when the short-term EMA crosses below the long-term EMA, it generates a sell signal.