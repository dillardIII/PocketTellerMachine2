Sure, in order to diversify the portfolio, we can create a Python script that selects a variety of stocks from different sectors. Here's a simple example of how you might do this:

```python
import random
import yfinance as yf

# Define a list of stocks from different sectors
tech_stocks = ['AAPL', 'MSFT', 'GOOGL']
healthcare_stocks = ['JNJ', 'PFE', 'MRK']
energy_stocks = ['XOM', 'CVX', 'BP']
financial_stocks = ['JPM', 'BAC', 'WFC']
consumer_stocks = ['PG', 'KO', 'PEP']

all_stocks = [tech_stocks, healthcare_stocks, energy_stocks, financial_stocks, consumer_stocks]

# Define the number of stocks to select from each sector
num_stocks = 2

# Create a diversified portfolio
portfolio = []
for sector in all_stocks:
    portfolio += random.sample(sector, num_stocks)

# Download historical market data
data = yf.download(portfolio, start="2020-01-01", end="2022-12-31")

# Calculate and print the portfolio's performance
returns = data['Adj Close'].pct_change()
portfolio_performance = returns.mean() * 252
print('Portfolio Performance: ', portfolio_performance)
```

Please note that this is a very basic example. In a real-world scenario, you would need to consider many other factors such as the correlation between different stocks, the volatility of the stocks, the weight of each stock in the portfolio, etc. Also, you would need to install the `yfinance` library to download the historical market data.