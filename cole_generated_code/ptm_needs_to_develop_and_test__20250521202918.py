from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide you with a simple Python code that simulates a basic trading strategy. However, please note that this is a very simplified example and real-world trading strategies are much more complex and involve sophisticated algorithms, machine learning, and extensive financial knowledge.

```python
import pandas as pd
import numpy as np

# Let's assume we have a simple data of stock prices
data = pd.DataFrame({
    'date': pd.date_range(start='01-01-2020', periods=100),
    'price': (np.random.rand(100) * 100).round(2)  # random stock prices
})

# Define a simple trading strategy: buy when the price drops by 5% or more from the recent peak,
# and sell when the price rises by 10% or more from the recent trough

def trading_strategy(data):
    buy_price = 0
    sell_price = 0
    balance = 0
    holdings = 0

    for i in range(1, len(data)):
        if data['price'].iloc[i] < 0.95 * data['price'].iloc[i-1] and balance >= data['price'].iloc[i]:  # buy condition
            buy_price = data['price'].iloc[i]
            holdings += 1
            balance -= buy_price
            print(f"Buy on {data['date'].iloc[i]} at {buy_price}")

        elif data['price'].iloc[i] > 1.1 * data['price'].iloc[i-1] and holdings > 0:  # sell condition
            sell_price = data['price'].iloc[i]
            holdings -= 1
            balance += sell_price
            print(f"Sell on {data['date'].iloc[i]} at {sell_price}")

    print(f"Final balance: {balance}")
    print(f"Final holdings: {holdings}")

trading_strategy(data)
```

This script simulates a simple trading strategy on a randomly generated stock price data. The strategy is to buy when the price drops by 5% or more from the recent peak, and sell when the price rises by 10% or more from the recent trough. The final balance and holdings are printed at the end.

Please note that this is a very simplified example and real-world trading strategies are much more complex and involve sophisticated algorithms, machine learning, and extensive financial knowledge.