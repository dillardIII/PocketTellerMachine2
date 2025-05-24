Sure, here is a simple Python code that can be used to track the progress of PTM's wins and losses. This code uses a dictionary to store the goals and the current status.

```python
class PTM:
    def __init__(self):
        # Initialize the goals and current status
        self.goals = {'wins': 0, 'losses': 0}
        self.current_status = {'wins': 0, 'losses': 0}

    def set_goals(self, wins, losses):
        # Set the goals for wins and losses
        self.goals['wins'] = wins
        self.goals['losses'] = losses

    def update_status(self, wins, losses):
        # Update the current status of wins and losses
        self.current_status['wins'] += wins
        self.current_status['losses'] += losses

    def track_progress(self):
        # Track the progress of wins and losses
        win_progress = (self.current_status['wins'] / self.goals['wins']) * 100
        loss_progress = (self.current_status['losses'] / self.goals['losses']) * 100

        return win_progress, loss_progress

# Create an instance of PTM
ptm = PTM()

# Set the goals for wins and losses
ptm.set_goals(100, 50)

# Update the current status of wins and losses
ptm.update_status(30, 10)

# Track the progress of wins and losses
win_progress, loss_progress = ptm.track_progress()

print(f"Win Progress: {win_progress}%")
print(f"Loss Progress: {loss_progress}%")
```

This code will output the progress of wins and losses as a percentage of the goals. Please adjust the numbers according to your needs.