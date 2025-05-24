Sure, here is a simple way to implement that in Python. You could do this with an `if` clause to check if backtest results exist or not. If they don't exist, it should trigger the fallback strategy.

Assuming `backtest_results` is the variable storing the backtest results.

```python
if not backtest_results:
    # Implement fallback strategy
    print("No backtest results found. Implementing fallback strategy...")
    fallback_strategy()
else:
    # Continue with existing backtest results
    print("Backtest results found. Continue processing...")
    process_backtest_results(backtest_results)

    
def fallback_strategy():
    # code for fallback strategy
    print("Fallback strategy in action...")
    pass

def process_backtest_results(results):
    # code to process the backtest results
    print("Processing backtest results...")
    pass
```
 
In this example code, replace `fallback_strategy` and `process_backtest_results` functions with your actual strategies or procedures.

Please note, this is a simple example and the actual implementation can differ based on how your trading system is designed.