from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple example of a Python code for a trading strategy. This strategy is a simple moving average crossover strategy. This strategy buys when the short term moving average crosses above the long term moving average and sells when the short term moving average crosses below the long term moving average.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the period for the short and long moving average
short_period = 20
long_period = 100

# Get the stock data
df = web.DataReader(stock, data_source='yahoo', start='01-01-2010')

# Calculate the short and long moving average
df['short_mavg'] = df['Close'].rolling(window=short_period, min_periods=1, center=False).mean()
df['long_mavg'] = df['Close'].rolling(window=long_period, min_periods=1, center=False).mean()

# Create a column 'signal' such that if the short moving average is greater than the long moving average
# then set the signal as 1 else 0
df['signal'] = np.where(df['short_mavg'] > df['long_mavg'], 1.0, 0.0)

# Create a column 'positions' which is the difference of the 'signal' column
df['positions'] = df['signal'].diff()

# Plotting
plt.figure(figsize=(20,10))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(df['short_mavg'], label='Short Moving Average', color='red')
plt.plot(df['long_mavg'], label='Long Moving Average', color='black')
plt.plot(df.loc[df.positions == 1.0].index, df.short_mavg[df.positions == 1.0], '^' , markersize=10, color='g')
plt.plot(df.loc[df.positions == -1.0].index, df.short_mavg[df.positions == -1.0], 'v' , markersize=10, color='r')
plt.ylabel('Price')
plt.xlabel('Date')
plt.legend(loc='best')
plt.title('Moving Average Crossover Strategy')
plt.grid(True)
plt.show()
```

This code will plot the stock price, short moving average, long moving average and the buy/sell signals. Green arrows indicate buying points and red arrows indicate selling points.

Please note that this is a very basic strategy and in real world trading, you would need to consider many other factors like transaction costs, slippage, risk management etc. Also, this strategy assumes that you have the ability to trade at the closing price of each day which may not always be possible.