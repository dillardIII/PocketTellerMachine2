Sure, here is a simple Python code to simulate a trading system. This code will initiate at least one trade and gather data on wins and losses. Please note that this is a very basic simulation and doesn't take into account many factors that would be present in a real-world trading scenario.

```python
import random

class PTM:
    def __init__(self):
        self.trades = []
        self.wins = 0
        self.losses = 0

    def initiate_trade(self):
        # Simulate a trade with a 50% chance of winning
        trade_result = random.choice(['win', 'loss'])
        self.trades.append(trade_result)
        
        if trade_result == 'win':
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

# Initiate at least one trade
ptm.initiate_trade()

# Get trade data
trade_data = ptm.get_trade_data()

print(trade_data)
```

In this code, we create a PTM class that has methods to initiate a trade and get trade data. When a trade is initiated, it randomly results in a win or a loss. The results are stored and can be retrieved using the `get_trade_data` method.