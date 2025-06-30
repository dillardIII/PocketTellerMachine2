from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code that generates a trading strategy based on the RSI.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf

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

def implement_RSI_strategy(data, window=14):
    data['RSI'] = calculate_RSI(data['Adj Close'], window)
    data['Buy_Signal'] = (data['RSI'] < 30)
    data['Sell_Signal'] = (data['RSI'] > 70)
    return data

start_date = datetime(2020, 1, 1)
end_date = datetime.now()

data = yf.download('AAPL', start=start_date, end=end_date)
data = implement_RSI_strategy(data)

# Plotting
plt.figure(figsize=(12,5))
plt.plot(data['Adj Close'], label='Price', color='blue')
plt.title('RSI Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()

plt.figure(figsize=(12,5))
plt.title('RSI')
plt.plot(data['RSI'], label='RSI', color='red')
plt.axhline(0, linestyle='--', alpha=0.5, color='gray')
plt.axhline(10, linestyle='--', alpha=0.5, color='orange')
plt.axhline(20, linestyle='--', alpha=0.5, color='green')
plt.axhline(30, linestyle='--', alpha=0.5, color='red')
plt.axhline(70, linestyle='--', alpha=0.5, color='red')
plt.axhline(80, linestyle='--', alpha=0.5, color='green')
plt.axhline(90, linestyle='--', alpha=0.5, color='orange')
plt.axhline(100, linestyle='--', alpha=0.5, color='gray')
plt.xlabel('Date')
plt.ylabel('RSI')
plt.show()
```

This code calculates the RSI for a given window (default is 14 days as it's commonly used) and generates buy signals when the RSI is below 30 (oversold) and sell signals when the RSI is above 70 (overbought). It then plots the price and the RSI for visualization.

Please note that this is a very basic strategy and should not be used for actual trading without further refinement and testing. Always do your own research and consider other factors before making trading decisions.