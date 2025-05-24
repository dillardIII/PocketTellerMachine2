Sure, here is a simple Python code that simulates diversification of a portfolio. This code uses the `yfinance` library to download stock data, `pandas` for data manipulation, and `numpy` for calculations. 

Please note that this is a very basic example and real portfolio diversification involves more complex analysis and strategic decision-making.

```python
import yfinance as yf
import pandas as pd
import numpy as np

# Define the list of stocks for our portfolio
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB']

# Download the stock data
data = yf.download(stocks, start='2020-01-01', end='2022-12-31')['Adj Close']

# Calculate the daily returns
returns = data.pct_change()

# Calculate mean returns and covariances of the stocks
mean_returns = returns.mean()
cov_matrix = returns.cov()

# Number of Portfolios to simulate
num_portfolios = 10000
results = np.zeros((3,num_portfolios))

for i in range(num_portfolios):
    # Select random weights and normalize to 1
    weights = np.random.random(len(stocks))
    weights /= np.sum(weights)
    
    # Calculate expected return, volatility and Sharpe ratio
    portfolio_return = np.sum(mean_returns * weights) * 252
    portfolio_std_dev = np.sqrt(np.dot(weights.T,np.dot(cov_matrix, weights))) * np.sqrt(252)
    results[0,i] = portfolio_return
    results[1,i] = portfolio_std_dev

# Convert results array to Pandas DataFrame
results_frame = pd.DataFrame(results.T,columns=['return','stdev'])

# Print the portfolios with the highest Sharpe ratio
max_sharpe_port = results_frame.iloc[results_frame['return'].idxmax()]
print("Portfolio with highest return:\n", max_sharpe_port)
```

This script creates a number of random portfolios (10,000 in this case) with different weights of the specified stocks, calculates the expected annual return and standard deviation (volatility) for each portfolio, and then prints the portfolio with the highest return.

Please note that you need to install `yfinance`, `pandas` and `numpy` libraries to run this script. You can install them using pip:

```bash
pip install yfinance pandas numpy
```

Also, this is a simulation and the results may not be accurate for real trading. Always consult with a financial advisor before making trading decisions.