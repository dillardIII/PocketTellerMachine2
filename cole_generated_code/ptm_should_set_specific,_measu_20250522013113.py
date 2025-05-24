Sure, here's a simple Python code snippet that can help you track the progress of PTM's wins and losses:

```python
class PTM:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.win_goal = 0
        self.loss_goal = 0

    def set_goals(self, win_goal, loss_goal):
        self.win_goal = win_goal
        self.loss_goal = loss_goal

    def track_progress(self, wins, losses):
        self.wins += wins
        self.losses += losses

        if self.wins >= self.win_goal:
            print(f"Win goal achieved! Current wins: {self.wins}")
        else:
            print(f"Win goal not yet achieved. Current wins: {self.wins}")

        if self.losses >= self.loss_goal:
            print(f"Loss goal achieved! Current losses: {self.losses}")
        else:
            print(f"Loss goal not yet achieved. Current losses: {self.losses}")

# Example usage
ptm = PTM()
ptm.set_goals(10, 5)
ptm.track_progress(3, 1)
ptm.track_progress(7, 4)
```

In this code, we create a class PTM with attributes for wins, losses, and the goals for each. The `set_goals` method allows you to specify the goals, and the `track_progress` method allows you to update the wins and losses and check if the goals have been achieved.