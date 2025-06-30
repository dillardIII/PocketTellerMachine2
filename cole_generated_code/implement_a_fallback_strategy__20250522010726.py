from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, to implement a fallback strategy when no backtest results are found, we can use exception handling in Python. Here is a simple example:

```python
class Backtest:
    def __init__(self):
        self.results = None

    def run_backtest(self):
        # Code to run backtest
        # This should update self.results with the backtest results
        pass

    def get_results(self):
        if self.results is None:
            raise Exception('No backtest results found.')

        return self.results

# Create a Backtest instance
backtest = Backtest()

try:
    # Try to get the backtest results
    results = backtest.get_results()
except Exception as e:
    # If no results are found, implement fallback strategy
    print(str(e))
    print('Implementing fallback strategy...')
    # Code for fallback strategy
```

In this code, we have a `Backtest` class with methods to run a backtest and get the results. If no results are found when trying to get the results, it raises an exception. We then catch this exception and implement the fallback strategy.

Please replace the `# Code to run backtest` and `# Code for fallback strategy` comments with the actual code to run the backtest and the fallback strategy.