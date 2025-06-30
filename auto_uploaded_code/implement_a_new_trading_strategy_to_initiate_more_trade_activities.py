from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, below is a very simple example of a Python script that simulates a trading strategy. 

This script monitors the price of a stock and decides to buy or sell based on simple conditions: If the price drops below a certain level, it's time to buy. If it raises above a certain level, it's time to sell.

```python
import random
import time

class TradeBot:
    def __init__(self, balance=1000.0, stock=0.0):
        self.balance = balance
        self.stock = stock

    def buy(self, price):
        if self.balance > price:
            self.stock += 1
            self.balance -= price
            print(f'Bought stock at ${price:.2f}')
            print(f'Current Balance: ${self.balance:.2f}\n')

    def sell(self, price):
        if self.stock > 0:
            self.stock -= 1
            self.balance += price
            print(f'Sold stock at ${price:.2f}')
            print(f'Current Balance: ${self.balance:.2f}\n')

    def start_trading(self, low_price=5.0, high_price=20.0):
        while True:
            current_price = random.uniform(low_price, high_price)

            if current_price <= 7.0:
                self.buy(current_price)

            elif current_price >= 15.0:
                self.sell(current_price)

            print(f'Stock Price: ${current_price:.2f}')
            print(f'Stocks: {self.stock}\n')

            time.sleep(1) # Wait for 1 second

# Create a new TradeBot and start trading
bot = TradeBot()
bot.start_trading()
```
Please note that it is a very basic and naive implementation of a trading strategy and serving for demonstration. In a real-world application, you need to consider a lot of other factors like market trends, company performance data, order sizing and much more. Also, in real-world trading applications, prices are obtained from live feeds and execution of trades are done via APIs connected to an exchange/brokerage-service.

If you're interested you may want to look into libraries like backtrader or pyalgotrade, which allow backtesting of trading strategies, provide a wealth of indicators, and can connect to live data feeds.