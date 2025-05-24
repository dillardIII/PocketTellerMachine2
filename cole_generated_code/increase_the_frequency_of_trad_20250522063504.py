To increase the frequency of trades, we need to modify the trading algorithm. However, without knowing the specifics of the current trading algorithm, it's hard to provide a specific code. 

Assuming we have a simple trading bot that makes trades based on some criteria, we could increase the frequency of trades by reducing the threshold of that criteria. 

Here's a very simplified example:

```python
import random

class TradingBot:
    def __init__(self, frequency):
        self.frequency = frequency

    def trade(self):
        # This is a dummy trading function
        # In a real trading bot, this would be where the trading logic goes
        if random.random() < self.frequency:
            return True
        else:
            return False

# Create a trading bot with a low trading frequency
bot = TradingBot(0.1)

# Simulate running the bot for a day
trades = [bot.trade() for _ in range(24*60)]

print(f"Made {sum(trades)} trades in a day")

# Now increase the trading frequency
bot.frequency = 0.5

# Simulate running the bot for a day again
trades = [bot.trade() for _ in range(24*60)]

print(f"Made {sum(trades)} trades in a day")
```

In this example, the `trade` method of the `TradingBot` class makes a trade with a certain probability (the `frequency`). By increasing the `frequency`, we increase the number of trades the bot makes in a day. 

Please note that this is a very simplified example and a real trading bot would be much more complex. It would take into account many factors such as market conditions, the current portfolio, risk management strategies, etc.