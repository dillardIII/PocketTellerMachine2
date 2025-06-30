from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a trading bot using Python. This bot will buy when the price is low and sell when the price is high. 

Please note that this is a very basic example and real-world trading bots are much more complex and require careful consideration of many factors. 

```python
import time
import random

class Trade:
    def __init__(self, price, type):
        self.price = price
        self.type = type

class PTM:
    def __init__(self):
        self.balance = 10000
        self.shares = 0
        self.trades = []

    def buy(self, price):
        if self.balance > price:
            self.balance -= price
            self.shares += 1
            self.trades.append(Trade(price, 'buy'))
            print(f'Bought at {price}. Balance is now {self.balance}')

    def sell(self, price):
        if self.shares > 0:
            self.balance += price
            self.shares -= 1
            self.trades.append(Trade(price, 'sell'))
            print(f'Sold at {price}. Balance is now {self.balance}')

    def trade(self):
        while True:
            price = random.randint(1, 100)
            if price < 30:
                self.buy(price)
            elif price > 70:
                self.sell(price)
            time.sleep(1)

ptm = PTM()
ptm.trade()
```

In this example, the PTM class represents the trading bot. It has a balance and shares, which represent the amount of money and the number of shares it has respectively. The buy and sell methods are used to buy and sell shares at a certain price. The trade method is where the trading logic is. It generates a random price between 1 and 100, and if the price is less than 30, it buys, and if the price is more than 70, it sells. This continues indefinitely until the program is stopped.