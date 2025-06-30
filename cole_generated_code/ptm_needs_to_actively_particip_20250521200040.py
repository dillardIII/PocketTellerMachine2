from ghost_env import INFURA_KEY, VAULT_ADDRESS
To complete this task, we need to create a simple trading system. This system will keep track of our trades and calculate our wins and losses. Here is a simple Python code to do this:

```python
class Trade:
    def __init__(self, buy_price, sell_price, shares):
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.shares = shares

    def profit(self):
        return (self.sell_price - self.buy_price) * self.shares

class PTM:
    def __init__(self):
        self.trades = []

    def add_trade(self, buy_price, sell_price, shares):
        trade = Trade(buy_price, sell_price, shares)
        self.trades.append(trade)

    def total_profit(self):
        total = 0
        for trade in self.trades:
            total += trade.profit()
        return total

# Create PTM instance
ptm = PTM()

# Add trades
ptm.add_trade(10, 15, 100)  # Bought at $10, sold at $15, 100 shares
ptm.add_trade(20, 18, 50)   # Bought at $20, sold at $18, 50 shares

# Calculate total profit
print("Total profit: $", ptm.total_profit())
```

In this code, we have two classes: `Trade` and `PTM`. `Trade` represents a single trade, with a buy price, sell price, and number of shares. It has a method `profit` to calculate the profit of the trade.

`PTM` represents our trading system. It has a list of trades and a method to add new trades. It also has a method `total_profit` to calculate the total profit from all trades.

We create an instance of `PTM`, add some trades, and then calculate the total profit.