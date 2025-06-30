from ghost_env import INFURA_KEY, VAULT_ADDRESS
In order to diversify the portfolio, we can create a Python script that selects a variety of stocks from different sectors. Here's a simple example of how this could be done:

```python
import pandas as pd
import yfinance as yf
import random

# Define the sectors we want to diversify in
sectors = ['Technology', 'Healthcare', 'Financial Services', 'Consumer Cyclical', 'Real Estate', 'Energy']

# Define a list of stocks for each sector
stocks = {
    'Technology': ['AAPL', 'MSFT', 'GOOGL', 'FB', 'TSLA'],
    'Healthcare': ['JNJ', 'UNH', 'PFE', 'MRK', 'ABT'],
    'Financial Services': ['JPM', 'BAC', 'WFC', 'C', 'GS'],
    'Consumer Cyclical': ['AMZN', 'HD', 'MCD', 'NKE', 'SBUX'],
    'Real Estate': ['AMT', 'PLD', 'SPG', 'PSA', 'AVB'],
    'Energy': ['XOM', 'CVX', 'COP', 'EOG', 'SLB']
}

# Create an empty DataFrame to store the portfolio
portfolio = pd.DataFrame(columns=['Sector', 'Stock', 'Price'])

# For each sector, randomly select a stock and add it to the portfolio
for sector in sectors:
    stock = random.choice(stocks[sector])
    price = yf.Ticker(stock).info['regularMarketPrice']
    portfolio = portfolio.append({'Sector': sector, 'Stock': stock, 'Price': price}, ignore_index=True)

print(portfolio)
```

This script uses the yfinance library to get the current price of each stock. It randomly selects one stock from each sector and adds it to the portfolio. The resulting portfolio is diversified across the specified sectors.

Note: This is a very simplified example and actual portfolio diversification should consider many other factors such as the correlation between assets, the expected returns and risks of each asset, etc.