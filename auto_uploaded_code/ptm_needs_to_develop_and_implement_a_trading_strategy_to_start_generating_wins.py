Here is a simple Python code to implement a basic trading strategy using moving averages. This strategy is not guaranteed to generate wins, but it is a common starting point for developing more complex strategies. 

This code assumes that you have historical price data in a pandas DataFrame called `df` with 'Close' prices. It calculates the short-term (50 days) and long-term (200 days) moving averages, and generates 'Buy' signals when the short-term average crosses above the long-term average, and 'Sell' signals when it crosses below.

Please note that this is a very simplified strategy and real-world trading involves many other factors.

```python
import pandas as pd
import numpy as np

# Assuming df is your DataFrame and it has a 'Close' column with prices
df['MA50'] = df['Close'].rolling(50).mean()
df['MA200'] = df['Close'].rolling(200).mean()

# Create a column for Buy/Sell signals
df['Buy_Signal'] = np.where(df['MA50'] > df['MA200'], 1, 0)
df['Sell_Signal'] = np.where(df['MA50'] < df['MA200'], -1, 0)

# Generate trading orders
df['Trade'] = df['Buy_Signal'] + df['Sell_Signal']

# Print the DataFrame
print(df)
```

In this code, a 'Buy' signal is represented by 1, a 'Sell' signal is represented by -1, and no action is represented by 0 in the 'Trade' column.

This is a very basic strategy and should be used for educational purposes only. Always consult with a financial advisor before making trading decisions.