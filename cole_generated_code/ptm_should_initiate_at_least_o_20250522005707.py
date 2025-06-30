from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code to initiate a trade. This code is just a basic example and does not include any specific trading strategies. 

```python
import random

class PTM:
    def __init__(self):
        self.balance = 10000  # initial balance
        self.stocks = 0  # initial stocks

    def buy_stock(self, price, quantity):
        if price * quantity > self.balance:
            print("Not enough balance to buy the stocks")
            return
        self.balance -= price * quantity
        self.stocks += quantity
        print(f"Bought {quantity} stocks at {price} each. Current balance: {self.balance}")

    def sell_stock(self, price, quantity):
        if quantity > self.stocks:
            print("Not enough stocks to sell")
            return
        self.balance += price * quantity
        self.stocks -= quantity
        print(f"Sold {quantity} stocks at {price} each. Current balance: {self.balance}")

    def initiate_trade(self):
        stock_price = random.randint(50, 150)  # random stock price between 50 and 150
        if random.choice([True, False]):  # randomly decide to buy or sell
            self.buy_stock(stock_price, 1)  # buy 1 stock
        else:
            self.sell_stock(stock_price, 1)  # sell 1 stock

ptm = PTM()
ptm.initiate_trade()
```

This code creates a class `PTM` which represents a simple trading model. It has methods to buy and sell stocks and an `initiate_trade` method which randomly decides to buy or sell a stock at a random price. 

Please note that this is a very simplified model and real-world trading involves much more complexities like handling multiple types of stocks, considering market trends, etc. Also, this code does not evaluate the effectiveness of any trading strategies. For that, you would need to define what you mean by "effectiveness" and then implement corresponding metrics.