Sure, here is a simple example of a Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is used to identify buying and selling opportunities in a price trend.

Please note that this is a very basic strategy and may not be suitable for real trading. It's just an example to show how a trading strategy can be implemented in Python.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

# Fetching the data
data = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2021-12-31")

# Calculate short-term simple moving average
ShortEMA = data.Close.ewm(span=12, adjust=False).mean()

# Calculate long-term simple moving average
LongEMA = data.Close.ewm(span=26, adjust=False).mean()

# Calculate the Moving Average Convergence/Divergence (MACD)
MACD = ShortEMA - LongEMA

# Calculate the signal line
signal = MACD.ewm(span=9, adjust=False).mean()

# Create a new column to hold the trading strategy
data['Buy_Signal_Price'] = np.where(MACD > signal, data['Close'], np.nan)
data['Sell_Signal_Price'] = np.where(MACD < signal, data['Close'], np.nan)

# Plot the data
plt.figure(figsize=(12.2, 4.5))
plt.scatter(data.index, data['Buy_Signal_Price'], color='green', label='Buy', marker='^', alpha=1)
plt.scatter(data.index, data['Sell_Signal_Price'], color='red', label='Sell', marker='v', alpha=1)
plt.plot(data['Close'], label='Close Price', alpha=0.35)
plt.title('Close Price Buy & Sell Signals')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()
```

This code fetches the historical price data of Apple Inc. (AAPL) from Yahoo Finance, calculates the short-term and long-term exponential moving averages (EMA), and then calculates the Moving Average Convergence/Divergence (MACD) and the signal line. When the MACD crosses above the signal line, it generates a buy signal, and when it crosses below the signal line, it generates a sell signal. These signals are plotted on a chart.