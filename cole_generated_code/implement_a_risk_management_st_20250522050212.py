Sure, here's a simple Python code that implements a risk management strategy using stop loss and take profit levels. This strategy is commonly used in trading to minimize potential losses and secure profits.

```python
class RiskManagement:
    def __init__(self, balance, stop_loss_percent, take_profit_percent):
        self.balance = balance
        self.stop_loss_percent = stop_loss_percent
        self.take_profit_percent = take_profit_percent

    def calculate_stop_loss(self, entry_price):
        return entry_price - (entry_price * self.stop_loss_percent / 100)

    def calculate_take_profit(self, entry_price):
        return entry_price + (entry_price * self.take_profit_percent / 100)

    def execute_trade(self, entry_price, current_price):
        stop_loss = self.calculate_stop_loss(entry_price)
        take_profit = self.calculate_take_profit(entry_price)

        if current_price <= stop_loss:
            print("Stop loss triggered. Sell at: ", current_price)
            self.balance += entry_price - current_price
        elif current_price >= take_profit:
            print("Take profit triggered. Sell at: ", current_price)
            self.balance += current_price - entry_price
        else:
            print("Hold position. Current price: ", current_price)

        print("Current balance: ", self.balance)


# Initialize risk management strategy with a balance of 10000, stop loss at 10% and take profit at 20%
risk_management = RiskManagement(10000, 10, 20)

# Assume we enter a trade at a price of 100
entry_price = 100

# If the current price drops to 90, stop loss will be triggered
risk_management.execute_trade(entry_price, 90)

# If the current price rises to 120, take profit will be triggered
risk_management.execute_trade(entry_price, 120)
```

This code is a very simple representation of a risk management strategy. In real trading, you would need to consider more factors such as transaction fees, the volatility of the market, the size of your positions, etc.