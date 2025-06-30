from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop and implement new trading strategies, we need to have a clear understanding of the market data. Here is a simple Python code that uses a basic moving average crossover strategy for trading. This is a simple strategy where we buy when the short term moving average crosses above the long term moving average and sell when the short term moving average crosses below the long term moving average.

Please note that this is a very basic strategy and may not be profitable in real trading. It is just an example to show how a trading strategy can be coded in Python. 

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Fetching the historical data
df = pdr.get_data_yahoo('AAPL', '2020-01-01', '2021-12-31')

# Calculating the short term and long term moving averages
df['Short_Term_MA'] = df['Close'].rolling(window=20).mean()
df['Long_Term_MA'] = df['Close'].rolling(window=50).mean()

# Creating a column 'Signal' such that if Short_Term_MA > Long_Term_MA then Signal = 1 else 0
df['Signal'] = 0.0  
df['Signal'][df['Short_Term_MA'] > df['Long_Term_MA']] = 1.0

# Creating a column 'Position' which is the difference of present and previous day 'Signal'
df['Position'] = df['Signal'].diff()

# Print the DataFrame
print(df)

# Now, Position = 1.0 means buy and Position = -1.0 means sell. This is your trading strategy.
```

This code fetches the historical data of Apple Inc. from Yahoo Finance, calculates the short term (20 days) and long term (50 days) moving averages of the closing prices, generates a trading signal based on the comparison of these two moving averages, and finally determines the trading positions based on the change in trading signals.

Remember, this is a very simple strategy and in real trading, you need to consider transaction costs, risk management, portfolio diversification, and many other factors. Also, you need to backtest your strategy on historical data before live trading.