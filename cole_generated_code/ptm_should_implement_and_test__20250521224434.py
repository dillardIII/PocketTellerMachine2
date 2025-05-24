Sure, I can provide you with a simple Python code for a basic trading strategy. However, please note that this is a very simplified version of what a real trading strategy might look like. 

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', 'SPY']

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2000-01-01'
end_date = '2016-12-31'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = pdr.get_data_yahoo(tickers, start_date, end_date)

# Getting just the adjusted closing prices. This will return a Pandas DataFrame
# The index in this DataFrame is the major index of the panel_data.
close = panel_data['Adj Close']

# Getting all weekdays between 01/01/2000 and 12/31/2016
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# How do we align the existing prices in adj_close with our new set of dates?
# All we need to do is reindex close using all_weekdays as the new index
close = close.reindex(all_weekdays)

# Reindexing will insert missing values (NaN) for the dates that were not present
# in the original set. To cope with this, we can fill the missing by replacing them
# with the latest available price for each instrument.
close = close.fillna(method='ffill')

print(close.head(10))

# Define the strategy: buy if the stock price is 2% less than the previous day, sell if the stock price is 2% more than the previous day
def implement_strategy(prices):
    buy_price = 0
    sell_price = 0
    transactions = []
    for i in range(1, len(prices)):
        if prices[i] < prices[i-1]*0.98:
            buy_price = prices[i]
            transactions.append(('buy', i, buy_price))
        elif prices[i] > prices[i-1]*1.02:
            sell_price = prices[i]
            transactions.append(('sell', i, sell_price))
    return transactions

# Implement the strategy for each stock
for ticker in tickers:
    print(f"Transactions for {ticker}:")
    transactions = implement_strategy(close[ticker])
    for transaction in transactions:
        print(transaction)
```

This strategy is very simple and doesn't take into account transaction costs or other important factors that should be considered in a real trading strategy. It's just an example to illustrate how you could implement a trading strategy in Python.