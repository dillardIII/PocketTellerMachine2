from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide you with a simple example of a trading strategy using Python. This strategy will be based on a simple Moving Average Crossover, which is a common trading strategy. 

Please note that this is a very basic strategy and real-world trading strategies involve much more factors and complex algorithms.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the instruments to download. We would like to see Apple, Microsoft and others.
companies_dict = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Amazon': 'AMZN',
    'Google': 'GOOG',
}

# Define which online source to use
data_source = 'yahoo'

# Define the start and end dates that we want to see
start_date = '2016-01-01'
end_date = '2021-12-31'

# Use pandas_datareader.data.DataReader to load the desired data
panel_data = web.DataReader(list(companies_dict.values()), data_source, start_date, end_date)

# Calculate the short-window simple moving average
short_rolling = panel_data.rolling(window=20).mean()

# Calculate the long-window simple moving average
long_rolling = panel_data.rolling(window=100).mean()

# Create a 'signal' (invested or not invested) when the short moving average crosses the long moving average
signal = short_rolling > long_rolling

# Create a trading orders based on the signals
positions = signal.diff()

# Plotting
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Price in $')

# Plot the closing price
panel_data['Close'].plot(ax=ax1, color='r', lw=2.)

# Plot the short and long moving averages
short_rolling['Close'].plot(ax=ax1, color='b', lw=2.)
long_rolling['Close'].plot(ax=ax1, color='y', lw=2.)

# Plot the buy signals
ax1.plot(positions[positions == 1.0].index, 
         short_rolling[positions == 1.0],
         '^', markersize=10, color='m')

# Plot the sell signals
ax1.plot(positions[positions == -1.0].index, 
         short_rolling[positions == -1.0],
         'v', markersize=10, color='k')

plt.show()
```

This script will download the historical data for the specified companies from Yahoo Finance, calculate the short and long window moving averages, generate trading signals when these averages cross, and plot the results.

Please note that this is a very basic trading strategy and is not meant to be used for real trading without further improvements.