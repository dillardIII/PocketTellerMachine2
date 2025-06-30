from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can help with that. However, I need more context to provide a more accurate solution. Here is a general example of how you might handle a situation where no backtest results are found.

```python
def backtest(strategy):
    # This is just an example. Your backtest function might be different.
    results = strategy.run_backtest()

    if not results:
        print("No backtest results found. Falling back to default strategy.")
        default_strategy = DefaultStrategy()
        results = default_strategy.run_backtest()

    return results
```

In this example, if the `run_backtest` method of a strategy returns an empty result (which could be a list, dictionary, etc. depending on your implementation), we print a message and then run a default strategy instead. 

Please note that you would need to replace `strategy.run_backtest()` and `DefaultStrategy().run_backtest()` with your actual backtest execution code. Also, you would need to define what your `DefaultStrategy` is.