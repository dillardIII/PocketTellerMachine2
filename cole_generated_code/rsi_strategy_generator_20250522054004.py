The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate an RSI strategy:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Download historical data as dataframe
yf.pdr_override()
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end=datetime.now())

# Calculate the RSI
delta = df['Adj Close'].diff()
up = delta.clip(lower=0)
down = -1*delta.clip(upper=0)
ema_up = up.ewm(com=13, adjust=False).mean()
ema_down = down.ewm(com=13, adjust=False).mean()
rs = ema_up/ema_down
df['RSI'] = 100 - (100/(1 + rs))

# Create a strategy
df['Buy_Signal'] = np.where(df['RSI'] < 30, 1, 0) # Buy when RSI < 30
df['Sell_Signal'] = np.where(df['RSI'] > 70, 1, 0) # Sell when RSI > 70

# Plot the prices and the strategy signals
plt.figure(figsize=(12,5))
plt.plot(df['Adj Close'], label='Price', color='blue')
plt.plot(df.index, df.RSI, label='RSI', color='orange')
plt.plot(df[df['Buy_Signal'] == 1].index, df['Adj Close'][df['Buy_Signal'] == 1], '^', markersize=10, color='g', label='buy')
plt.plot(df[df['Sell_Signal'] == 1].index, df['Adj Close'][df['Sell_Signal'] == 1], 'v', markersize=10, color='r', label='sell')
plt.ylabel('Price in $')
plt.xlabel('Date')
plt.title('RSI Strategy Generator')
plt.legend()
plt.grid()
plt.show()
```

This code downloads historical data for Apple Inc. (AAPL) from Yahoo Finance, calculates the RSI, generates a simple strategy (buy when RSI < 30, sell when RSI > 70), and plots the prices and the strategy signals. Please note that this is a very simple strategy and should not be used for real trading without further enhancements.