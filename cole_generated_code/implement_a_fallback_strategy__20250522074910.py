Sure, here is a simple Python function that implements a fallback strategy for when no backtest results are found. This function, `get_backtest_results`, takes in a `backtest_id` as an argument. If no results are found for the given `backtest_id`, it falls back to a default strategy.

```python
def get_backtest_results(backtest_id):
    # Assuming that get_results is a function that retrieves backtest results
    # based on a given backtest_id
    try:
        results = get_results(backtest_id)
    except Exception as e:
        print(f"No backtest results found for {backtest_id}. Falling back to default strategy.")
        results = get_results('default')
    return results
```

In this code, if the `get_results` function raises an exception (which we assume happens when no results are found for a given `backtest_id`), we catch that exception and print a message indicating that we're falling back to a default strategy. We then get the results for the 'default' backtest_id.

Please note that this is a simplified example. The actual implementation will depend on how your backtesting system is set up and how it handles cases where no results are found.