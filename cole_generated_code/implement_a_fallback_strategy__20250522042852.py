from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple implementation of a fallback strategy for when no backtest results are found. This code assumes that you have a function called `run_backtest()` which returns the backtest results, and a function called `fallback_strategy()` which is your fallback strategy when no backtest results are found.

```python
def get_backtest_results():
    results = run_backtest()  # function to run backtest and get results

    # check if results are empty
    if not results:
        print("No backtest results found. Running fallback strategy...")
        results = fallback_strategy()  # function to run fallback strategy

    return results

def run_backtest():
    # Your code to run backtest here
    # Return the results
    pass

def fallback_strategy():
    # Your code for fallback strategy here
    # Return the results
    pass
```

You can replace the `run_backtest()` and `fallback_strategy()` functions with your actual implementation. The `get_backtest_results()` function will first try to get the backtest results. If no results are found, it will run the fallback strategy and return those results.