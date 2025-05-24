When implementing a fallback strategy for when no backtest results are found it can be handled through exceptions in Python. Here is how you could do it:

```python
class NoBacktestResultsFound(Exception):
    """Raised when no backtest results are found."""
    pass

def backtest_strategy(strategy):
    try:
        # Assume backtest function that returns list of backtest results.
        backtest_results = backtest(strategy) 
        
        if not backtest_results:
            raise NoBacktestResultsFound

        return backtest_results

    except NoBacktestResultsFound:
        print('No backtest results found for the strategy.')
        # Here we implement fallback strategy
        # It can be anything depending on your app's requirements
        # For instance, we could retry backtesting with a default strategy
        print('Falling back to default strategy')
        default_strategy = 'Default Strategy'
        backtest_results = backtest(default_strategy)
        return backtest_results

    except Exception as e:
        print(f'An error occurred: {str(e)}')
        # In case of any other exceptions, return empty list or do something else
        return []
```

In the above code, we assume that `backtest()` function is responsible for backtesting the strategy and returning the results. It might be different in your use case, so please adjust accordingly.