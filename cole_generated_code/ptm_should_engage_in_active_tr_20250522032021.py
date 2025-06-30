from ghost_env import INFURA_KEY, VAULT_ADDRESS
To generate wins and losses data for PTM's active trading, we would need to simulate a trading strategy. Here's a simple example using Python and pandas library. This example assumes that we have historical price data for a certain stock in a CSV file.

Please note that this is a simulation and should not be used for actual trading. Real-world trading involves many more factors and requires careful analysis and risk management.

```python
import pandas as pd
import numpy as np

# Load historical price data from CSV file
data = pd.read_csv('price_data.csv')

# Calculate daily returns
data['return'] = data['price'].pct_change()

# Define a simple trading strategy: buy if yesterday's return was positive, sell if it was negative
data['signal'] = np.where(data['return'].shift(-1) > 0, 1, -1)

# Calculate strategy returns
data['strategy_return'] = data['signal'] * data['return']

# Define wins and losses
data['win'] = np.where(data['strategy_return'] > 0, 1, 0)
data['loss'] = np.where(data['strategy_return'] < 0, 1, 0)

# Print the total number of wins and losses
print('Wins:', data['win'].sum())
print('Losses:', data['loss'].sum())
```

This code first calculates daily returns based on price changes. Then it defines a simple trading strategy: if yesterday's return was positive, it assumes that the price will go up today, so it "buys" the stock; if yesterday's return was negative, it assumes that the price will go down, so it "sells" the stock. Then it calculates the returns of this strategy and defines wins as days with positive returns and losses as days with negative returns. Finally, it prints the total number of wins and losses.