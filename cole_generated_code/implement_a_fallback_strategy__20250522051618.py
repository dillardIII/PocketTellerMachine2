from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of how you could implement a fallback strategy in Python when no backtest results are found.

```python
class Backtest:
    def __init__(self):
        self.results = None

    def run_backtest(self):
        # Run your backtest here
        # If successful, assign the results to self.results
        pass

    def get_results(self):
        if self.results is None:
            print("No backtest results found. Running fallback strategy.")
            self.fallback_strategy()
        else:
            return self.results

    def fallback_strategy(self):
        # Implement your fallback strategy here
        print("Running fallback strategy...")
        pass

# Usage
backtest = Backtest()
backtest.run_backtest()
results = backtest.get_results()
```

In this example, when you try to get the results of the backtest, it checks if the results exist. If not, it prints a message and runs the fallback strategy. You would need to implement the `run_backtest` and `fallback_strategy` methods according to your requirements.