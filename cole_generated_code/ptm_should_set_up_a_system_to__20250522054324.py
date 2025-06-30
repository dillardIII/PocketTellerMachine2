from ghost_env import INFURA_KEY, VAULT_ADDRESS
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

    def performance_evaluation(self):
        total_games = self.wins + self.losses
        if total_games == 0:
            return "No games played yet."
        win_rate = self.wins / total_games
        loss_rate = self.losses / total_games
        return f"Total games: {total_games}, Wins: {self.wins}, Losses: {self.losses}, Win rate: {win_rate*100}%, Loss rate: {loss_rate*100}%"

# Usage
ptm = PTM()
ptm.win()
ptm.loss()
ptm.loss()
print(ptm.performance_evaluation())
```

This code creates a class named `PTM` with methods to track wins and losses and to evaluate performance. The `win` method increments the `wins` attribute by 1, and the `loss` method increments the `losses` attribute by 1. The `performance_evaluation` method calculates the total number of games, win rate, and loss rate, and returns a string with this information.