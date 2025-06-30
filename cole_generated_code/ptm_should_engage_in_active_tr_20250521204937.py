from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code that simulates active trading. Please note that this is a very simplified version and does not take into account many factors that are usually considered in real trading.

```python
import random

class Trade:
    def __init__(self):
        self.balance = 10000  # starting balance
        self.trades = []  # list of trades

    def make_trade(self):
        # randomly decide whether the trade is a win or a loss
        win = random.choice([True, False])

        # randomly decide the amount of the trade
        amount = random.uniform(0, self.balance)

        if win:
            # if the trade is a win, increase the balance
            self.balance += amount
            self.trades.append(('win', amount))
        else:
            # if the trade is a loss, decrease the balance
            self.balance -= amount
            self.trades.append(('loss', amount))

    def start_trading(self, num_trades):
        for _ in range(num_trades):
            self.make_trade()

        return self.trades, self.balance

# create a Trade object
trade = Trade()

# start trading
trades, final_balance = trade.start_trading(100)

# print the trades and the final balance
print('Trades:', trades)
print('Final balance:', final_balance)
```

This code creates a `Trade` class that has a `balance` and a list of `trades`. The `make_trade` method randomly decides whether a trade is a win or a loss, and randomly decides the amount of the trade. The `start_trading` method makes a specified number of trades and returns the list of trades and the final balance.