from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can help you write a simple Python code to simulate a trade. However, please note that this is just a simulation and should not be used for real trading. 

```python
class Trade:
    def __init__(self, balance):
        self.balance = balance

    def buy(self, price):
        if self.balance < price:
            print("Insufficient balance to initiate trade.")
        else:
            self.balance -= price
            print(f"Trade initiated. Bought at {price}. Current balance is {self.balance}.")

    def sell(self, price):
        self.balance += price
        print(f"Trade completed. Sold at {price}. Current balance is {self.balance}.")

# Initialize PTM with a balance of 10000
ptm = Trade(10000)

# PTM buys at 5000
ptm.buy(5000)

# PTM sells at 6000
ptm.sell(6000)
```

In this code, we have a `Trade` class with `buy` and `sell` methods. The `buy` method is used to initiate a trade and the `sell` method is used to complete a trade. We create an instance of `Trade` with an initial balance of 10000. Then, we simulate a trade where PTM buys at 5000 and sells at 6000.