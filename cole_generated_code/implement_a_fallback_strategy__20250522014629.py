from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of how you might implement a fallback strategy when no backtest results are found. In this case, the fallback strategy is to simply print a message and return an empty list. 

```python
def backtest_strategy(strategy):
    # Assume get_backtest_results is a function that returns backtest results for a given strategy
    backtest_results = get_backtest_results(strategy)
    
    if not backtest_results:
        print("No backtest results found. Implementing fallback strategy.")
        return []
    
    return backtest_results

def get_backtest_results(strategy):
    # This function should implement the logic to get backtest results for a given strategy
    # For now, let's assume it returns an empty list
    return []
```

You can replace the print statement and the return statement in the if condition with any fallback strategy you want to implement. For example, you might want to run a different strategy, or you might want to raise an exception. The specific fallback strategy would depend on your specific use case.