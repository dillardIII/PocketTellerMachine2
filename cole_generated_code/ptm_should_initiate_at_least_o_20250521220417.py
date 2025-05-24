Here is a simple example of how you might implement this in Python. This is a very basic example and doesn't represent a real trading system. It's just a simple simulation to illustrate the concept.

```python
import random

class Trade:
    def __init__(self, name):
        self.name = name
        self.win = False

    def execute(self):
        # Simulate win or loss with 50/50 chance
        self.win = random.choice([True, False])

class PTM:
    def __init__(self):
        self.trades = []

    def initiate_trade(self, trade_name):
        trade = Trade(trade_name)
        trade.execute()
        self.trades.append(trade)

    def gather_data(self):
        wins = sum([trade.win for trade in self.trades])
        losses = len(self.trades) - wins
        return wins, losses

# Create PTM and initiate at least one trade
ptm = PTM()
ptm.initiate_trade("Trade 1")

# Gather data on wins and losses
wins, losses = ptm.gather_data()
print(f"Wins: {wins}, Losses: {losses}")
```

In this code, we create a `Trade` class to represent a trade, which can either win or lose. The `PTM` class represents the trading system, which can initiate trades and gather data on wins and losses. The `initiate_trade` method creates a new trade, executes it, and adds it to the list of trades. The `gather_data` method calculates the number of wins and losses.