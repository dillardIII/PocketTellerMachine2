Sure, here's a simple Python script that simulates a trade initiation. This script doesn't connect to any real trading platform, it's just an example of how you could structure your code. In a real-world scenario, you would need to use a trading API to execute trades.

```python
class Trade:
    def __init__(self, symbol, quantity, trade_type):
        self.symbol = symbol
        self.quantity = quantity
        self.trade_type = trade_type

class PTM:
    def __init__(self):
        self.trades = []

    def initiate_trade(self, trade):
        self.trades.append(trade)
        print(f"Trade initiated: {trade.trade_type} {trade.quantity} {trade.symbol}")

# Create PTM instance
ptm = PTM()

# Create a trade
trade = Trade("AAPL", 100, "BUY")

# Initiate the trade
ptm.initiate_trade(trade)
```

In this script, we define two classes: `Trade` and `PTM`. `Trade` represents a single trade, with a symbol (the stock to be traded), quantity (the number of shares to trade), and trade_type (whether it's a buy or sell order). `PTM` represents the trading system, with a list of trades it has initiated.

To initiate a trade, we create a `Trade` instance and pass it to `PTM`'s `initiate_trade` method. This method adds the trade to `PTM`'s list of trades and prints a message indicating that the trade has been initiated.