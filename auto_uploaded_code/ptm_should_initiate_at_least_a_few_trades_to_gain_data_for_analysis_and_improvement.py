from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide a simple Python code to simulate a trading bot. However, please note that this is a very basic example and doesn't include real trading strategies. You should not use this for real trading without adding proper trading strategies, error handling and security measures.

```python
import random
import time

class PTM:
    def __init__(self, initial_balance=10000):
        self.balance = initial_balance
        self.trades = []

    def trade(self, price, type):
        if type == 'buy':
            if self.balance >= price:
                self.balance -= price
                self.trades.append((time.time(), price, type))
                print(f"Bought at {price}. Current balance: {self.balance}")
            else:
                print("Not enough balance to buy")
        elif type == 'sell':
            self.balance += price
            self.trades.append((time.time(), price, type))
            print(f"Sold at {price}. Current balance: {self.balance}")

    def start_trading(self, min_price=50, max_price=150):
        for _ in range(10):  # replace with while True for infinite loop
            price = random.randint(min_price, max_price)
            type = 'buy' if random.random() < 0.5 else 'sell'
            self.trade(price, type)
            time.sleep(1)  # wait for 1 second

ptm = PTM()
ptm.start_trading()
```

This code creates a simple trading bot that randomly decides to buy or sell at a random price between 50 and 150. It initiates 10 trades and waits for 1 second between each trade. The trades and the remaining balance are printed to the console. The trades are also stored in a list for later analysis.