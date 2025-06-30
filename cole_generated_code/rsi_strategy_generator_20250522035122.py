from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate an RSI strategy:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web
import matplotlib.pyplot as plt

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

def implement_rsi_strategy(data, window):
    data['RSI'] = calculate_rsi(data['Adj Close'], window)
    data['Buy_Signal'] = (data['RSI'] < 30)
    data['Sell_Signal'] = (data['RSI'] > 70)
    return data

# Fetch data
data = web.DataReader('AAPL', data_source='yahoo', start='01-01-2020', end='31-12-2020')
data = data[['Adj Close']]

# Implement RSI Strategy
window = 14
data = implement_rsi_strategy(data, window)

# Plotting
plt.figure(figsize=(12,5))
plt.plot(data['Adj Close'], label='AAPL')
plt.plot(data.loc[data['Buy_Signal']].index, data['Adj Close'][data['Buy_Signal']], '^', markersize=10, color='g', label='buy')
plt.plot(data.loc[data['Sell_Signal']].index, data['Adj Close'][data['Sell_Signal']], 'v', markersize=10, color='r', label='sell')
plt.title('Apple Adj Close Price History Buy / Sell Signals')
plt.xlabel('Oct. 02, 2006 - Dec. 30, 2011')
plt.ylabel('Adj Close Price USD ($)')
plt.legend(loc='upper left')
plt.grid()
plt.show()
```

This script fetches the historical data for Apple Inc. from Yahoo Finance, calculates the RSI, and generates buy signals when the RSI is below 30 (oversold conditions) and sell signals when the RSI is above 70 (overbought conditions). It then plots the adjusted close price along with the buy and sell signals.

Please note that this is a very basic strategy and should not be used for real trading without further improvements.