Sure, here is a simple Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is not guaranteed to increase the number of trades, but it's a start. You can modify it or implement more complex strategies as per your needs.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

# Define the stock to be traded
stock = 'AAPL'

# Define the Moving Averages periods
short_MA = 20
long_MA = 100

# Get the stock data
df = web.DataReader(stock, data_source='yahoo', start='01-01-2010')

# Calculate the Moving Averages
df['Short_MA'] = df['Adj Close'].rolling(window=short_MA).mean()
df['Long_MA'] = df['Adj Close'].rolling(window=long_MA).mean()

# Create a column 'Signal' such that if the Short_MA is greater than Long_MA then buy else sell
df['Signal'] = np.where(df['Short_MA'] > df['Long_MA'], 1, 0)

# Create a column 'Position' which is the difference of the 'Signal' column and then multiply by the 'Adj Close' price to get the daily market value of the position
df['Position'] = df['Signal'].diff() * df['Adj Close']

# Print the DataFrame
print(df)
```

This strategy works by generating a trading signal when a short-term moving average crosses a long-term moving average. When the short-term average is higher than the long-term average, it generates a buy signal, and when the short-term average is lower, it generates a sell signal.

Please note that this is a simplified example and doesn't take into account trading fees, slippage, and other factors that could impact the performance of a trading strategy. Also, it's always recommended to backtest any trading strategy before live trading.