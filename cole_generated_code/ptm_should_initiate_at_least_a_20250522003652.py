Sure, here is a simple Python code that simulates a trading bot. This bot will make trades and record the wins and losses. Please note that this is a simulation and doesn't involve real trading.

```python
import random

class PTM:
    def __init__(self):
        self.trades = []
        self.wins = 0
        self.losses = 0

    def make_trade(self):
        # Simulate a trade win or loss
        trade_outcome = random.choice(['win', 'loss'])

        # Record the trade
        self.trades.append(trade_outcome)

        # Update wins and losses
        if trade_outcome == 'win':
            self.wins += 1
        else:
            self.losses += 1

    def report(self):
        print(f'Total trades: {len(self.trades)}')
        print(f'Wins: {self.wins}')
        print(f'Losses: {self.losses}')


# Initialize PTM
ptm = PTM()

# Make trades
for _ in range(10):  # Change this number to make more or fewer trades
    ptm.make_trade()

# Report results
ptm.report()
```

This code creates a `PTM` class that simulates a trading bot. The bot can make trades with the `make_trade` method, which randomly determines whether the trade is a win or a loss. The bot keeps track of all trades, wins, and losses. After making a certain number of trades, the bot reports the total number of trades, wins, and losses.