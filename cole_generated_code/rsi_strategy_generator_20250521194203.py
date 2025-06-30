from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a trading strategy based on RSI.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Function to calculate RSI
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

# Fetching the data
data = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2021-12-31")
data['RSI'] = calculate_RSI(data['Close'], 14)

# Generate trading signals
data['Buy_Signal'] = np.where((data['RSI'] < 30), 1, 0) # Over-sold condition
data['Sell_Signal'] = np.where((data['RSI'] > 70), -1, 0) # Over-bought condition

# Plotting
plt.figure(figsize=(12,5))
plt.plot(data['RSI'], label='RSI', color='blue')
plt.axhline(0, linestyle='--', alpha=0.5, color='black')
plt.axhline(20, linestyle='--', alpha=0.5, color='orange')
plt.axhline(30, linestyle='--', alpha=0.5, color='green')
plt.axhline(70, linestyle='--', alpha=0.5, color='red')
plt.axhline(80, linestyle='--', alpha=0.5, color='orange')
plt.axhline(100, linestyle='--', alpha=0.5, color='black')
plt.title('RSI Strategy')
plt.show()
```

This script fetches the historical data for Apple Inc. (AAPL) from Yahoo Finance. It calculates the RSI based on the closing prices with a window of 14 days. If the RSI is below 30, it generates a buy signal, and if the RSI is above 70, it generates a sell signal. The script also plots the RSI values and the buy/sell signals.