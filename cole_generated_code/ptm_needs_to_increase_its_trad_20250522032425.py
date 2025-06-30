from ghost_env import INFURA_KEY, VAULT_ADDRESS
In order to increase trading activity, you could automate the trading process. Here is a simple example of how you might do this using Python. This example uses a fictional trading API, so you'll need to replace it with your actual trading API.

```python
import time
import random
from trading_api import place_order  # Replace with your actual trading API

def automated_trading():
    symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT']  # List of symbols to trade
    while True:
        symbol = random.choice(symbols)  # Choose a random symbol
        action = random.choice(['buy', 'sell'])  # Randomly decide to buy or sell
        quantity = random.randint(1, 10)  # Randomly decide the quantity to buy/sell

        # Place the order
        place_order(
            symbol=symbol,
            action=action,
            quantity=quantity
        )

        # Wait for a random amount of time between 1 and 10 seconds before the next trade
        time.sleep(random.randint(1, 10))

# Run the automated trading
automated_trading()
```

This script will continuously place random buy and sell orders for the specified symbols, which should increase your trading activity.

Please note that this is a very simple and naive approach to automated trading. In a real-world scenario, you would want to use a more sophisticated strategy based on actual market data and possibly machine learning algorithms. Also, keep in mind that this script will run indefinitely until you stop it, so make sure to monitor it closely and set appropriate limits to prevent losses.