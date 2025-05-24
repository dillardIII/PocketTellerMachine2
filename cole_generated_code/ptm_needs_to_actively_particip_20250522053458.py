To actively participate in the market, PTM (let's assume it's a trading bot) needs to perform actions such as buying and selling stocks. Here is a simple Python code that simulates this process:

```python
import random

class PTM:
    def __init__(self):
        self.cash = 10000
        self.stocks = 0
        self.stock_price = 100

    def buy_stock(self, num_stocks):
        if self.cash >= num_stocks * self.stock_price:
            self.cash -= num_stocks * self.stock_price
            self.stocks += num_stocks
            print(f"PTM bought {num_stocks} stocks.")

    def sell_stock(self, num_stocks):
        if self.stocks >= num_stocks:
            self.stocks -= num_stocks
            self.cash += num_stocks * self.stock_price
            print(f"PTM sold {num_stocks} stocks.")

    def random_trade(self):
        action = random.choice(['buy', 'sell'])
        num_stocks = random.randint(1, 10)

        if action == 'buy':
            self.buy_stock(num_stocks)
        else:
            self.sell_stock(num_stocks)

ptm = PTM()
for _ in range(100):
    ptm.random_trade()
```

In this code, PTM starts with $10,000 and no stocks. The price of a stock is fixed at $100 for simplicity. PTM randomly decides whether to buy or sell stocks, and the number of stocks to trade is also randomly decided (between 1 and 10). This process is repeated 100 times to simulate active participation in the market.

Please note that this is a very simple simulation and does not reflect the complexities of real-world trading. In a real trading scenario, PTM would need to consider factors such as the current market price of the stocks, market trends, and trading strategies.