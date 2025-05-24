Sure, here's a simple Python code snippet that implements a fallback strategy when no backtest results are found. I'm assuming that you have a function called `run_backtest()` which returns the backtest results, and a function called `fallback_strategy()` which is the fallback strategy you want to implement.

```python
def get_backtest_results():
    try:
        # Try to get backtest results
        results = run_backtest()
        
        # If no results are found, raise an exception
        if not results:
            raise ValueError("No backtest results found.")
            
    except ValueError as e:
        print(e)
        
        # Run fallback strategy
        results = fallback_strategy()
        
    return results

def run_backtest():
    # Your code to run backtest goes here
    pass

def fallback_strategy():
    # Your code for fallback strategy goes here
    pass
```

In this code, `get_backtest_results()` is the main function you'd call to get the backtest results. It first tries to get the results from `run_backtest()`. If no results are found (i.e., if `results` is empty), it raises a `ValueError`. This error is then caught in the `except` block, where it prints the error message and then runs the fallback strategy by calling `fallback_strategy()`. The results of the fallback strategy are then returned.