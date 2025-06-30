from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code for a trading strategy using Moving Average Crossover. This strategy is one of the most commonly used strategies in trading. It involves two moving averages, one short period and one long period. When the short period moving average crosses above the long period moving average, it indicates a buy signal. Conversely, when the short period moving average crosses below the long period moving average, it indicates a sell signal.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

# Define the stock to be used
stock = 'AAPL'

# Define the data range
start_date = '01/01/2010'
end_date = '01/01/2022'

# Load the data from web
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short-term simple moving average (SMA)
short_sma = 50
df['ShortSMA'] = df['Adj Close'].rolling(window=short_sma).mean()

# Calculate the long-term simple moving average (SMA)
long_sma = 200
df['LongSMA'] = df['Adj Close'].rolling(window=long_sma).mean()

# Create a column 'Signal' such that if ShortSMA > LongSMA then Signal = 1 else Signal = 0
df['Signal'] = 0.0  
df['Signal'][short_sma:] = np.where(df['ShortSMA'][short_sma:] > df['LongSMA'][short_sma:], 1.0, 0.0)   

# Generate trading orders
df['Position'] = df['Signal'].diff()

# Print the DataFrame
print(df)
```

This script will print a DataFrame that includes the adjusted close price, the short-term SMA, the long-term SMA, the signal (1 for buy, 0 for sell), and the position (1 for buy, -1 for sell, 0 for hold).

Please note that this is a very basic trading strategy and doesn't take into account other factors that could influence the decision to buy or sell a stock. It's always recommended to use more complex strategies and to backtest them with historical data before using them in a live trading environment.