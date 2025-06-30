from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide you with a simple example of a pair trading strategy using Python. This strategy is a type of statistical arbitrage that is based on the idea that if two stocks are historically correlated, then the relative price movement of one stock can be used to forecast the price movement of the other.

Here is a simple implementation of a pair trading strategy:

```python
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Download historical data for required stocks
tickers = ["AAPL","IBM"]
stock_data = pdr.get_data_yahoo(tickers, start="2019-01-01", end="2021-12-31")['Adj Close']

# Calculate returns
returns = stock_data.pct_change()
mean_daily_returns = returns.mean()
cov_matrix = returns.cov()

# Simulate a large number of possible portfolios
num_portfolios = 25000

# Set up array to hold results
results = np.zeros((3,num_portfolios))

for i in range(num_portfolios):
    # Select random weights for portfolio holdings
    weights = np.random.random(2)
    # Rebalance weights to sum to 1
    weights /= np.sum(weights)
    
    # Calculate portfolio return and volatility
    portfolio_return = np.sum(mean_daily_returns * weights) * 252
    portfolio_std_dev = np.sqrt(np.dot(weights.T,np.dot(cov_matrix, weights))) * np.sqrt(252)
    
    # Store results in results array
    results[0,i] = portfolio_return
    results[1,i] = portfolio_std_dev
    # Store Sharpe Ratio (return / volatility) - risk free rate element excluded for simplicity
    results[2,i] = results[0,i] / results[1,i]

# Convert results array to Pandas DataFrame
results_frame = pd.DataFrame(results.T,columns=['return','stdev','sharpe'])

# Locate position of portfolio with highest Sharpe Ratio
max_sharpe_port = results_frame.iloc[results_frame['sharpe'].idxmax()]

# Locate positon of portfolio with minimum standard deviation
min_vol_port = results_frame.iloc[results_frame['stdev'].idxmin()]

print(max_sharpe_port)
print(min_vol_port)
```

This code will print the portfolio with the maximum Sharpe Ratio and the portfolio with the minimum standard deviation, which represent the most profitable and least risky portfolios respectively. 

Please note that this is a simple example and real trading strategies should consider transaction costs, market impact, and other factors. Also, this example assumes that the returns are normally distributed, which may not be the case in real world.