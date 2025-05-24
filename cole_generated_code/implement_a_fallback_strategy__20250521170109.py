Sure, using exception handling in Python can help us establish this fallback strategy. Here is an example of how it might look like:

```python
def backtest_strategy(strategy):
    try:
        # Your actual backtest logic goes here
        results = backtest(strategy)
    except Exception as e:
        # Print the error
        print("Error occurred during backtesting: ", e)
        # Fallback strategy
        results = fallback_strategy(strategy)

    # Print or return the backtest results
    return results

def backtest(strategy):
    # Your actual backtest logic which may vary based on the kind of strategy
    # Raise an exception if no results found
    results = None
    if not results:
        raise Exception("No backtest results found")
    return results

def fallback_strategy(strategy):
    # Here define your fallback strategy when no backtest results are found
    # This could include re-running the strategy with simpler parameters or a totally different strategy altogether
    results = "Fallback results"
    return results
```
This is just a skeleton code and you can definitely fill in the rest based on your actual backtest logic, strategies and what to do when no backtest results are found.