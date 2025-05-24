Here is a simple example of how you can simulate a trading bot in Python. This bot will randomly decide whether to buy or sell a stock, and then learn from the outcome of that decision. This is a very basic example and in a real-world scenario, you would want your bot to make decisions based on more sophisticated algorithms and data analysis.

```python
import random

class TradingBot:
    def __init__(self):
        self.balance = 1000.0  # starting balance
        self.stocks = 0  # starting stocks
        self.stock_price = 100.0  # starting stock price

    def trade(self):
        # Randomly decide whether to buy or sell
        action = random.choice(['buy', 'sell'])

        # If the bot decides to buy
        if action == 'buy':
            if self.balance > self.stock_price:
                self.stocks += 1
                self.balance -= self.stock_price
                print(f"Bought 1 stock for {self.stock_price}. Balance is now {self.balance}")

        # If the bot decides to sell
        elif action == 'sell':
            if self.stocks > 0:
                self.stocks -= 1
                self.balance += self.stock_price
                print(f"Sold 1 stock for {self.stock_price}. Balance is now {self.balance}")

        # Update the stock price randomly
        self.stock_price += random.uniform(-10, 10)

    def learn(self):
        # In this simple example, the bot doesn't actually learn anything
        # In a real-world scenario, you would want to implement some kind of learning algorithm here
        pass

# Create a new trading bot
bot = TradingBot()

# Have the bot make trades and learn from them
for _ in range(100):
    bot.trade()
    bot.learn()
```

This bot doesn't actually learn anything from its trades. In a real-world scenario, you would want to implement a machine learning algorithm in the `learn` method that allows the bot to improve its trading strategy over time.