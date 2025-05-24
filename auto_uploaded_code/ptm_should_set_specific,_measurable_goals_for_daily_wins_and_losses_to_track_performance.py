Sure, here's a simple Python code that could be used to track daily wins and losses:

```python
class PTM:
    def __init__(self):
        self.daily_goals = {"wins": 0, "losses": 0}
        self.daily_performance = {"wins": 0, "losses": 0}

    def set_daily_goals(self, wins, losses):
        self.daily_goals["wins"] = wins
        self.daily_goals["losses"] = losses

    def record_performance(self, wins, losses):
        self.daily_performance["wins"] = wins
        self.daily_performance["losses"] = losses

    def track_performance(self):
        win_goal_met = self.daily_performance["wins"] >= self.daily_goals["wins"]
        loss_goal_met = self.daily_performance["losses"] <= self.daily_goals["losses"]

        if win_goal_met and loss_goal_met:
            return "Daily goals met!"
        else:
            return "Daily goals not met. Keep trying!"

# Example usage:
ptm = PTM()
ptm.set_daily_goals(wins=10, losses=5)
ptm.record_performance(wins=12, losses=4)
print(ptm.track_performance())
```

In this code, we have a class `PTM` that has methods to set daily goals for wins and losses, record the actual performance, and then track whether the performance met the goals. The `track_performance` method checks if the number of wins is greater than or equal to the goal, and if the number of losses is less than or equal to the goal. If both conditions are met, it returns a success message. Otherwise, it returns a message indicating that the goals were not met.