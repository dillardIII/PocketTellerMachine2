from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's an example of how you might implement a simple trading strategy in Python using the pandas library. This strategy is called a moving average crossover, which means that we buy when the short-term moving average crosses above the long-term moving average, and we sell when the short-term moving average crosses below the long-term moving average.

Please note that this is a very basic strategy and in real-world trading, you would need to consider many other factors like transaction costs, slippage, risk management, etc.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assuming we have a DataFrame 'df' with 'Close' prices
df = pd.read_csv('your_data.csv')

# Calculate the short-term moving average
short_window = 10
df['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Calculate the long-term moving average
long_window = 30
df['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create a 'signals' DataFrame with the signal: 1.0 for a long position and -1.0 for a short position
df['signal'] = 0.0
df['signal'][short_window:] = np.where(df['short_mavg'][short_window:] 
                                        > df['long_mavg'][short_window:], 1.0, -1.0)   

# Generate trading orders
df['positions'] = df['signal'].diff()

# Print the DataFrame
print(df)

# Plotting the strategy
plt.figure(figsize=(10,5))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(df['short_mavg'], label='Short Moving Average', color='red')
plt.plot(df['long_mavg'], label='Long Moving Average', color='green')
plt.plot(df.loc[df.positions == 1.0].index, 
         df.short_mavg[df.positions == 1.0],
         '^', markersize=10, color='m', label='buy')
plt.plot(df.loc[df.positions == -1.0].index, 
         df.short_mavg[df.positions == -1.0],
         'v', markersize=10, color='k', label='sell')
plt.ylabel('Price')
plt.xlabel('Date')
plt.legend(loc='best')
plt.grid()
plt.show()
```

This code assumes that you have a CSV file named 'your_data.csv' that contains the closing prices of the stock you're interested in. You'll need to replace 'your_data.csv' with the path to your actual data file.