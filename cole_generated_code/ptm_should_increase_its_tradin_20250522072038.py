from ghost_env import INFURA_KEY, VAULT_ADDRESS
To increase PTM's trading activity, we would need to automate the trading process. Here is a simple Python code that uses a random trading strategy to increase trading activity. This code uses the `yfinance` library to download stock data and `pandas` to handle the data.

Please note that this is a very basic example and in a real scenario, you would need a much more sophisticated trading strategy and risk management.

```python
import yfinance as yf
import pandas as pd
import numpy as np
import time

# Define the stock to trade
stock = 'PTM'

# Define the period to download data
period = '1d'

# Define the interval for trading
interval = '1m'

# Download stock data
data = yf.download(tickers=stock, period=period, interval=interval)

# Define a simple random trading strategy
def random_trading_strategy(data):
    # Generate a random number
    random_number = np.random.randint(0, 2)
    
    # If the random number is 0, we buy, if it's 1, we sell
    if random_number == 0:
        action = 'Buy'
    else:
        action = 'Sell'
    
    return action

# Start trading
while True:
    # Get the latest data
    data = yf.download(tickers=stock, period=period, interval=interval)
    
    # Determine the action to take
    action = random_trading_strategy(data)
    
    # Print the action
    print(f'{action} {stock}')
    
    # Wait for the next minute
    time.sleep(60)
```

This code will increase the trading activity by making a trade every minute. The action (buy or sell) is determined by a simple random trading strategy. The data for each trade is downloaded using the `yfinance` library and handled using `pandas`. The code runs in an infinite loop, making a trade every minute. 

Please note that this code is for illustrative purposes only and should not be used for real trading. In a real scenario, you would need to implement a proper trading strategy and risk management. You would also need to handle the execution of the trades, which is not covered in this code.