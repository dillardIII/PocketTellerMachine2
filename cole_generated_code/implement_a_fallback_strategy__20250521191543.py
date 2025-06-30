from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can help with that. However, I need to know what you want to do when no backtest results are found. Do you want to return a default value, raise an exception, or something else? Here's a simple example of how you might structure your code to handle this situation:

```python
def backtest(strategy):
    # Run backtest
    results = strategy.run_backtest()

    # Check if results are empty
    if not results:
        # Fallback strategy: return a default value, raise an exception, etc.
        print("No backtest results found. Implementing fallback strategy.")
        return None  # Or whatever your fallback strategy is

    return results
```

In this example, the `backtest` function runs a backtest using the given strategy. If the results are empty (i.e., if `not results` is `True`), then it implements a fallback strategy. In this case, the fallback strategy is to print a message and return `None`, but you can replace this with whatever you want.