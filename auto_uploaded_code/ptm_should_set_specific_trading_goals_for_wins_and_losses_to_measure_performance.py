Sure, here is a simple Python code to set and measure trading goals for wins and losses.

```python
class PTM:
    def __init__(self):
        self.trades = []
        self.goal_wins = 0
        self.goal_losses = 0

    def set_goals(self, wins, losses):
        self.goal_wins = wins
        self.goal_losses = losses

    def add_trade(self, trade):
        self.trades.append(trade)

    def measure_performance(self):
        wins = len([trade for trade in self.trades if trade > 0])
        losses = len([trade for trade in self.trades if trade < 0])

        if wins >= self.goal_wins and losses <= self.goal_losses:
            return "Goal achieved"
        else:
            return "Goal not achieved"

# Create PTM object
ptm = PTM()

# Set trading goals
ptm.set_goals(10, 5)

# Add trades
ptm.add_trade(100)  # win
ptm.add_trade(-50)  # loss
ptm.add_trade(200)  # win
# ... add more trades

# Measure performance
print(ptm.measure_performance())
```

In this code, we create a `PTM` class that represents a trading system. The `set_goals` method allows us to set specific trading goals for wins and losses. The `add_trade` method allows us to add a trade result (positive for wins, negative for losses). The `measure_performance` method checks if the number of wins is greater than or equal to the goal for wins and if the number of losses is less than or equal to the goal for losses. If both conditions are met, it returns "Goal achieved", otherwise it returns "Goal not achieved".