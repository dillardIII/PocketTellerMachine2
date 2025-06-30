from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple Python code that implements a diversification strategy using the Modern Portfolio Theory (MPT). This strategy uses historical returns of different stocks to create a portfolio that maximizes return for a given level of risk.

Please note that this is a simplified example and actual trading strategies would require more complex models and risk management techniques.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define the stocks to include in the portfolio
stocks = ['AAPL', 'MSFT', 'GOOG', 'AMZN']

# Get the stock data
def get_data(stocks):
    stock_data = pd.DataFrame()
    for stock in stocks:
        stock_data[stock] = web.DataReader(stock, data_source='yahoo', start='01-01-2010')['Adj Close']
    return stock_data

# Calculate the returns of the stocks
def calculate_returns(stock_data):
    log_returns = np.log(stock_data / stock_data.shift(1))
    return log_returns

# Define the weights of the stocks
weights = np.array([0.25, 0.25, 0.25, 0.25])

# Calculate the portfolio return
def calculate_portfolio_return(returns, weights):
    portfolio_return = np.sum(returns.mean() * weights) * 250
    return portfolio_return

# Calculate the portfolio variance
def calculate_portfolio_variance(returns, weights):
    portfolio_variance = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 250, weights)))
    return portfolio_variance

# Optimize the portfolio
def optimize_portfolio(returns, weights):
    def check_sum(weights):
        return np.sum(weights) - 1

    constraints = ({'type': 'eq', 'fun': check_sum})
    bounds = tuple((0, 1) for x in range(len(stocks)))
    initial_guess = len(stocks) * [1. / len(stocks),]

    optimized_results = minimize(calculate_portfolio_variance, initial_guess, args=returns, method='SLSQP', bounds=bounds, constraints=constraints)
    return optimized_results

# Get the stock data
stock_data = get_data(stocks)

# Calculate the returns
returns = calculate_returns(stock_data)

# Optimize the portfolio
optimized_results = optimize_portfolio(returns, weights)

# Print the optimized weights
print("Optimized weights: ", optimized_results.x)
```

This code first fetches the historical data for the stocks, then it calculates the log returns of the stocks. It initializes the weights of the stocks equally. Then it calculates the portfolio return and variance. Finally, it optimizes the portfolio to minimize the variance (risk) using the 'SLSQP' method.

The result of the optimization is the weights of the stocks in the portfolio that minimize the risk for a given return. These weights can be used to diversify the portfolio.

Please note that you need to install the `pandas_datareader` and `scipy` libraries to run this code. You can install them using pip:

```
pip install pandas_datareader scipy
```