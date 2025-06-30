from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide you with a simple example of a Python code for a basic trading strategy. This strategy is based on Moving Average Crossover, which is a popular strategy used in algorithmic trading.

Please note that this is a very basic strategy and might not be profitable in real-world trading. Also, this code assumes that you have historical stock price data in a pandas DataFrame.

```python
import pandas as pd
import numpy as np

# Assuming df is your DataFrame and 'Close' is the column with closing prices

# Calculate the short-term simple moving average
short_sma = df['Close'].rolling(window=20).mean()

# Calculate the long-term simple moving average
long_sma = df['Close'].rolling(window=100).mean()

# Create a column in the DataFrame to hold the buy/sell signals
df['signal'] = 0.0

# Generate trading signals based on the crossover strategy
df['signal'][20:] = np.where(short_sma[20:] > long_sma[20:], 1.0, 0.0)

# Calculate daily portfolio returns
df['positions'] = df['signal'].diff()

# Print the DataFrame
print(df)
```

In this strategy, a buy signal is generated when the short-term moving average crosses above the long-term moving average, and a sell signal is generated when the short-term moving average crosses below the long-term moving average.

Please remember that this is a very simplistic strategy and in real-world trading, you would need to consider many other factors like transaction costs, slippage, risk management, etc. Also, you would need to backtest your strategy on historical data before live trading.