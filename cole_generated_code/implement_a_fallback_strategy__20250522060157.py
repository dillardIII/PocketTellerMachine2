Sure, here is a simple implementation of a fallback strategy when no backtest results are found. In this case, I will assume that backtest results are stored in a list. If the list is empty, then we will execute the fallback strategy.

```python
# Let's assume backtest_results is a list containing our backtest results
backtest_results = []

def fallback_strategy():
    print("No backtest results found. Executing fallback strategy...")
    # Implement your fallback strategy here

if not backtest_results:
    fallback_strategy()
else:
    print("Backtest results found. Proceeding with the normal strategy...")
    # Implement your normal strategy here
```

The code checks if the `backtest_results` list is empty. If it is, it calls the `fallback_strategy()` function, which is where you would implement your fallback strategy. If the `backtest_results` list is not empty, it proceeds with the normal strategy.

Please replace the print statements and comments with the actual code for your strategies.