Sure, here is a simple Python code that simulates a trade initiation. In this example, I'll use the `yfinance` package to fetch stock data and `pandas` to handle the data. Please note that this is a very basic example and real trading involves more complex strategies and risk management.

```python
import yfinance as yf
import pandas as pd

# Define the stock to trade
stock = 'AAPL'

# Fetch the stock data
data = yf.download(stock, start='2021-01-01', end='2021-12-31')

# Define a simple strategy: If the closing price of the stock is higher than the opening price, then buy 1 share at the next opening price.
data['Buy'] = (data['Close'] > data['Open']).shift()

# Calculate the number of shares to buy
data['Shares'] = data['Buy'].cumsum()

# Calculate the cost of the trades
data['Cost'] = - (data['Open'] * data['Shares']).diff()

# Calculate the value of the portfolio
data['Portfolio Value'] = data['Shares'] * data['Close']

# Calculate the cash left in the portfolio
data['Cash'] = data['Cost'].cumsum()

# Calculate the total value of the portfolio
data['Total'] = data['Cash'] + data['Portfolio Value']

# Print the final portfolio value
print('Final portfolio value:', data['Total'].iloc[-1])
```

This code will print the final value of the portfolio, which can be used to evaluate the effectiveness of the strategy. If the final portfolio value is higher than the initial cash, then the strategy can be considered effective. However, please note that past performance is not indicative of future results.