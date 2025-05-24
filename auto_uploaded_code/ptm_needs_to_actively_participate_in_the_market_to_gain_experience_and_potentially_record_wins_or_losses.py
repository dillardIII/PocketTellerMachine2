To accomplish this task, we can create a simple simulation of a trading bot in Python. This bot will randomly decide whether to buy or sell a stock based on a random number generator. The wins and losses will be recorded and displayed at the end of the simulation.

Here is a simple Python code for this task:

```python
import random

class PTM:
    def __init__(self):
        self.balance = 10000  # initial balance
        self.stock = 0  # number of stocks
        self.stock_price = 100  # initial stock price
        self.history = []  # trading history

    def buy(self):
        if self.balance > self.stock_price:
            self.balance -= self.stock_price
            self.stock += 1
            self.history.append(('buy', self.stock_price))

    def sell(self):
        if self.stock > 0:
            self.balance += self.stock_price
            self.stock -= 1
            self.history.append(('sell', self.stock_price))

    def simulate(self, days):
        for _ in range(days):
            self.stock_price += random.randint(-10, 10)  # stock price fluctuation
            if random.random() < 0.5:
                self.buy()
            else:
                self.sell()

        print('Final Balance:', self.balance)
        print('Final Stock:', self.stock)
        print('Trading History:', self.history)

ptm = PTM()
ptm.simulate(30)  # simulate for 30 days
```

This is a very basic simulation and does not take into account many factors that would be present in a real-world trading scenario, such as transaction fees, market trends, and more. It's also based on a completely random decision-making process, which is not how real trading bots would operate. 

For a more realistic simulation, you would need to implement a more sophisticated decision-making process, possibly using machine learning algorithms to predict market trends.