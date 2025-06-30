from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a trading strategy based on RSI:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import talib

# Define the instrument to download
stock = 'AAPL'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
df = web.DataReader(stock, 'yahoo', '2015-01-01', '2020-12-31')

# Calculate RSI
df['RSI'] = talib.RSI(df['Close'], timeperiod = 14)

# Define the strategy
df['Buy_Signal'] = np.where((df['RSI'] < 30), 1, 0)
df['Sell_Signal'] = np.where((df['RSI'] > 70), -1, 0)

# Plot the data
plt.figure(figsize=(12,5))
plt.plot(df['Close'], label='Close Prices', color='blue')
plt.title('Close Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()

plt.figure(figsize=(12,5))
plt.plot(df['RSI'], label='RSI', color='red')
plt.title('RSI')
plt.xlabel('Date')
plt.ylabel('RSI')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
```

This script downloads the historical data for a specific stock (in this case, AAPL), calculates the RSI, and generates buy and sell signals based on the RSI. The buy signal is generated when the RSI is less than 30 (oversold condition), and the sell signal is generated when the RSI is greater than 70 (overbought condition). The script also plots the close prices and the RSI.

Please note that this is a very basic trading strategy and should not be used for actual trading without further improvements and testing.