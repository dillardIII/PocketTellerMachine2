from ghost_env import INFURA_KEY, VAULT_ADDRESS
To diversify a portfolio, you need to invest in different types of assets such as stocks, bonds, mutual funds, etc. Here is a simple Python code that simulates diversification of a portfolio:

```python
import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

# List of stocks for portfolio
stocks = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

# Empty DataFrame to store closing prices
df = pd.DataFrame()

# Fetch the data
for stock in stocks:
    df[stock] = web.DataReader(stock, data_source='yahoo', start='01-01-2010')['Adj Close']

# Log returns - First the logarithm of the prices is taken and the the difference of consecutive (log) observations
log_returns = np.log(df / df.shift(1))

# Weights of the stocks in the portfolio
weights = np.array([0.25, 0.25, 0.25, 0.25])

# Expected Portfolio Return
port_return = np.sum(log_returns.mean() * weights) * 250

# Expected Portfolio Variance
port_variance = np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 250, weights)))

# Print the portfolio return and variance
print("Expected Portfolio Return: "+ str(round(port_return, 4) * 100) + "%")
print("Expected Portfolio Variance: "+ str(round(port_variance, 4) * 100) + "%")
```

This code fetches the historical data of the stocks, calculates the log returns, and then calculates the expected portfolio return and variance. The weights of the stocks in the portfolio are assumed to be equal. You can adjust the weights based on your investment strategy.

Please note that this is a very simplified example. In reality, portfolio diversification involves more complex strategies and risk management techniques. Also, this code does not take into account transaction costs, tax implications, etc.