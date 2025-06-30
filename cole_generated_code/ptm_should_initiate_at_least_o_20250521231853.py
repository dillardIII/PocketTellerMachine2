from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code that simulates a trade. This code doesn't connect to any real trading platform, it's just a simulation. 

```python
import random

class Trade:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class PTM:
    def __init__(self):
        self.balance = 10000
        self.trades = []

    def initiate_trade(self, trade, quantity):
        cost = trade.price * quantity
        if cost > self.balance:
            print("Insufficient balance to initiate the trade.")
            return
        self.balance -= cost
        self.trades.append((trade, quantity))
        print(f"Trade initiated: Bought {quantity} of {trade.name} at {trade.price}")

    def close_trade(self, trade):
        for t in self.trades:
            if t[0] == trade:
                self.trades.remove(t)
                closing_price = random.uniform(trade.price * 0.9, trade.price * 1.1)
                self.balance += closing_price * t[1]
                print(f"Trade closed: Sold {t[1]} of {trade.name} at {closing_price}")
                return
        print("Trade not found.")

ptm = PTM()
trade = Trade("AAPL", 150)
ptm.initiate_trade(trade, 10)
ptm.close_trade(trade)
print(f"Remaining balance: {ptm.balance}")
```

This code first defines a `Trade` class, which represents a trade with a name and a price. Then it defines a `PTM` class, which represents a trading manager with a balance and a list of trades. The `initiate_trade` method initiates a trade by subtracting the cost from the balance and adding the trade to the list of trades. The `close_trade` method closes a trade by removing it from the list of trades and adding the closing price to the balance. The closing price is randomly generated to be between 90% and 110% of the opening price, simulating potential wins or losses.