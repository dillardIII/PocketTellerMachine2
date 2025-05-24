Sure, here's a simple Python code that implements two basic trading strategies: Moving Average Crossover and Mean Reversion. Please note that this is a simplified version and real-world trading strategies can be much more complex and require thorough backtesting and risk management.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

# Define the stock to be traded
stock = 'AAPL'

# Define the data source
data_source = 'yahoo'

# Define the start and end dates
start_date = '01-01-2020'
end_date = '31-12-2020'

# Get the data
df = web.DataReader(stock, data_source, start_date, end_date)

# Calculate the short-term simple moving average
short_sma = df['Close'].rolling(window=20).mean()

# Calculate the long-term simple moving average
long_sma = df['Close'].rolling(window=100).mean()

# Create a 'Signal' column
df['Signal'] = 0.0
df['Signal'][short_sma > long_sma] = 1.0

# Create a 'Position' column
df['Position'] = df['Signal'].diff()

# Print the DataFrame
print(df)

# Mean Reversion Strategy
# Calculate the mean of the last N days
N = 20
df['Mean'] = df['Close'].rolling(window=N).mean()

# Calculate the standard deviation of the last N days
df['Std'] = df['Close'].rolling(window=N).std()

# Create a 'Buy_Signal' column (we buy the stocks when the current price falls more than a standard deviation below the mean)
df['Buy_Signal'] = df['Close'] < (df['Mean'] - df['Std'])

# Create a 'Sell_Signal' column (we sell the stocks when the current price is more than a standard deviation above the mean)
df['Sell_Signal'] = df['Close'] > (df['Mean'] + df['Std'])

# Print the DataFrame
print(df)
```

This code uses Yahoo Finance as the data source and implements the strategies on Apple Inc. (AAPL) stock. The Moving Average Crossover strategy generates a buy signal when the short-term moving average crosses above the long-term moving average, and a sell signal when the short-term moving average crosses below the long-term moving average. The Mean Reversion strategy assumes that the price will revert to its mean over time, and generates a buy signal when the price falls more than one standard deviation below the mean, and a sell signal when the price rises more than one standard deviation above the mean.

Please note that this code does not take into account transaction costs and slippage, and does not implement any risk management or portfolio optimization techniques. It is intended for educational purposes only and should not be used for real trading without further improvements.