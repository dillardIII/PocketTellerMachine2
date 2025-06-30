from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of how you might implement a fallback strategy in Python. In this case, if no backtest results are found, the function will return a message notifying the user.

```python
def backtest_strategy(strategy):
    # Assume get_backtest_results is a function that returns backtest results for a given strategy
    backtest_results = get_backtest_results(strategy)

    if not backtest_results:
        # Fallback strategy: Notify the user when no backtest results are found
        return "No backtest results found for the given strategy. Please try another strategy."

    # If backtest results are found, process and return them
    process_backtest_results(backtest_results)

def get_backtest_results(strategy):
    # This function should return the backtest results for the given strategy
    # For the sake of this example, we'll assume it returns None
    return None

def process_backtest_results(results):
    # This function should process the backtest results
    # For the sake of this example, we'll assume it does nothing
    pass

# Test the function with a strategy
print(backtest_strategy("Strategy 1"))
```

In this example, the `backtest_strategy` function attempts to get backtest results for a given strategy. If no results are found (i.e., `get_backtest_results` returns `None` or an empty list), it falls back to returning a notification message. If results are found, it processes and returns them.