To implement and test new trading strategies, we'll need to create a simple backtesting system. Backtesting is the process of testing a trading strategy on relevant historical data to ensure its viability before the trader risks any actual capital. 

Here's a simple Python code to implement and test a simple moving average crossover strategy using Pandas library:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Fetching historical data
def fetch_data(stock, start, end):
    df = pdr.get_data_yahoo(stock, start, end)
    return df

# Implementing the strategy
def implement_strategy(data):
    # Create 50 days simple moving average column
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    
    # Create 200 days simple moving average column
    data['SMA_200'] = data['Close'].rolling(window=200).mean()
    
    # Create a column to hold the buy/sell signals
    data['Buy_Signal'] = np.where(data['SMA_50'] > data['SMA_200'], 1, 0)
    data['Sell_Signal'] = np.where(data['SMA_50'] < data['SMA_200'], -1, 0)
    
    return data

# Testing the strategy
def test_strategy(data):
    data['Daily_Return'] = data['Close'].pct_change()
    data['Strategy_Return'] = data['Daily_Return'] * data['Buy_Signal'].shift()
    return data

# Fetch the data
data = fetch_data('AAPL', '2010-01-01', '2020-12-31')

# Implement the strategy
data = implement_strategy(data)

# Test the strategy
data = test_strategy(data)

# Calculate the cumulative returns
data['Cumulative_Market_Returns'] = np.exp(np.log1p(data['Daily_Return']).cumsum())
data['Cumulative_Strategy_Returns'] = np.exp(np.log1p(data['Strategy_Return']).cumsum())

# Plot the results
plt.figure(figsize=(10,5))
plt.plot(data['Cumulative_Market_Returns'], color='r', label='Market Returns')
plt.plot(data['Cumulative_Strategy_Returns'], color='g', label='Strategy Returns')
plt.legend()
plt.show()
```

This script fetches historical data for Apple Inc. from Yahoo Finance, calculates 50-day and 200-day simple moving averages, generates buy/sell signals based on these averages, and tests the strategy by calculating daily and cumulative returns. Finally, it plots the cumulative market and strategy returns for comparison. 

Please note that this is a simple example and real-world trading strategies can be much more complex. Also, past performance is not indicative of future results.