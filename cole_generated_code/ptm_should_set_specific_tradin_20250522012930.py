from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that sets specific trading goals for the day. In this example, the goals are set in terms of the number of trades to be made and the minimum profit to be achieved.

```python
class PTM:
    def __init__(self):
        self.trades_made = 0
        self.profit = 0.0

    def set_goals(self, trade_goal, profit_goal):
        self.trade_goal = trade_goal
        self.profit_goal = profit_goal
        print(f'Trading goals for the day are set to {trade_goal} trades and minimum profit of ${profit_goal}')

    def make_trade(self, profit):
        self.trades_made += 1
        self.profit += profit
        if self.trades_made >= self.trade_goal and self.profit >= self.profit_goal:
            print('Trading goals for the day are achieved.')
        elif self.trades_made >= self.trade_goal:
            print('Trade goal for the day is achieved. Keep going to reach the profit goal.')
        elif self.profit >= self.profit_goal:
            print('Profit goal for the day is achieved. Keep going to reach the trade goal.')
        else:
            print('Keep trading to reach the goals.')

# Initialize PTM
ptm = PTM()

# Set trading goals for the day
ptm.set_goals(10, 500)

# Make trades and check goals
ptm.make_trade(50)
ptm.make_trade(100)
ptm.make_trade(200)
```

In this code, `PTM` is a class that represents a trading system. It has two attributes: `trades_made` and `profit`, which track the number of trades made and the total profit respectively. The `set_goals` method is used to set the trading goals for the day. The `make_trade` method is used to make a trade and update the `trades_made` and `profit` attributes. After each trade, it checks if the trading goals for the day are achieved and prints an appropriate message.