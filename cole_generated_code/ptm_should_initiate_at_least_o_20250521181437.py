from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, to initiate a simple program that simulates trading and determines win/loss ratios for the PTM (Proprietary Trading Model), you can use the following Python code. Please keep in mind that this is a simplified version and real trading involves more factors and data analysis.

For the purposes of this task, the variables `initial_price`, `final_price` and `quantity` are considered. We assume that we start with buying a certain quantity of stocks, and then sell them later. If the final price is higher than the initial one, it is considered a win, otherwise, a loss.

```python
import random

class Trading:
    def __init__(self, trading_attempts):
        self.trading_attempts = trading_attempts
        self.wins = 0
        self.losses = 0

    def trade(self):
        for _ in range(self.trading_attempts):
            initial_price = random.uniform(50, 200)  # Random initial price between 50 and 200
            final_price = random.uniform(30, 220)  # Random final price between 30 and 220
            quantity = random.randint(1, 10)  # Random quantity between 1 and 10
            
            if final_price > initial_price:
                self.wins += quantity
            else:
                self.losses += quantity
    
    def get_ratio(self):
        total = self.wins + self.losses
        win_ratio = self.wins / total
        loss_ratio = self.losses / total

        return win_ratio, loss_ratio

trading = Trading(trading_attempts=100)
trading.trade()

win_ratio, loss_ratio = trading.get_ratio()

print(f"Win ratio: {win_ratio*100:.2f}%")
print(f"Loss ratio: {loss_ratio*100:.2f}%")
```

This code simulates 100 trading attempts, using random initial and final prices, and a random quantity of stocks. After all trading attempts, it calculates the win/loss ratio. Please notice that this code uses pseudorandom generation for the prices and quantity, so the win/loss ratio will vary every time you run the script.