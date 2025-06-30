from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code for EMA Crossover Analyzer using Pandas library. This code calculates the EMA for two different periods and then finds the points where these two EMAs cross each other.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover(data, short_window, long_window):
    short_ema = calculate_ema(data, short_window)
    long_ema = calculate_ema(data, long_window)

    buy_signals = (short_ema > long_ema) & (short_ema.shift() < long_ema.shift())
    sell_signals = (short_ema < long_ema) & (short_ema.shift() > long_ema.shift())

    return buy_signals, sell_signals

# Fetching data
df = web.DataReader('AAPL', 'yahoo', start='01-01-2020', end='12-31-2020')
df = df['Close']

# Define the EMA periods
short_window = 12
long_window = 26

buy_signals, sell_signals = ema_crossover(df, short_window, long_window)

# Plotting
plt.figure(figsize=(12,5))
plt.plot(df.index, df, label='Close Price', color='blue', alpha=0.35)
plt.plot(df.index, calculate_ema(df, short_window), label=f'Short EMA ({short_window})', color='red', alpha=0.7)
plt.plot(df.index, calculate_ema(df, long_window), label=f'Long EMA ({long_window})', color='green', alpha=0.7)
plt.scatter(df.index, df[buy_signals], color='green', marker='^', alpha=1)
plt.scatter(df.index, df[sell_signals], color='red', marker='v', alpha=1)
plt.title('EMA Crossover')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend(loc='upper left')
plt.show()
```

This script fetches the historical closing prices for AAPL from Yahoo Finance, calculates the short-term and long-term EMA, and then finds the points where these two EMAs cross each other. These crossover points are potential buy and sell signals. The script then plots the closing prices, the two EMAs, and the buy/sell signals on a chart.

Please note that you need to install the following Python packages if they are not installed yet: pandas, pandas_datareader, numpy, and matplotlib. You can install them using pip:

```bash
pip install pandas pandas_datareader numpy matplotlib
```