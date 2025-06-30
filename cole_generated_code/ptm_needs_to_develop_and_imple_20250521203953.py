from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a Python code for a trading strategy using moving averages. The strategy is to buy when the short term moving average crosses above the long term moving average and sell when the short term moving average crosses below the long term moving average.

Please note that this is a very basic strategy and should be used for educational purposes only. Real-world trading strategies are much more complex and take into account many other factors.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2022-12-31')

# Calculate short-term and long-term moving averages
short_term = 50
long_term = 200
data['Short_MA'] = data['Close'].rolling(window=short_term).mean()
data['Long_MA'] = data['Close'].rolling(window=long_term).mean()

# Create a 'Signal' column
data['Signal'] = 0.0  
data['Signal'][short_term:] = np.where(data['Short_MA'][short_term:] > data['Long_MA'][short_term:], 1.0, 0.0)

# Generate trading orders
data['Position'] = data['Signal'].diff()

# Print data
print(data)

# Create buy and sell signals
buy_signals = data[data['Position'] == 1]
sell_signals = data[data['Position'] == -1]

print('Buy Signals:')
print(buy_signals)
print('Sell Signals:')
print(sell_signals)
```

This script downloads historical data for the desired ticker symbol, calculates short-term and long-term moving averages, generates a signal when these averages cross, and then generates trading orders based on these signals. The buy and sell signals are then printed out.