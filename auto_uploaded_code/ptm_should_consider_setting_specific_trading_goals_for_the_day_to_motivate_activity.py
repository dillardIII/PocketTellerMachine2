from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that sets a specific trading goal for the day.

```python
class TradingGoals:
    def __init__(self, initial_goal):
        self.goal = initial_goal
        self.trades_made = 0

    def make_trade(self):
        self.trades_made += 1
        print(f"Trade made. Total trades: {self.trades_made}")

    def check_goal(self):
        if self.trades_made >= self.goal:
            print("Daily trading goal reached!")
        else:
            remaining = self.goal - self.trades_made
            print(f"{remaining} more trades to reach the daily goal.")

# Set a daily goal of 10 trades
ptm = TradingGoals(10)

# Make some trades
for _ in range(5):
    ptm.make_trade()

# Check progress towards goal
ptm.check_goal()
```

In this code, we create a `TradingGoals` class that keeps track of the daily trading goal and the number of trades made. When a trade is made, the `make_trade` method is called, which increments the number of trades made and prints out the total. The `check_goal` method checks if the goal has been reached and prints out a message accordingly.