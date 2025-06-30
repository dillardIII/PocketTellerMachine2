from ghost_env import INFURA_KEY, VAULT_ADDRESS
To increase the number of trades, you can create a loop that will execute trades more frequently. Here is a simple example of how you might do this with a hypothetical trading API:

```python
import random
import time

class TradeAPI:
    def __init__(self):
        self.trades = 0
        self.wins = 0

    def execute_trade(self):
        # Simulate a trade execution
        self.trades += 1
        # Simulate a win with 50% probability
        if random.random() > 0.5:
            self.wins += 1
        return self.wins, self.trades

# Initialize the trading API
api = TradeAPI()

# Set the number of trades to execute
num_trades = 100

# Execute trades
for _ in range(num_trades):
    wins, trades = api.execute_trade()
    print(f"Executed trade {trades}, total wins: {wins}")
    # Sleep for a while to simulate time between trades
    time.sleep(0.1)
```

This code will execute 100 trades, with a 50% chance of each trade being a win. The number of trades to execute can be adjusted by changing the `num_trades` variable.

Please note that in real trading, increasing the number of trades does not necessarily improve the probability of recording wins. The outcome of each trade is largely independent and depends on the market conditions, your trading strategy, and many other factors.