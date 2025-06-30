from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python function that implements a fallback strategy when no backtest results are found. This function assumes that you have a function named `run_backtest()` that runs the backtest and returns results. If no results are found, it falls back to a default strategy.

```python
def backtest_with_fallback():
    # Run the backtest
    results = run_backtest()

    # Check if results are empty
    if not results:
        print("No backtest results found. Falling back to default strategy.")
        
        # Define your default strategy here
        default_strategy = {
            'buy': ['AAPL', 'GOOGL', 'AMZN'],
            'sell': ['TSLA', 'FB']
        }
        
        return default_strategy

    return results
```

Please replace the `run_backtest()` function and `default_strategy` with your actual backtest function and fallback strategy.