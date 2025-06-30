from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of how you might implement a fallback strategy in Python when no backtest results are found. In this case, the fallback strategy is to print a message and return an empty list.

```python
def get_backtest_results():
    # This is a placeholder for where you'd get your backtest results.
    # Replace this with your actual code.
    backtest_results = []

    if not backtest_results:
        print("No backtest results found. Falling back to default strategy.")
        return []

    return backtest_results

# Call the function
results = get_backtest_results()
if not results:
    # Implement your fallback strategy here.
    print("Fallback strategy activated.")
```

In this code, `get_backtest_results` is a function that is supposed to return backtest results. If it doesn't find any (i.e., if `backtest_results` is empty), it prints a message and returns an empty list.

Then, when you call `get_backtest_results`, you check if `results` is empty. If it is, you print a message saying that the fallback strategy has been activated. You can replace this print statement with whatever your actual fallback strategy is.