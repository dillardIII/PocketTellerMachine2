from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple implementation of a Relative Strength Index (RSI) strategy generator in Python. This code will calculate the RSI for a given stock price data and generate a trading strategy based on it.

```python
import pandas as pd
import numpy as np

def calculate_RSI(data, window):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    average_gain = up.rolling(window=window).mean()
    average_loss = abs(down.rolling(window=window).mean())

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def RSI_Strategy(data, window=14):
    # Calculate RSI
    data['RSI'] = calculate_RSI(data['Close'], window)

    # Create signals
    data['Buy_Signal'] = np.where((data['RSI'] < 30), 1, 0)  # oversold condition
    data['Sell_Signal'] = np.where((data['RSI'] > 70), -1, 0)  # overbought condition

    # Generate strategy
    data['Strategy'] = data['Buy_Signal'] + data['Sell_Signal']

    return data

# Load data
data = pd.read_csv('stock_data.csv')  # replace with your csv file
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Apply RSI Strategy
data = RSI_Strategy(data)

print(data)
```

This code assumes that you have a CSV file named 'stock_data.csv' that contains the stock price data with 'Date' and 'Close' columns. The 'Close' column represents the closing price of the stock.

The RSI_Strategy function calculates the RSI for the stock price data and generates a trading strategy based on it. If the RSI is less than 30, it's considered oversold and a buy signal is generated. If the RSI is more than 70, it's considered overbought and a sell signal is generated.

Please replace 'stock_data.csv' with your actual CSV file and make sure that the 'Date' and 'Close' columns exist in your data. If your data has different column names, please adjust the code accordingly.