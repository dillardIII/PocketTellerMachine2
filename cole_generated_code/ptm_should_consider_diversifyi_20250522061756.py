To diversify a portfolio, you need to select different types of investments. This can be done by using different strategies such as investing in different sectors, different regions, etc. Here is a simple Python code that simulates diversifying a portfolio by investing in different sectors.

```python
import random

# List of sectors to invest in
sectors = ["Technology", "Healthcare", "Finance", "Consumer Discretionary", "Utilities", "Industrials", "Materials", "Real Estate", "Energy", "Consumer Staples"]

# Initial portfolio
portfolio = {}

# Function to diversify portfolio
def diversify_portfolio(portfolio, sectors, num_investments):
    for i in range(num_investments):
        # Randomly select a sector
        sector = random.choice(sectors)
        # If sector is already in portfolio, add to the investment, else start a new investment
        if sector in portfolio:
            portfolio[sector] += 1
        else:
            portfolio[sector] = 1
    return portfolio

# Diversify portfolio
portfolio = diversify_portfolio(portfolio, sectors, 10)

print(portfolio)
```

This code randomly selects sectors to invest in. The number of investments in each sector is determined by the `num_investments` parameter. The resulting portfolio is a dictionary where the keys are the sectors and the values are the number of investments in each sector.

Please note that this is a very simplified example and does not take into account many factors that should be considered when diversifying a portfolio, such as the risk and return of each investment, the correlation between different investments, etc. It's always recommended to seek advice from a financial advisor or use a sophisticated financial model when diversifying a portfolio.