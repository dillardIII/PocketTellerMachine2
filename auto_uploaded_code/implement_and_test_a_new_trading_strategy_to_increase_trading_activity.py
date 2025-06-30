from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple trading strategy using Python. This strategy is known as a moving average crossover strategy. It is a basic strategy where a trader buys an asset when its short term moving average crosses above its long term moving average, and sells when the short term moving average crosses below the long term moving average. 

Please note that this is a basic strategy and may not necessarily increase trading activity or profitability. It's always recommended to use more sophisticated strategies and risk management techniques in live trading.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

# Define the assets to be used
assets = ['AAPL']

# Define the data frame
df = pd.DataFrame()

# Fetch the data
for asset in assets:
    df[asset] = web.DataReader(asset, data_source='yahoo', start='01-01-2010')['Adj Close']

# Define the short term and long term moving averages
short_term_avg = df.rolling(window=20).mean()
long_term_avg = df.rolling(window=100).mean()

# Create a signals data frame
signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0

# Generate the trading signals 0 or 1,
# 1 when short term moving average is greater than long term moving average
signals['signal'][short_term_avg > long_term_avg] = 1.0

# Generate the trading orders
signals['positions'] = signals['signal'].diff()

# Print the signals
print(signals)

# Test the strategy with an initial capital
initial_capital = float(100000.0)

# Create a data frame for positions
positions = pd.DataFrame(index=signals.index).fillna(0.0)

# Buy 100 shares
positions[assets] = 100*signals['signal']

# Initialize the portfolio with value owned
portfolio = positions.multiply(df[assets], axis=0)

# Store the difference in shares owned
pos_diff = positions.diff()

# Add holdings to portfolio
portfolio['holdings'] = (positions.multiply(df[assets], axis=0)).sum(axis=1)

# Add cash to portfolio
portfolio['cash'] = initial_capital - (pos_diff.multiply(df[assets], axis=0)).sum(axis=1).cumsum()

# Add total to portfolio
portfolio['total'] = portfolio['cash'] + portfolio['holdings']

# Add returns to portfolio
portfolio['returns'] = portfolio['total'].pct_change()

# Print the portfolio
print(portfolio)
```

This code fetches the historical data for the asset (in this case, Apple Inc.), calculates the short term and long term moving averages, generates trading signals and orders, and tests the strategy with an initial capital. The final portfolio value and returns are also calculated and printed.