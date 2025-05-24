Here is a simple Python code that sets specific trading goals for the day. This code sets a goal for the number of trades to be made in a day and keeps track of the number of trades made. Once the goal is reached, it prints a congratulatory message.

```python
class PTM:
    def __init__(self, goal):
        self.goal = goal
        self.trades_made = 0

    def make_trade(self):
        self.trades_made += 1
        if self.trades_made >= self.goal:
            print("Congratulations! You've reached your trading goal for the day!")
        else:
            print(f"You've made {self.trades_made} trades today. Keep going!")

# Set a goal of 10 trades for the day
ptm = PTM(10)

# Simulate making trades
for _ in range(12):
    ptm.make_trade()
```

In this code, the `PTM` class has a `goal` attribute for the trading goal and a `trades_made` attribute to keep track of the number of trades made. The `make_trade` method increments `trades_made` and checks if the goal has been reached.

Please note that this is a very basic example and a real-world trading system would be much more complex, involving real-time data feeds, order management, risk checks, and possibly machine learning algorithms for making trading decisions.