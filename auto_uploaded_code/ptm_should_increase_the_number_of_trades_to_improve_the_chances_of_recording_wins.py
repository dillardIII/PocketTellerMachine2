To increase the number of trades, you could modify the trading algorithm to reduce the threshold for making a trade. However, it's important to note that increasing the number of trades doesn't necessarily improve the chances of recording wins. It could also increase the chances of recording losses. Here's a simple example of how you might modify a hypothetical trading algorithm:

```python
class PTM:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.trades = 0

    def trade(self, market):
        # Let's say the market is a list of price changes
        for change in market:
            # Originally, we might only trade if the price change is above a certain threshold
            # To increase the number of trades, we could lower this threshold
            # For example, let's say the original threshold was 0.05
            # We could lower it to 0.01 to increase the number of trades
            if abs(change) > 0.01:
                self.trades += 1
                # Then we would apply some trading logic here
                # For example, if the price is going up, we might buy
                # If the price is going down, we might sell
                if change > 0:
                    self.buy()
                else:
                    self.sell()

    def buy(self):
        # Buying logic here
        pass

    def sell(self):
        # Selling logic here
        pass
```

This is a very simplified example and real trading algorithms would be much more complex. They would take into account many more factors and use more sophisticated methods to decide when to trade.