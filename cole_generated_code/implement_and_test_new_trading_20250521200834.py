from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a Python code implementing a basic trading strategy using the Moving Average Crossover strategy. This strategy is based on the premise that a short-term moving average crossing above a long-term moving average is a buy signal, and vice versa.

Please note that this is a very basic strategy and should be used for educational purposes only. Real-world trading involves many more factors.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used
stock = 'AAPL'

# Define the data range
start_date = '01/01/2010'
end_date = '01/01/2022'

# Get the stock data
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short-term moving average
short_window = 40
df['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Calculate the long-term moving average
long_window = 100
df['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create a 'signals' DataFrame with the signal information
signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0

# Create signals
signals['signal'][short_window:] = np.where(df['short_mavg'][short_window:] 
                                            > df['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print the DataFrame
print(signals)

# Plotting the strategy
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Price in $')
df['Close'].plot(ax=ax1, color='r', lw=2.)
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)
ax1.plot(signals.loc[signals.positions == 1.0].index, 
         df['Close'][signals.positions == 1.0],
         '^', markersize=10, color='m')
ax1.plot(signals.loc[signals.positions == -1.0].index, 
         df['Close'][signals.positions == -1.0],
         'v', markersize=10, color='k')
plt.show()
```

This script will fetch the historical data for the specified stock, calculate the short-term and long-term moving averages, generate trading signals based on these averages, and plot the results. The green triangles represent a buy signal and the red triangles represent a sell signal.