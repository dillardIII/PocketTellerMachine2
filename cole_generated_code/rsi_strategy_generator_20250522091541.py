from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a basic RSI strategy:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Download historical data for required stocks
ticker = "AAPL"
yf.pdr_override()
df = pdr.get_data_yahoo(ticker, start="2020-01-01", end=datetime.today().strftime('%Y-%m-%d'))

# Calculate the RSI
delta = df['Adj Close'].diff()
up = delta.clip(lower=0)
down = -1*delta.clip(upper=0)
ema_up = up.ewm(com=13, adjust=False).mean()
ema_down = down.ewm(com=13, adjust=False).mean()
rs = ema_up/ema_down
df['RSI'] = 100 - (100/(1+rs))

# Define the strategy
df['Buy_Signal'] = np.where(df['RSI'] < 30, 1, 0) # Over-sold conditions
df['Sell_Signal'] = np.where(df['RSI'] > 70, -1, 0) # Over-bought conditions

# Plot the strategy
plt.figure(figsize=(12,5))
plt.plot(df['Adj Close'], label='Adj Close', color='blue')
plt.plot(df['RSI'], label='RSI', color='red')
plt.plot(df.index, df['Buy_Signal'] * df['Adj Close'], '^', markersize=10, color='m')
plt.plot(df.index, df['Sell_Signal'] * df['Adj Close'], 'v', markersize=10, color='k')
plt.title('RSI Strategy for ' + ticker)
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.grid()
plt.show()
```

This code will generate a plot of the RSI strategy for the given ticker symbol. The magenta upward-pointing triangles represent buy signals (when RSI < 30), and the black downward-pointing triangles represent sell signals (when RSI > 70). Please note that this is a very basic strategy and should not be used for actual trading without further refinement and testing.