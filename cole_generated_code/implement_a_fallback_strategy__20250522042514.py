from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code to implement a fallback strategy when no backtest results are found. The fallback strategy can be customized according to your needs. In this example, I will just print a message and return an empty dictionary.

```python
def get_backtest_results(backtest_id):
    # This is a placeholder for the actual code to get backtest results
    # Let's assume it returns a dictionary with backtest results
    results = {}

    # Check if the results are empty
    if not results:
        print("No backtest results found for id: ", backtest_id)
        # Fallback strategy: return an empty dictionary
        return {}

    return results

# Test the function
print(get_backtest_results('123'))
```

In this code, the function `get_backtest_results` is supposed to return the backtest results for a given `backtest_id`. If the results are empty (which is simulated by an empty dictionary `results`), it prints a message and returns an empty dictionary as a fallback strategy.