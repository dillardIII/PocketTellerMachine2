from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code that simulates the initiation of 5 trades. In a real-world scenario, you would need to integrate this with a trading API to actually execute the trades.

```python
import random

class Trade:
    def __init__(self, trade_id, stock, quantity):
        self.trade_id = trade_id
        self.stock = stock
        self.quantity = quantity

class PTM:
    def __init__(self):
        self.trades = []

    def initiate_trade(self, trade):
        self.trades.append(trade)
        print(f"Trade initiated: {trade.trade_id} - Buying {trade.quantity} of {trade.stock}")

# List of stocks to trade
stocks = ['AAPL', 'GOOG', 'TSLA', 'AMZN', 'MSFT']

# Create PTM instance
ptm = PTM()

# Initiate 5 trades
for i in range(1, 6):
    stock = random.choice(stocks)
    quantity = random.randint(1, 100)
    trade = Trade(i, stock, quantity)
    ptm.initiate_trade(trade)
```

This code creates a `Trade` class to represent a trade, and a `PTM` class to represent the trading system. The `PTM` class has a method `initiate_trade` to initiate a new trade.

The code then creates a list of stocks to trade, creates an instance of `PTM`, and initiates 5 trades with random stock and quantity. Each time a trade is initiated, a message is printed to the console.