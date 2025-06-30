from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that sets specific trading goals for the day:

```python
class TradingGoals:
    def __init__(self, initial_investment, target_profit, target_trades):
        self.initial_investment = initial_investment
        self.target_profit = target_profit
        self.target_trades = target_trades

    def display_goals(self):
        print(f"Today's Trading Goals:")
        print(f"Initial Investment: ${self.initial_investment}")
        print(f"Target Profit: ${self.target_profit}")
        print(f"Target Number of Trades: {self.target_trades}")

# Set today's trading goals
today_goals = TradingGoals(1000, 200, 10)
today_goals.display_goals()
```

In this code, we define a class `TradingGoals` with an initializer method that sets the initial investment, target profit, and target number of trades for the day. We also have a method `display_goals` that prints out these goals.

Then, we create an instance of `TradingGoals` for today's goals and call `display_goals` to display them.

Please note that this is a very basic example. In a real-world application, you would likely want to include more complex logic, such as checking if the goals are realistic or adjusting the goals based on market conditions.