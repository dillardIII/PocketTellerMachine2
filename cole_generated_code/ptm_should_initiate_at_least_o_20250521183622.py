from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that simulates a trading bot. This bot will initiate at least one trade. Please note that this is a very basic example and doesn't include any real trading strategies or risk management.

```python
import random

class PTM:
    def __init__(self, balance):
        self.balance = balance
        self.stock = 0

    def buy(self, price):
        if self.balance > price:
            self.balance -= price
            self.stock += 1
            print(f"PTM bought 1 stock for {price}. Current balance: {self.balance}")

    def sell(self, price):
        if self.stock > 0:
            self.balance += price
            self.stock -= 1
            print(f"PTM sold 1 stock for {price}. Current balance: {self.balance}")

    def trade(self):
        # Random price between 10 and 20
        price = random.randint(10, 20)

        # Randomly decide to buy or sell
        if random.choice(["buy", "sell"]) == "buy":
            self.buy(price)
        else:
            self.sell(price)

# Initialize PTM with a balance of 100
ptm = PTM(100)

# PTM initiates at least one trade
ptm.trade()
```

This script will randomly decide to buy or sell a stock at a random price between 10 and 20. If PTM decides to buy, it will only do so if it has enough balance. If PTM decides to sell, it will only do so if it has at least 1 stock.