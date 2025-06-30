from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It's typically used to identify overbought or oversold conditions in a market.

Here's a simple Python code to generate a trading strategy based on RSI:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
from ta.momentum import RSIIndicator

# Define the ticker list
tickers_list = ['AAPL']

# Fetch the data
data = yf.download(tickers_list,'2016-1-1')['Adj Close']

# Print first 5 rows of the data
print(data.head())

# Calculate RSI
rsi = RSIIndicator(data, 14)
data['RSI'] = rsi.rsi()

# Define the RSI threshold values
low_rsi = 30
high_rsi = 70

# Create signals
data['Buy_Signal'] = np.where((data['RSI'] < low_rsi), 1, 0)
data['Sell_Signal'] = np.where((data['RSI'] > high_rsi), -1, 0)

# Print the dataframe
print(data)

# Plotting
plt.figure(figsize=(12,5))
plt.plot(data['RSI'], label='RSI', color='blue')
plt.axhline(0, linestyle='--', alpha=0.1)
plt.axhline(20, linestyle='--', alpha=0.5)
plt.axhline(30, linestyle='--')
plt.axhline(70, linestyle='--')
plt.axhline(80, linestyle='--', alpha=0.5)
plt.axhline(100, linestyle='--', alpha=0.1)
plt.fill_between(data.index, y1=30, y2=70, color='#adccff', alpha='0.3')
plt.title('RSI Strategy')
plt.show()
```

In this code, we first fetch the historical data for a specific ticker (in this case, 'AAPL' for Apple Inc.). Then, we calculate the RSI using the `RSIIndicator` function from the `ta` library. We then create 'Buy' and 'Sell' signals based on the RSI values. If the RSI is less than 30 (indicating the stock is oversold), we generate a 'Buy' signal. If the RSI is more than 70 (indicating the stock is overbought), we generate a 'Sell' signal. Finally, we plot the RSI values and the buy/sell signals.