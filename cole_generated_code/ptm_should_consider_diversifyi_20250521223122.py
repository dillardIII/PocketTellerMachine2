To diversify a trading portfolio, we can use Python with the help of pandas, numpy and yfinance libraries. Here's a simple example of how you can do it:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

# Define the stocks to be included in the portfolio
stocks = ['AAPL', 'TSLA', 'GOOGL', 'AMZN', 'MSFT']

# Define the start and end dates for the data
start_date = '2020-01-01'
end_date = datetime.today().strftime('%Y-%m-%d')

# Download the data
data = yf.download(stocks, start=start_date, end=end_date)['Adj Close']

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
    weights = np.random.random(len(stocks))
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

# Create a scatter plot coloured by Sharpe Ratio
plt.scatter(results_frame.stdev,results_frame['return'],c=results_frame.sharpe,cmap='RdYlBu')
plt.xlabel('Volatility')
plt.ylabel('Returns')
plt.colorbar()
# Plot red star to highlight position of portfolio with highest Sharpe Ratio
plt.scatter(max_sharpe_port[1],max_sharpe_port[0],marker=(5,1,0),color='r',s=500)
# Plot green star to highlight position of minimum variance portfolio
plt.scatter(min_vol_port[1],min_vol_port[0],marker=(5,1,0),color='g',s=500)
plt.show()
```

This Python code will generate a scatter plot of the different portfolio combinations based on the selected stocks. The red star on the plot indicates the portfolio with the highest Sharpe ratio (best risk-adjusted performance), and the green star indicates the portfolio with the lowest standard deviation (least risk).