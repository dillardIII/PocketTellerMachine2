Sure, here is a simple Python code for generating a Relative Strength Index (RSI) strategy using the pandas library. This strategy will generate buy signals when the RSI is below 30 (oversold) and sell signals when the RSI is above 70 (overbought).

```python
import pandas as pd
import pandas_datareader as web
import numpy as np

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

# Fetching historical data
data = web.DataReader('AAPL', 'yahoo', start='01-01-2020', end='31-12-2020')
data['RSI'] = calculate_rsi(data['Close'], 14)

# Generating signals
data['Buy_Signal'] = np.where(data['RSI'] < 30, 1, 0)
data['Sell_Signal'] = np.where(data['RSI'] > 70, -1, 0)

print(data)
```

This code fetches historical data for Apple Inc. (AAPL) from Yahoo Finance for the year 2020, calculates the 14-day RSI, and generates buy and sell signals based on the RSI. The 'Buy_Signal' column in the dataframe will contain 1 on the days where the RSI is below 30, and the 'Sell_Signal' column will contain -1 on the days where the RSI is above 70.