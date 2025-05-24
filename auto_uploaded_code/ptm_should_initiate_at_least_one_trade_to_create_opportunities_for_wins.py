Here's a simple Python code to simulate a trading bot. This bot will initiate at least one trade when the price of a stock reaches a certain threshold. Please note that this is a very basic example and real-world trading bots are much more complex and involve more sophisticated algorithms.

```python
class PTM:
    def __init__(self, initial_balance=1000):
        self.balance = initial_balance
        self.stock = 0

    def buy(self, price):
        if self.balance > price:
            self.stock += 1
            self.balance -= price
            print(f'Bought stock for {price}. Current balance: {self.balance}')

    def sell(self, price):
        if self.stock > 0:
            self.stock -= 1
            self.balance += price
            print(f'Sold stock for {price}. Current balance: {self.balance}')

    def trade(self, current_price):
        if current_price < 100:
            self.buy(current_price)
        elif current_price > 150:
            self.sell(current_price)


# Initialize PTM
ptm = PTM()

# Simulate price changes
prices = [120, 90, 160, 140, 180]

for price in prices:
    ptm.trade(price)
```

In this code, we first create a PTM class with `buy`, `sell` and `trade` methods. The `trade` method decides whether to buy or sell based on the current price. If the price is less than 100, it buys a stock, and if the price is more than 150, it sells a stock. We then simulate price changes and call the `trade` method for each price.

Please note that this code does not take into account transaction fees and other aspects of trading. It's a very simplified example and should not be used for real trading.