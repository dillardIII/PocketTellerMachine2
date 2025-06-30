from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a Python code that implements a basic trading strategy. This strategy is based on moving averages, a common indicator used in trading.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

# Define the ticker list
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

# Fetch the data
data = pdr.get_data_yahoo(tickers_list, start="2017-01-01", end="2021-12-31")['Adj Close']

# Print first 5 rows of the data
print(data.head())

# Calculate the 20 days moving averages of the closing prices
short_rolling = data.rolling(window=20).mean()

# Calculate the 200 days moving averages of the closing prices
long_rolling = data.rolling(window=200).mean()

# Create a 'signals' DataFrame with the `sign` of the difference of short and long window
signals = pd.DataFrame(index=data.index)
for t in tickers_list:
    signals[t] = np.where(short_rolling[t] > long_rolling[t], 1.0, 0.0)

# Print `signals`
print(signals)

# Create a portfolio
portfolio = pd.DataFrame(index=data.index)
initial_capital= float(100000.0)

# Create a DataFrame `positions`
positions = pd.DataFrame(index=signals.index).fillna(0.0)

# Buy a 100 shares
for t in tickers_list:
    positions[t] = 100*signals[t]   

# Initialize the portfolio with value owned   
portfolio['holdings'] = (positions.multiply(data, axis=0)).sum(axis=1)

# Store the difference in shares owned 
pos_diff = positions.diff()

# Add `holdings` to portfolio
portfolio['cash'] = initial_capital - (pos_diff.multiply(data, axis=0)).sum(axis=1).cumsum()   

# Add `total` to portfolio
portfolio['total'] = portfolio['cash'] + portfolio['holdings']

# Add `returns` to portfolio
portfolio['returns'] = portfolio['total'].pct_change()

# Print the first lines of `portfolio`
print(portfolio.head())
```

This code fetches the historical data for a list of tickers, calculates the 20-day and 200-day moving averages, and generates trading signals based on these moving averages. It then calculates the portfolio value over time based on these signals. 

Please note that this is a very basic trading strategy and real-world strategies can be much more complex. Also, this code assumes that we can buy fractional shares, which may not be the case in reality. 

Finally, this code does not take into account transaction costs, which can significantly impact the performance of a trading strategy. 

This code also assumes that the trading signals are generated and executed on the same day, which may not be the case in reality. 

Please use this code as a starting point and customize it according to your needs.