Sure, here is a simple Python code that simulates a trade and gathers data on wins and losses. Please note that this is a basic simulation and does not involve any real trading. 

```python
import random

class PTM:
    def __init__(self):
        self.trades = []
        self.wins = 0
        self.losses = 0

    def initiate_trade(self):
        # Simulate a trade with random outcome
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

# Create a PTM instance
ptm = PTM()

# Initiate a trade
ptm.initiate_trade()

# Get trade data
trade_data = ptm.get_trade_data()

print(trade_data)
```

This code creates a PTM class with methods to initiate a trade and get trade data. The `initiate_trade` method simulates a trade with a random outcome of either 'win' or 'loss'. The `get_trade_data` method returns a dictionary with the total number of trades, wins, and losses. 

Please replace the random trade outcome with actual trading logic as per your requirements.