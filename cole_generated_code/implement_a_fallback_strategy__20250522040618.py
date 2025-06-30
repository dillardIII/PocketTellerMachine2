from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code snippet that implements a fallback strategy when no backtest results are found. This code assumes that you have a function `run_backtest()` that runs the backtest and returns the results. If no results are found, the fallback strategy is to run a default backtest and return those results.

```python
def get_backtest_results():
    results = run_backtest()
    if not results:
        print("No backtest results found. Running default backtest...")
        results = run_default_backtest()
    return results

def run_backtest():
    # Your code to run the backtest goes here
    # This function should return the backtest results if successful, or None if no results are found
    pass

def run_default_backtest():
    # Your code to run a default backtest goes here
    # This function should return the default backtest results
    pass
```

Please replace the `run_backtest()` and `run_default_backtest()` functions with your actual backtest running code.