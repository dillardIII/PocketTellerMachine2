Creating a python code for trading strategies involves numerous steps, this can get quite complex as you need more specifics, like what kind of strategies will be used etc. However, I'll provide you with a simple illustrative example of a Mean Reversion strategy which uses the concept that the price will revert to its mean over time. Here it is:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data

# Define the instruments to download
tickers = ['AAPL']

# Define which online source to use
data_source = 'yahoo'

# We would like five years of historical data
start_date = '2015-01-01'
end_date = '2020-12-31'

# Use pandas_datareader.data.DataReader to load the desired data
df = data.DataReader(tickers, data_source, start_date, end_date)

# Compute the mean price
df['Mean'] = df['Adj Close'].rolling(window=30).mean() 

# Create a "Buy Signal" when price is below the mean minus one standard deviation
df['Buy_Signal'] = np.where(df['Adj Close'] < (df['Mean'] - df['Adj Close'].rolling(window=30).std()), 1, 0)

# Create a "Sell Signal" when price is above the mean plus one standard deviation
df['Sell_Signal'] = np.where(df['Adj Close'] > (df['Mean'] + df['Adj Close'].rolling(window=30).std()), -1, 0)

# Create a "Strategy" which says when to buy or sell
df['Strategy'] = df['Buy_Signal'] + df['Sell_Signal']

# Print the DataFrame
print(df)
```

In this example, we used the Yahoo Finance API to get the historical data of AAPL stock. Our trading strategy is to buy when the price falls below one standard deviation from the mean and sell when it rises above one standard deviation from the mean. The default window size for rolling mean and standard deviation computations is set to 30 days.