Sure, here's a simple Python function that implements a fallback strategy when no backtest results are found.

```python
def backtest_strategy(data):
    try:
        # Assume backtest() is a function that performs backtesting and returns results
        results = backtest(data)
        if not results:
            raise ValueError("No backtest results found")
        return results
    except ValueError as e:
        print(e)
        # Fallback strategy
        print("Implementing fallback strategy...")
        # Assume fallback_strategy() is a function that performs the fallback strategy
        fallback_results = fallback_strategy(data)
        return fallback_results
```

In this code, the `backtest_strategy` function tries to perform backtesting on the provided data. If no results are found (i.e., `results` is empty), it raises a `ValueError`. This error is caught in the `except` block, where it prints the error message and then implements the fallback strategy by calling `fallback_strategy(data)`. 

Please note that you need to replace `backtest(data)` and `fallback_strategy(data)` with your actual backtesting and fallback strategy functions.