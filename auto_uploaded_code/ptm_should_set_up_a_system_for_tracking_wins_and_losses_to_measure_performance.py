Sure, here's a simple Python code to track wins and losses for PTM:

```python
class PTM:
    def __init__(self):
        self.wins = 0
        self.losses = 0

    def win(self):
        self.wins += 1

    def loss(self):
        self.losses += 1

    def performance(self):
        total_games = self.wins + self.losses
        if total_games == 0:
            return "No games played yet."
        else:
            win_rate = self.wins / total_games
            loss_rate = self.losses / total_games
            return f"Performance: {win_rate*100}% wins, {loss_rate*100}% losses"

# Example usage:
ptm = PTM()
ptm.win()
ptm.loss()
print(ptm.performance())
```

This code creates a class `PTM` with methods to increment wins and losses, and a method to calculate and return the performance as a percentage of wins and losses. The `performance` method checks if any games have been played before calculating the percentages to avoid dividing by zero.