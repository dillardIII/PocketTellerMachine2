To increase the number of trades executed, you could modify the trading algorithm to execute trades more frequently. Here is a simple example of how you might do this in Python. Please note that this is a very simplified example and does not take into account many important factors that should be considered in a real trading algorithm, such as market conditions, risk management, etc.

```python
class PTM:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.trades_executed = 0

    def execute_trade(self, trade_value):
        if self.balance >= trade_value:
            self.balance -= trade_value
            self.trades_executed += 1
            return True
        else:
            return False

    def increase_trade_frequency(self, trade_value, trade_frequency):
        for _ in range(trade_frequency):
            if not self.execute_trade(trade_value):
                break

# Initialize PTM with a balance of 10000
ptm = PTM(10000)

# Execute trades with a value of 100, 200 times
ptm.increase_trade_frequency(100, 200)

print(f"Trades executed: {ptm.trades_executed}")
```

In this example, the `increase_trade_frequency` method attempts to execute a trade with a certain value a specified number of times. If the balance is insufficient to execute a trade, it stops trading.

Please note that more trades do not necessarily mean more chances of winning. It's important to have a good trading strategy that takes into account factors such as market conditions, risk management, etc.