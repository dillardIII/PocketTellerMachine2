from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple example of a mean reversion trading strategy implemented in Python. This strategy assumes that the price of a stock will revert to its mean over time. If the price is below the mean, it will rise, and if it's above the mean, it will fall.

Please note that this is a simplified example and real-world trading strategies are much more complex and require rigorous backtesting and risk management.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the stock symbol
symbol = 'AAPL'

# Fetch the data
df = pdr.get_data_yahoo(symbol, start="2020-01-01", end="2022-12-31")

# Calculate the mean and standard deviation of the stock price
df['Mean'] = df['Close'].rolling(window=20).mean()
df['Std'] = df['Close'].rolling(window=20).std()

# Define the upper and lower Bollinger Bands
df['Upper'] = df['Mean'] + (df['Std'] * 2)
df['Lower'] = df['Mean'] - (df['Std'] * 2)

# Create a column to hold the trading signals
df['Signal'] = 0.0

# Generate trading signals based on the Bollinger Bands
df['Signal'][df['Close'] > df['Upper']] = -1.0
df['Signal'][df['Close'] < df['Lower']] = 1.0

# Calculate daily returns
df['Return'] = df['Close'].pct_change()

# Calculate strategy returns
df['Strategy_Return'] = df['Return'] * df['Signal'].shift()

# Drop the NaN values
df.dropna(inplace=True)

# Print the DataFrame
print(df)
```

This script fetches the historical price data for a specified stock symbol using the Yahoo Finance API, calculates the mean and standard deviation of the stock price over a 20-day rolling window, and generates trading signals based on the Bollinger Bands. If the stock price is above the upper band, it generates a sell signal (-1.0), and if it's below the lower band, it generates a buy signal (1.0). It then calculates the daily returns and the strategy returns, which are the product of the daily returns and the shifted trading signals.