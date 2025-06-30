from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code to simulate a trading bot. This bot will initiate at least one trade when the current price is lower than the average price, which increases the chances of making a profit when the price goes up.

```python
import random

class PTM:
    def __init__(self):
        self.funds = 10000
        self.stocks = 0
        self.prices = []
        self.current_price = 0

    def update_price(self):
        # Simulate price change
        self.current_price = random.randint(50, 150)
        self.prices.append(self.current_price)

    def trade(self):
        # Calculate average price
        average_price = sum(self.prices) / len(self.prices)

        # If current price is lower than average price, buy stocks
        if self.current_price < average_price:
            self.stocks += self.funds // self.current_price
            self.funds %= self.current_price

        # If current price is higher than average price, sell stocks
        elif self.current_price > average_price and self.stocks > 0:
            self.funds += self.stocks * self.current_price
            self.stocks = 0

    def run(self):
        for _ in range(100):
            self.update_price()
            self.trade()

# Create PTM and run
ptm = PTM()
ptm.run()

# Print final funds and stocks
print(f'Final funds: {ptm.funds}')
print(f'Final stocks: {ptm.stocks}')
```

This code simulates 100 days of trading. The PTM (Profitable Trading Machine) will buy stocks when the current price is lower than the average price and sell stocks when the current price is higher than the average price. This strategy increases the chances of making a profit.