from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a RSI strategy:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web
import matplotlib.pyplot as plt

def calculate_RSI(data, window):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    avg_gain = up.rolling(window=window).mean()
    avg_loss = abs(down.rolling(window=window).mean())
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def implement_RSI_strategy(data, window):
    data['RSI'] = calculate_RSI(data['Adj Close'], window)
    data['Buy_Signal'] = np.where((data['RSI'] < 30), 1, 0) # oversold condition
    data['Sell_Signal'] = np.where((data['RSI'] > 70), 1, 0) # overbought condition
    return data

# Fetching the data
ticker = 'AAPL'
data = web.DataReader(ticker, 'yahoo', start='01-01-2015', end='31-12-2020')

# Implementing the strategy
window = 14
data = implement_RSI_strategy(data, window)

# Plotting the data
plt.figure(figsize=(12,5))
plt.plot(data['RSI'], label='RSI', color='blue')
plt.axhline(0, linestyle='--', alpha=0.5, color='black')
plt.axhline(10, linestyle='--', alpha=0.5, color='orange')
plt.axhline(20, linestyle='--', alpha=0.5, color='green')
plt.axhline(30, linestyle='--', alpha=0.5, color='red')
plt.axhline(70, linestyle='--', alpha=0.5, color='red')
plt.axhline(80, linestyle='--', alpha=0.5, color='green')
plt.axhline(90, linestyle='--', alpha=0.5, color='orange')
plt.axhline(100, linestyle='--', alpha=0.5, color='black')
plt.title('RSI strategy')
plt.show()
```

In this code, we first define a function to calculate the RSI. Then, we define another function to implement the RSI strategy. This function adds two new columns to the data: 'Buy_Signal' and 'Sell_Signal'. These columns contain 1s and 0s indicating whether to buy or sell the stock based on the RSI value. Finally, we fetch the data for a specific stock (in this case, Apple), implement the strategy, and plot the RSI values.