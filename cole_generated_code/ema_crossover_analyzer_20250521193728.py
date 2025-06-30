from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code using pandas library to analyze EMA crossover:

```python
import pandas as pd
import pandas_datareader as web
import datetime as dt

# Define the stock and the period
stock = 'AAPL'
start = dt.datetime(2020,1,1)
end = dt.datetime.now()

# Fetch the data
data = web.DataReader(stock, 'yahoo', start, end)

# Calculate the short-term and long-term EMA
short_EMA = data.Close.ewm(span=12, adjust=False).mean()
long_EMA = data.Close.ewm(span=26, adjust=False).mean()

# Create signals
data['Buy_Signal'] = (short_EMA > long_EMA)
data['Sell_Signal'] = (short_EMA < long_EMA)

# Print the data
print(data)
```

This script fetches the data for a specified stock (in this case, Apple) from Yahoo Finance, calculates the short-term (12-day) and long-term (26-day) Exponential Moving Average (EMA), and creates a buy signal when the short-term EMA is above the long-term EMA, and a sell signal when the short-term EMA is below the long-term EMA.

Please note that you need to install pandas_datareader library to fetch the data from Yahoo Finance. You can install it using pip:

```python
pip install pandas_datareader
```

Also, this is a very basic EMA crossover strategy and may not be profitable in real trading. You should consider other factors and use more sophisticated strategies for real trading.