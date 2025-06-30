from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code that implements a diversification strategy. This strategy will invest in a variety of stocks to reduce risk. For simplicity, we will assume that we are investing in 5 different stocks and we will distribute our capital equally among all stocks.

Please note that this is a very simplified version of a trading strategy. In a real-world scenario, you would need to consider many other factors such as stock correlations, market conditions, risk tolerance, etc.

```python
import yfinance as yf
import pandas as pd

class DiversificationStrategy:
    def __init__(self, capital, stocks):
        self.capital = capital
        self.stocks = stocks
        self.portfolio = {stock: 0 for stock in stocks}

    def invest(self):
        investment_per_stock = self.capital / len(self.stocks)
        for stock in self.stocks:
            data = yf.download(stock, period='1d')
            price = data['Close'][0]
            shares = investment_per_stock / price
            self.portfolio[stock] = shares

    def print_portfolio(self):
        for stock, shares in self.portfolio.items():
            print(f'Stock: {stock}, Shares: {shares}')

# Test the strategy
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB']
strategy = DiversificationStrategy(10000, stocks)
strategy.invest()
strategy.print_portfolio()
```

This code uses the yfinance library to get the latest stock prices. It then calculates how many shares of each stock we can buy with our capital divided by the number of stocks. The portfolio is stored as a dictionary where the keys are the stock symbols and the values are the number of shares.

Please install the necessary libraries by using pip install command if not already installed.

```python
pip install yfinance pandas
```

Please note that this code does not actually execute any trades, it just simulates the strategy. To execute trades, you would need to integrate with a trading platform API.