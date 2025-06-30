from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, let's initiate some trades for PTM. But remember, the following is a basic simulation of trades and not advice or an algorithm to choose stocks. Please input your own parameters and strategy according to your requirements.

```python
import random

# Information about the stocks
stocks = ['AAPL', 'GOOG', 'TSLA', 'AMZN', 'MSFT']
stock_prices = {'AAPL': 150, 'GOOG': 2000, 'TSLA': 700, 'AMZN': 3400, 'MSFT': 300}

# Funds available for trading
funds = 10000

# List to record trades
trades = []

def initiate_trade(funds, stocks, stock_prices):
    while funds > 0:
        # Select a random stock
        stock = random.choice(stocks)

        # Determine the price of the stock
        price = stock_prices[stock]

        # Determine the number of shares to buy 
        if funds//price > 0:
            shares = random.randint(1, funds//price)
        else:
            break

        # Update the amount of funds after buying the shares
        funds -= shares * price

        trade_info = {
            'Stock': stock,
            'Shares': shares,
            'Price Per Share': price,
            'Total Cost': shares * price
        }

        # Add the trade to the list of trades
        trades.append(trade_info) 

    return trades

trades = initiate_trade(funds, stocks, stock_prices)

for trade in trades:
    print(trade)
```

This code will randomly select stocks from the given list and purchase a random number of shares until the available fund is exhausted. Please note the random trading strategy used here is not recommended for real investment, it is just a demonstration for the purpose of the task.