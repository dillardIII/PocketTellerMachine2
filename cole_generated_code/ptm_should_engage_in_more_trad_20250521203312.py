To increase the number of trades PTM engages in, we can create a Python script that uses a simple trading strategy. This strategy will buy when the price is low and sell when the price is high.

Here's a simple Python code that uses a hypothetical trading API to implement this strategy:

```python
import time
import trading_api  # hypothetical trading API

def trade():
    while True:
        # Get the current price of the stock
        current_price = trading_api.get_current_price("PTM")

        # If the price is lower than a certain threshold, buy the stock
        if current_price < 100:  # this threshold should be adjusted based on the stock's typical price range
            trading_api.buy("PTM")

        # If the price is higher than a certain threshold, sell the stock
        elif current_price > 200:  # this threshold should be adjusted based on the stock's typical price range
            trading_api.sell("PTM")

        # Wait for a while before the next trade
        time.sleep(60)  # adjust this based on how frequently you want to trade

# Start trading
trade()
```

Please note that this is a very simplified example. Real-world trading strategies are much more complex and take into account many other factors. Also, this code assumes that you have a trading API that provides `get_current_price`, `buy`, and `sell` functions. You would need to replace `trading_api` with the actual API you are using.

Moreover, increasing the number of trades doesn't necessarily increase the chances of wins. It's important to have a good trading strategy that takes into account the risk and reward of each trade.