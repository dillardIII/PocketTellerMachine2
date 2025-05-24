Sure, here is a simple implementation of a fallback strategy in Python:

```python
def backtest_strategy(strategy):
    try:
        # Execute backtest
        results = strategy.backtest()
        
        # Check if results are empty
        if not results:
            raise ValueError('No backtest results found')
        
        return results
    except ValueError as e:
        print(e)
        print('Executing fallback strategy...')
        
        # Fallback strategy
        fallback_results = strategy.fallback()
        
        return fallback_results
```

In this code, we first attempt to execute the backtest for a given strategy. If no results are found (i.e., the results are empty), we raise a `ValueError`. This error is then caught in the `except` block, where we print a message and execute the fallback strategy. The results of the fallback strategy are then returned.

Please note that this code assumes that your `strategy` object has `backtest` and `fallback` methods that return the backtest results. If your implementation is different, you may need to adjust the code accordingly.