The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market.

Here is a simple Python code to generate a trading strategy based on RSI:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr
from datetime import datetime
import matplotlib.pyplot as plt
from talib import RSI

# Download historical data as dataframe
yf.pdr_override()
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end=datetime.now())

# Calculate RSI
df['RSI'] = RSI(df['Close'], timeperiod=14)

# Create signals
df['Buy_Signal'] = np.where(df['RSI'] < 30, 1, 0)  # Oversold level
df['Sell_Signal'] = np.where(df['RSI'] > 70, -1, 0)  # Overbought level

# Generate trading orders
df['Order'] = df['Buy_Signal'] + df['Sell_Signal']

# Print data
print(df)

# Plot data
plt.figure(figsize=(12,5))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.title('Close Price')
plt.legend(loc='upper left')
plt.show()

plt.figure(figsize=(12,5))
plt.plot(df['RSI'], label='RSI', color='orange')
plt.title('RSI')
plt.legend(loc='upper left')
plt.show()
```

In this code, we first download the historical data of a stock (in this case, Apple Inc.) from Yahoo Finance. Then we calculate the RSI of the closing prices with a time period of 14 days. We generate buy signals when the RSI is below 30 (oversold condition) and sell signals when the RSI is above 70 (overbought condition). Finally, we plot the closing prices and the RSI.

Please note that this is a very simple trading strategy and may not be profitable in real trading. Always backtest your strategies before live trading.