from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a trading strategy based on RSI.

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Download historical data as dataframe
yf.pdr_override()
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2021-12-31")

def calculate_RSI(data, window):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    average_gain = up.rolling(window).mean()
    average_loss = abs(down.rolling(window).mean())
    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Calculate RSI
df['RSI'] = calculate_RSI(df['Close'], 14)

# Create signals
df['Buy_Signal'] = np.where(df['RSI'] < 30, 1, 0)  # oversold condition
df['Sell_Signal'] = np.where(df['RSI'] > 70, -1, 0)  # overbought condition

# Plot
plt.figure(figsize=(12,5))
plt.plot(df.index, df['RSI'], label='RSI')
plt.fill_between(df.index, y1=30, y2=70, color='#adccff', alpha='0.3')
plt.legend(loc='upper left')
plt.show()
```

This script downloads historical data for Apple Inc. (AAPL) from Yahoo Finance, calculates the 14-day RSI, and generates buy signals when the RSI falls below 30 (oversold condition) and sell signals when the RSI rises above 70 (overbought condition). The results are plotted on a graph.