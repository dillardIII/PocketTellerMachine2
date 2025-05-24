Sure, here is a simple Python code that can be used to track the daily wins and losses for PTM. This code assumes that the data for wins and losses is input manually. 

```python
class PTM:
    def __init__(self):
        self.daily_wins = 0
        self.daily_losses = 0
        self.goal_wins = 0
        self.goal_losses = 0

    def set_goals(self, wins, losses):
        self.goal_wins = wins
        self.goal_losses = losses

    def record_win(self):
        self.daily_wins += 1

    def record_loss(self):
        self.daily_losses += 1

    def check_progress(self):
        print(f"Goal for wins: {self.goal_wins}, Current wins: {self.daily_wins}")
        print(f"Goal for losses: {self.goal_losses}, Current losses: {self.daily_losses}")

# Usage
ptm = PTM()
ptm.set_goals(10, 5)  # Set goals
ptm.record_win()  # Record a win
ptm.record_loss()  # Record a loss
ptm.check_progress()  # Check progress
```

This is a very basic implementation. Depending on the actual requirements, you might need to add more features, such as storing the data in a database, handling multiple users, etc.