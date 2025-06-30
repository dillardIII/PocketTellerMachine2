from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python script that sets trading goals for the day. This script assumes that you have a `Trader` class with methods for setting and getting trading goals.

```python
class Trader:
    def __init__(self, name):
        self.name = name
        self.trading_goals = 0

    def set_trading_goals(self, goals):
        self.trading_goals = goals
        print(f"Trading goals for {self.name} set to {self.trading_goals} for the day.")

    def get_trading_goals(self):
        return self.trading_goals

# Create an instance of Trader for PTM
ptm = Trader("PTM")

# Set trading goals for the day
ptm.set_trading_goals(10)

# Get trading goals for the day
print(f"Trading goals for PTM today: {ptm.get_trading_goals()}")
```

In this script, `Trader` is a class that represents a trader. Each `Trader` has a `name` and `trading_goals` which represents their trading goals for the day.

The `set_trading_goals` method sets the trading goals for the day, and the `get_trading_goals` method returns the current trading goals.

The script then creates a `Trader` named PTM and sets their trading goals for the day to 10. It then prints out the trading goals for PTM.

Please note that this is a very basic script and a real-world trading system would be much more complex, likely involving real-time data feeds, complex algorithms for deciding when to buy and sell, and much more.