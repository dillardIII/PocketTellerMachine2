from ghost_env import INFURA_KEY, VAULT_ADDRESS
To implement a fallback strategy when no backtest results are found, we will use Python's exception handling.

Here we assume:
1. `backtest()` is the function conducting the backtest and returning the result. It returns `None` when no backtests are found.
2. `fallback_strategy()` is the function conducting the fallback strategy in case no backtest results are found.

```python
def run_backtest():
    try:
        # Run the backtest
        result = backtest()

        # If result is None, raise an exception
        if result is None:
            raise Exception("No backtest results found")
    except Exception as err:
        # In case of any error, print the error and run the fallback strategy
        print(f"Error: {err}")
        print("Running fallback strategy...")
        result = fallback_strategy()

    return result

def backtest():
    # In real cases, the content of this function would include your backtesting process
    # This function returns None means no backtest was found
    return None

def fallback_strategy():
    # In real cases, the content of this function would include your fallback strategy process

    return "Running fallback strategy successfully"

# Run the backtest
result = run_backtest()
print(result)
```

Please adjust these codes to align with your actual Zenbot trading system as needed. The backtest or fallback strategy functions would obviously be much more complex in real use cases.