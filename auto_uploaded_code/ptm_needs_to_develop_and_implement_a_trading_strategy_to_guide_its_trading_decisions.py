from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code to implement a basic trading strategy. This strategy uses Moving Average Crossover which is a common trading strategy. It involves the use of two moving averages, one short term and one long term. When the short term moving average crosses above the long term moving average, it indicates a buy signal. Conversely, when the short term moving average crosses below the long term moving average, it indicates a sell signal.

Please note that this is a very basic strategy and real-world trading strategies can be much more complex involving many more factors.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the start and end dates for the data
start_date = '01/01/2010'
end_date = '01/01/2022'

# Get the stock data
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short term and long term moving averages
short_term_avg = df['Close'].rolling(window=20).mean()
long_term_avg = df['Close'].rolling(window=100).mean()

# Create a 'signal' column where if the short term moving average is greater than the long term moving average, set to 1 (buy), else 0 (sell)
df['signal'] = np.where(short_term_avg > long_term_avg, 1.0, 0.0)

# Create a 'positions' column which is the difference of the 'signal' column. This column will give us the points where a buy or sell signal is generated
df['positions'] = df['signal'].diff()

# Plot the closing price, short term and long term moving averages and the buy/sell signals
plt.figure(figsize=(20,10))
plt.plot(df['Close'], label='Close Price', color='blue', alpha=0.35)
plt.plot(short_term_avg, label='40-day SMA', color='red', alpha=0.35)
plt.plot(long_term_avg, label='100-day SMA', color='green', alpha=0.35)
plt.plot(df[df['positions'] == 1.0].index, df[short_term_avg[df['positions'] == 1.0]], '^', markersize=10, color='m')
plt.plot(df[df['positions'] == -1.0].index, df[short_term_avg[df['positions'] == -1.0]], 'v', markersize=10, color='k')
plt.title('Apple Inc. - Moving Average Crossover Trading Signals')
plt.legend(loc='upper left')
plt.grid()
plt.show()
```

This code will plot the closing price of the stock, the short term and long term moving averages and the points where a buy or sell signal is generated. Please note that you need to install `pandas_datareader` library to fetch the stock data. You can install it using pip:

```shell
pip install pandas_datareader
```