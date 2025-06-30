from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can help you write a simple Python code to simulate trades. However, please note that this is just a simulation and does not involve real trading. 

```python
import pandas as pd
import random

# Define the stocks we are interested in
stocks = ['AAPL', 'GOOG', 'TSLA', 'AMZN', 'MSFT']

# Define the possible actions
actions = ['BUY', 'SELL']

# Define the quantity range
quantity_range = range(1, 101)

# Define the price range
price_range = range(50, 500)

# Create an empty list to store the trades
trades = []

# Generate the trades
for _ in range(10):
    stock = random.choice(stocks)
    action = random.choice(actions)
    quantity = random.choice(quantity_range)
    price = random.choice(price_range)

    trades.append({
        'Stock': stock,
        'Action': action,
        'Quantity': quantity,
        'Price': price
    })

# Convert the trades to a DataFrame
df = pd.DataFrame(trades)

# Print the DataFrame
print(df)
```

This script will generate 10 trades with random stock, action, quantity, and price. The trades are stored in a pandas DataFrame for easy analysis.