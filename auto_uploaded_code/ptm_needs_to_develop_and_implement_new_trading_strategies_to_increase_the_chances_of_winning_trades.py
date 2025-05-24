Sure, here's a simple Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is one of the most commonly used strategies in trading. It involves two moving averages, one short period and one long period. When the short period moving average crosses above the long period moving average, it's a signal to buy. When the short period moving average crosses below the long period moving average, it's a signal to sell.

Please note that this is a very basic strategy and may not always result in winning trades. Also, this code assumes that you have historical stock price data in a pandas DataFrame named 'df'.

```python
import pandas as pd
import numpy as np

# Define the moving average periods
short_period = 50
long_period = 200

# Calculate the short period moving average
df['short_mavg'] = df['Close'].rolling(window=short_period, min_periods=1, center=False).mean()

# Calculate the long period moving average
df['long_mavg'] = df['Close'].rolling(window=long_period, min_periods=1, center=False).mean()

# Create a column 'signal' such that if short moving average is greater than long moving average then signal is 1 else 0
df['signal'] = np.where(df['short_mavg'] > df['long_mavg'], 1.0, 0.0)

# Create a column 'positions' which is the difference of the 'signal' column and its shifted version
# This column indicates whether to buy (1), sell (-1), or do nothing (0)
df['positions'] = df['signal'].diff()

# Print the DataFrame
print(df)
```

This code will add two columns to the DataFrame: 'signal' and 'positions'. The 'signal' column will contain 1.0 when the short moving average is greater than the long moving average and 0.0 otherwise. The 'positions' column will contain 1 when a buy signal is generated, -1 when a sell signal is generated, and 0 otherwise.

Please replace 'Close' with the column name in your DataFrame that represents the closing prices of the stock. Also, you may need to adjust the short_period and long_period according to your trading strategy.