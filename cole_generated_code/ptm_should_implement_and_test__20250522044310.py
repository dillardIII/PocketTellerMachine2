from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code for implementing a basic trading strategy using Moving Average Crossover. This strategy is not a recommendation for trading, it is just an example of how you might code a strategy.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Download historical data as dataframe
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2021-12-31")

# Calculate short-term simple moving average
ShortEMA = df.Close.ewm(span=12, adjust=False).mean()

# Calculate long-term simple moving average
LongEMA = df.Close.ewm(span=26, adjust=False).mean()

# Create signals based on crossover
df['Buy_Signal'] = np.where(ShortEMA > LongEMA, 1, 0)
df['Sell_Signal'] = np.where(ShortEMA < LongEMA, -1, 0)

# Generate trades
df['Trade'] = df['Buy_Signal'] + df['Sell_Signal']

# Print the dataframe
print(df)
```

This code calculates the short-term and long-term exponential moving averages (EMA) of the closing prices of the Apple Inc. (AAPL) stock. When the short-term EMA is greater than the long-term EMA, it generates a buy signal, and when the short-term EMA is less than the long-term EMA, it generates a sell signal. The 'Trade' column in the dataframe indicates when to buy (1) and sell (-1) the stock.

Please note that this is a very basic trading strategy and may not be profitable. It is recommended to use more advanced strategies and consider other factors such as trading fees and market conditions. Also, always backtest your strategies before live trading.