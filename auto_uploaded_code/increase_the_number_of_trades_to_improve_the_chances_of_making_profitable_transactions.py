from ghost_env import INFURA_KEY, VAULT_ADDRESS
In order to increase the number of trades, you can create a loop that will execute trades more frequently. However, please note that increasing the number of trades doesn't necessarily guarantee more profitable transactions. 

Here is a simple example of how you can increase the number of trades using Python. This example assumes that you have a function called `execute_trade()` that performs a single trade:

```python
def increase_trades(num_trades):
    for _ in range(num_trades):
        execute_trade()
```

In this code, `num_trades` is the number of trades you want to execute. You can call this function with the desired number of trades as follows:

```python
increase_trades(100)  # Execute 100 trades
```

Please note that this is a very simplified example. In a real-world scenario, you would need to consider many other factors such as market conditions, available capital, risk management, etc. Also, the `execute_trade()` function would need to be defined to actually perform a trade, which would typically involve making a request to a trading API.