Sure, here's a simple Python function that implements a fallback strategy for when no backtest results are found. In this case, the fallback strategy is to print a message and return an empty dictionary.

```python
def get_backtest_results(backtest_id):
    # This is a placeholder for the actual code to get backtest results
    # In a real-world scenario, you would replace this with actual code
    backtest_results = {}

    # Check if the backtest results are empty
    if not backtest_results:
        print(f"No backtest results found for id: {backtest_id}")
        # Fallback strategy: return an empty dictionary
        return {}

    # If backtest results are found, return them
    return backtest_results
```

This is a very basic fallback strategy. Depending on the specifics of your trading system, you might want to implement a more complex fallback strategy. For example, you could try to re-run the backtest, fetch results from a different source, or use some default results.