from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple Python code that uses the `pandas` library to calculate the Relative Strength Index (RSI) for a given stock. This is a basic strategy generator and does not include the trading part.

```python
import pandas as pd
import pandas_datareader as web
import datetime as dt

# Function to calculate RSI
def calculate_rsi(data, window):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    average_gain = up.rolling(window).mean()
    average_loss = abs(down.rolling(window).mean())

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Define the stock and the date range
stock = 'AAPL'
start = dt.datetime(2020,1,1)
end = dt.datetime.now()

# Get the stock data
data = web.DataReader(stock, 'yahoo', start, end)

# Calculate the RSI
data['RSI'] = calculate_rsi(data['Close'], 14)

print(data)
```

This code calculates the 14-day RSI for the Apple stock. The `calculate_rsi` function calculates the RSI based on the closing prices of the stock. 

Please note that this is a simple RSI calculation and does not take into account trading fees, slippage, or other factors that could impact the performance of a trading strategy. Always backtest your strategies before live trading.