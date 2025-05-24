Sure, here's a simple Python code snippet that could be used to initiate a trade. This code assumes that you have a function called `evaluate_strategy` which determines the effectiveness of the current strategy.

```python
class PTM:
    def __init__(self):
        self.trades = 0

    def initiate_trade(self, strategy):
        # Initiate a trade based on the given strategy
        print(f"Initiating trade with {strategy} strategy...")
        self.trades += 1

        # Evaluate the effectiveness of the current strategy
        effectiveness = self.evaluate_strategy(strategy)

        print(f"The effectiveness of the {strategy} strategy is {effectiveness}.")

    def evaluate_strategy(self, strategy):
        # This function should contain the logic to evaluate the effectiveness of the strategy
        # For now, it just returns a placeholder value
        return "placeholder value"

# Create a PTM object
ptm = PTM()

# Initiate a trade using the "buy low, sell high" strategy
ptm.initiate_trade("buy low, sell high")
```

Please note that this is a very simplified example. In a real-world application, the `initiate_trade` function would likely involve interacting with a trading API to actually execute the trade, and the `evaluate_strategy` function would involve some form of data analysis to determine the effectiveness of the strategy.