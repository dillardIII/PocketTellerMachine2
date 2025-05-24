Sure, here's a simple Python code to implement a trading strategy. In this example, we'll use a basic strategy of diversifying the portfolio by investing in different sectors. We'll use the `yfinance` library to get the stock data. Please note that this is a very basic example and real-world trading strategies can be much more complex.

```python
import yfinance as yf
import pandas as pd

class TradingStrategy:
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def diversify(self, new_stock):
        if new_stock not in self.portfolio:
            self.portfolio.append(new_stock)
            print(f"Added {new_stock} to the portfolio.")
        else:
            print(f"{new_stock} is already in the portfolio.")

    def get_portfolio(self):
        return self.portfolio

    def get_stock_data(self, stock):
        data = yf.download(stock, start='2020-01-01', end='2022-12-31')
        return data

# Initialize portfolio with some stocks
portfolio = ['AAPL', 'GOOGL', 'AMZN']

# Initialize trading strategy
trading_strategy = TradingStrategy(portfolio)

# Diversify portfolio
trading_strategy.diversify('MSFT')
trading_strategy.diversify('TSLA')

# Get updated portfolio
print(trading_strategy.get_portfolio())

# Get stock data
for stock in trading_strategy.get_portfolio():
    data = trading_strategy.get_stock_data(stock)
    print(f"\n{stock} data:")
    print(data.head())
```

This code will add 'MSFT' and 'TSLA' to the portfolio if they are not already there. Then it will print the updated portfolio and the stock data for each stock in the portfolio.

Please note that you need to install `yfinance` library to run this code. You can install it using pip:

```bash
pip install yfinance
```

Also, this is a very basic trading strategy. In real-world scenarios, you would need to consider many other factors like the performance of the stocks, the correlation between the stocks, the risk tolerance, etc.