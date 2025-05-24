Here is a simple Python code that implements a risk management strategy. This strategy is based on setting a stop loss level for each trade. If the price falls to this level, the trade is automatically closed to prevent further losses.

```python
class Trade:
    def __init__(self, symbol, entry_price, quantity):
        self.symbol = symbol
        self.entry_price = entry_price
        self.quantity = quantity
        self.stop_loss = self.set_stop_loss()

    def set_stop_loss(self, risk_percent=0.02):
        """Set stop loss level based on risk tolerance"""
        return self.entry_price * (1 - risk_percent)

    def check_trade(self, current_price):
        """Check if the trade should be closed based on current price"""
        if current_price <= self.stop_loss:
            return self.close_trade(current_price)
        return "Trade is still open"

    def close_trade(self, current_price):
        """Close the trade and calculate the loss"""
        loss = (self.entry_price - current_price) * self.quantity
        return f"Trade closed. Loss: {loss}"

# Example usage
trade = Trade("AAPL", 150, 10)
print(trade.check_trade(145))
```

In this code, a `Trade` class is defined with methods to set a stop loss level, check if the trade should be closed, and close the trade. The stop loss level is set as a certain percentage below the entry price, which can be adjusted based on your risk tolerance. When the `check_trade` method is called with the current price, it checks if this price is below the stop loss level. If it is, the trade is closed and the loss is calculated.

Please note that this is a very basic risk management strategy and may not be suitable for all trading scenarios. You might want to consider other factors such as the volatility of the asset, your overall portfolio risk, etc. when implementing a real-world risk management strategy.