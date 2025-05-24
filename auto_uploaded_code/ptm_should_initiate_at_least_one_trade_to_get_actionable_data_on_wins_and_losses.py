To initiate a trade and get actionable data on wins and losses, we can use a simple Python script. However, please note that this is a simplified version and real trading involves more complexities.

```python
import random

class PTM:
    def __init__(self):
        self.trades = []
        self.wins = 0
        self.losses = 0

    def initiate_trade(self):
        # Here we are using a random choice for the sake of example,
        # in real trading, this decision should be based on some strategy
        trade_outcome = random.choice(['win', 'loss'])
        self.trades.append(trade_outcome)

        if trade_outcome == 'win':
            self.wins += 1
        else:
            self.losses += 1

    def get_trade_data(self):
        return {
            'total_trades': len(self.trades),
            'wins': self.wins,
            'losses': self.losses
        }

# Create PTM instance
ptm = PTM()

# Initiate at least one trade
ptm.initiate_trade()

# Get actionable data
trade_data = ptm.get_trade_data()
print(trade_data)
```

This script creates a PTM (Presumed Trading Machine) that can initiate trades. The outcome of each trade is randomly determined as either a 'win' or 'loss'. The PTM keeps track of all trades, wins, and losses. After initiating at least one trade, we can get the actionable data which includes the total number of trades, wins, and losses.