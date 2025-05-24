In order to implement and test new trading strategies, we first need to define what kind of strategies we want to test. For simplicity, let's assume we want to test a simple moving average crossover strategy. This strategy buys when the short-term moving average crosses above the long-term moving average, and sells when the short-term moving average crosses below the long-term moving average.

Here's a simple Python code using pandas library to implement this strategy:

```python
import pandas as pd
import numpy as np

# Assuming we have a DataFrame 'df' with 'Close' prices
df = pd.read_csv('your_data.csv')

# Define the short and long windows
short_window = 40
long_window = 100

# Initialize the 'signals' DataFrame with the 'signal' column
df['signal'] = 0.0

# Create short simple moving average over the short window
df['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
df['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
df['signal'][short_window:] = np.where(df['short_mavg'][short_window:] 
                                        > df['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
df['positions'] = df['signal'].diff()

# Print DataFrame
print(df)
```

This code will output a DataFrame with 'positions' column where 1.0 means 'buy' and -1.0 means 'sell'. You can then use this information to place your trades.

Please note that this is a very simplistic strategy and is unlikely to be profitable without further refinement. It's important to backtest any strategy thoroughly before live trading. Also, this code assumes that you have a CSV file 'your_data.csv' containing the 'Close' prices of the asset you're trading.