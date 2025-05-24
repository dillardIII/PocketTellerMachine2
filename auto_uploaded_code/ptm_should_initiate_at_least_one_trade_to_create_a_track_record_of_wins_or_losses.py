Sure, here's a simple Python code that simulates a trading system. This code initiates a trade and records whether it's a win or a loss based on a random outcome.

```python
import random

class PTM:
    def __init__(self):
        self.record = []

    def trade(self):
        # Simulate a trade outcome with 50% chance of win
        outcome = random.choice(['win', 'loss'])
        self.record.append(outcome)
        print(f'Trade completed with {outcome} outcome')

    def get_record(self):
        wins = self.record.count('win')
        losses = self.record.count('loss')
        print(f'Total trades: {len(self.record)}, Wins: {wins}, Losses: {losses}')

# Create PTM object
ptm = PTM()

# Initiate a trade
ptm.trade()

# Print the record
ptm.get_record()
```

In this code, we create a class `PTM` which has a record of trade outcomes. The `trade` method simulates a trade with a 50% chance of either a win or a loss. The `get_record` method prints the total number of trades, wins, and losses.

Please note that this is a very basic simulation and real trading systems are much more complex and involve many other factors.