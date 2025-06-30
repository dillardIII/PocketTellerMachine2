from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code using the Pandas library to calculate and analyze the EMA crossover.

```python
import pandas as pd
import pandas_datareader as web
import datetime as dt

# Define the start and end date
start = dt.datetime(2020,1,1)
end = dt.datetime.now()

# Load the data
df = web.DataReader('AAPL', 'yahoo', start, end)

# Calculate the short-term EMA
short_EMA = df.Close.ewm(span=12, adjust=False).mean()

# Calculate the long-term EMA
long_EMA = df.Close.ewm(span=26, adjust=False).mean()

# Create signals
df['Buy_Signal'] = short_EMA > long_EMA
df['Sell_Signal'] = short_EMA < long_EMA

# Print the data
print(df)
```

In this code, we first fetch the historical data of the Apple Inc. stock using the Yahoo Finance API. Then, we calculate the short-term (12-day) and long-term (26-day) EMA of the closing prices. If the short-term EMA is greater than the long-term EMA, it is a buy signal, and if the short-term EMA is less than the long-term EMA, it is a sell signal.

Please note that you need to install pandas_datareader library to fetch the data from Yahoo Finance API. You can install it using pip:

```bash
pip install pandas_datareader
```

Also, this is a very basic EMA crossover strategy. In real-world trading, you would need to consider many other factors and use more sophisticated strategies.