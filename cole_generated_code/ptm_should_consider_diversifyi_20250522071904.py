Sure, here is a simple Python code that uses the Modern Portfolio Theory (MPT) to diversify a portfolio. This code uses the pandas and yfinance libraries to get historical data, numpy to perform numerical calculations, and matplotlib to plot the efficient frontier.

Please note that this is a simple example and real portfolio diversification involves more complex analysis and considerations.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Define the stocks to be used for diversification
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB']

# Get the stock data
data = yf.download(stocks, start='2015-01-01', end='2020-12-31')['Adj Close']

# Calculate the returns
returns = data.pct_change()

# Calculate mean returns and covariances
mean_returns = returns.mean()
cov_matrix = returns.cov()

# Set the number of portfolios to simulate
num_portfolios = 10000
results = np.zeros((3,num_portfolios))

for i in range(num_portfolios):
    # Select random weights for portfolio holdings
    weights = np.random.random(len(stocks))
    weights /= np.sum(weights)
    
    # Calculate portfolio return and volatility
    portfolio_return = np.sum(mean_returns * weights) * 252
    portfolio_std_dev = np.sqrt(np.dot(weights.T,np.dot(cov_matrix, weights))) * np.sqrt(252)
    
    # Store results in results array
    results[0,i] = portfolio_return
    results[1,i] = portfolio_std_dev
    # Store Sharpe Ratio (return / volatility) - risk free rate element excluded for simplicity
    results[2,i] = results[0,i] / results[1,i]

# Convert results array to Pandas DataFrame
results_frame = pd.DataFrame(results.T,columns=['return','stdev','sharpe'])

# Plot efficient frontier with a scatter plot
plt.scatter(results_frame.stdev,results_frame.return,c=results_frame.sharpe,cmap='RdYlBu')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.show()
```

This code will generate a plot of the efficient frontier, which shows the set of optimal portfolios that offer the highest expected return for a defined level of risk. The color of each point represents the Sharpe Ratio, which measures the performance of an investment compared to a risk-free asset, after adjusting for its risk. The higher the Sharpe Ratio, the better the investment's risk-adjusted return.