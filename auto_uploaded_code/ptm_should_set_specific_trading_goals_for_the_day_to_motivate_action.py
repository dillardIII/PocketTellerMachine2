Sure, I can help you write a simple Python code that sets specific trading goals for the day. Please note that this is a basic example and in real trading scenarios, goals would be set based on complex algorithms and market analysis.

```python
class PTM:
    def __init__(self):
        self.trading_goals = {}

    def set_trading_goal(self, stock, goal):
        self.trading_goals[stock] = goal

    def get_trading_goals(self):
        return self.trading_goals

# Create an instance of PTM
ptm = PTM()

# Set trading goals for the day
ptm.set_trading_goal('AAPL', 'Buy 50 shares')
ptm.set_trading_goal('GOOG', 'Sell 30 shares')
ptm.set_trading_goal('AMZN', 'Buy 10 shares')

# Get trading goals for the day
print(ptm.get_trading_goals())
```

This script creates a class `PTM` with methods to set and get trading goals. The goals are stored in a dictionary where the keys are the stock symbols and the values are the goals. You can set goals by calling the `set_trading_goal` method with the stock symbol and the goal as arguments. You can get all the goals by calling the `get_trading_goals` method.