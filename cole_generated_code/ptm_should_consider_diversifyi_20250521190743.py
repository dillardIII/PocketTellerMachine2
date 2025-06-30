from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python script that could be used to diversify a portfolio. This script uses the yfinance library to download stock data and the pandas library to manipulate the data.

Please note that this is a very basic example and real portfolio diversification involves much more complex analysis and decision making.

```python
import yfinance as yf
import pandas as pd

# List of stocks to consider for diversification
stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB']

# Download historical market data
data = yf.download(stocks, start="2020-01-01", end="2022-12-31")

# Use only Close price for each stock
data = data['Close']

# Calculate the daily returns
returns = data.pct_change()

# Calculate the mean daily return and covariance of daily returns
mean_daily_returns = returns.mean()
cov_matrix = returns.cov()

# Set the number of runs of random portfolio weights
num_portfolios = 25000

# Set up an array to hold results
results = np.zeros((3,num_portfolios))

for i in range(num_portfolios):
    # Select random weights for portfolio holdings
    weights = np.random.random(5)
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

print("The portfolio for maximum return is:")
print(max_sharpe_port)

print("The portfolio for minimum volatility is:")
print(min_vol_port)
```

This script generates a number of random portfolios with different weights of the specified stocks, calculates the returns and volatility for each portfolio, and then identifies the portfolios with the highest Sharpe ratio (return/volatility) and the lowest volatility. 

Please note that this script does not actually execute any trades, it just provides an analysis based on historical data. You would need to implement additional functionality to execute trades based on this analysis.