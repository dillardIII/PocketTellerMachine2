from ghost_env import INFURA_KEY, VAULT_ADDRESS
To complete this task, we need to create a simple trading bot using Python. For simplicity, we'll use a basic strategy: buy when the price is low and sell when the price is high. We'll use the `yfinance` library to get stock price data and `pandas` to analyze it.

Please note that this is a very basic trading bot and is not recommended for actual trading. It's just for demonstration purposes.

```python
import yfinance as yf
import pandas as pd

class TradingBot:
    def __init__(self, ticker, budget):
        self.ticker = ticker
        self.budget = budget
        self.shares = 0

    def get_data(self):
        data = yf.download(self.ticker, start='2021-01-01', end='2022-12-31')
        return data['Close']

    def buy(self, price):
        shares_to_buy = self.budget // price
        if shares_to_buy > 0:
            self.budget -= shares_to_buy * price
            self.shares += shares_to_buy
            print(f'Bought {shares_to_buy} shares at {price}')

    def sell(self, price):
        if self.shares > 0:
            self.budget += self.shares * price
            print(f'Sold {self.shares} shares at {price}')
            self.shares = 0

    def trade(self):
        data = self.get_data()
        buy_price = data.min()
        sell_price = data.max()

        self.buy(buy_price)
        self.sell(sell_price)

        return self.budget

# Initialize the bot with a ticker and a budget
bot = TradingBot('AAPL', 10000)

# Start trading
final_budget = bot.trade()

print(f'Final budget: {final_budget}')
```

This bot will buy shares when the price is at its lowest point and sell when the price is at its highest point. The final budget will be printed at the end.