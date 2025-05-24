To set and track specific, measurable goals for wins and losses, we can create a Python class named `PTM` (Presume it stands for Profit Trade Management). This class will have methods to set goals, record wins and losses, and track progress. Here's a simple implementation:

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

    def record_win(self):
        self.wins += 1

    def record_loss(self):
        self.losses += 1

    def track_progress(self):
        win_progress = (self.wins / self.win_goal) * 100 if self.win_goal > 0 else 0
        loss_progress = (self.losses / self.loss_goal) * 100 if self.loss_goal > 0 else 0

        return win_progress, loss_progress
```

This class can be used as follows:

```python
ptm = PTM()
ptm.set_goals(win_goal=100, loss_goal=50)

# Record some wins and losses
for _ in range(60):
    ptm.record_win()
for _ in range(30):
    ptm.record_loss()

# Track progress
win_progress, loss_progress = ptm.track_progress()
print(f"Win progress: {win_progress}%")
print(f"Loss progress: {loss_progress}%")
```

This will print the progress towards the win and loss goals as percentages.