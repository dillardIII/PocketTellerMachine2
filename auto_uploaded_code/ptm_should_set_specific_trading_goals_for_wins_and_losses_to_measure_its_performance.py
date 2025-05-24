Sure, here's a simple Python code that sets specific trading goals for wins and losses. This code assumes that you have a list of trades with their respective profits or losses.

```python
class PTM:
    def __init__(self, trades):
        self.trades = trades
        self.win_goal = 0
        self.loss_goal = 0

    def set_goals(self, win_goal, loss_goal):
        self.win_goal = win_goal
        self.loss_goal = loss_goal

    def measure_performance(self):
        wins = [trade for trade in self.trades if trade > 0]
        losses = [trade for trade in self.trades if trade < 0]

        if len(wins) >= self.win_goal and abs(sum(losses)) <= self.loss_goal:
            return "Performance goal achieved"
        else:
            return "Performance goal not achieved"


# Example usage:
trades = [100, -50, 200, -150, 300, -100]
ptm = PTM(trades)
ptm.set_goals(3, 200)  # Set goal of 3 wins and losses not exceeding 200
print(ptm.measure_performance())
```

In this code, a PTM (Portfolio Trading Manager) class is defined. It has a list of trades and methods to set goals and measure performance. The `set_goals` method sets the win and loss goals. The `measure_performance` method checks if the number of wins is greater than or equal to the win goal and the total loss does not exceed the loss goal. If both conditions are met, it returns "Performance goal achieved", otherwise it returns "Performance goal not achieved".