Here is a simple Python code that simulates a basic trading strategy. This strategy buys when the price is low and sells when the price is high. Please note that this is a very simplified version of a trading strategy and real-world trading involves a lot more factors and complex algorithms.

```python
class TradingStrategy:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.stock = 0

    def buy(self, price):
        if self.balance > price:
            self.stock += 1
            self.balance -= price
            print(f"Bought stock for {price}. Current balance: {self.balance}")

    def sell(self, price):
        if self.stock > 0:
            self.stock -= 1
            self.balance += price
            print(f"Sold stock for {price}. Current balance: {self.balance}")

    def implement_strategy(self, prices):
        for price in prices:
            if price < 50:  # Buy condition
                self.buy(price)
            elif price > 100:  # Sell condition
                self.sell(price)


# Initialize trading with a balance of 1000
trading = TradingStrategy(1000)

# Simulate prices
prices = [40, 45, 50, 55, 100, 105, 110]

# Implement trading strategy
trading.implement_strategy(prices)
```

In this code, we create a `TradingStrategy` class that has methods to buy and sell stocks based on their prices. The `implement_strategy` method goes through a list of prices and decides whether to buy or sell based on the price.

Please note that this is a very basic trading strategy and real-world trading strategies are much more complex and take into account many other factors.