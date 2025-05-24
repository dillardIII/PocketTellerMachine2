Sure, here is a simple Python code that implements two basic trading strategies: Moving Average Crossover and Mean Reversion. Please note that this is a very simplified version and real-world trading strategies can be much more complex and require thorough backtesting and risk management.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Define the stock symbol and data source
symbol = 'AAPL'
source = 'yahoo'

# Define the date range
start_date = '2010-01-01'
end_date = '2020-12-31'

# Get the stock data
df = pdr.get_data_yahoo(symbol, start=start_date, end=end_date)

# Calculate the short-term and long-term moving averages
df['short_mavg'] = df['Close'].rolling(window=20).mean()
df['long_mavg'] = df['Close'].rolling(window=100).mean()

# Create signals based on moving average crossover
df['signal'] = np.where(df['short_mavg'] > df['long_mavg'], 1.0, 0.0)
df['positions'] = df['signal'].diff()

# Plot the stock price and moving averages
plt.figure(figsize=(10,7))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(df['short_mavg'], label='20-day Mavg', color='red')
plt.plot(df['long_mavg'], label='100-day Mavg', color='green')
plt.plot(df[df['positions'] == 1.0].index, df['short_mavg'][df['positions'] == 1.0], '^', markersize=10, color='m')
plt.plot(df[df['positions'] == -1.0].index, df['short_mavg'][df['positions'] == -1.0], 'v', markersize=10, color='k')
plt.title('Moving Average Crossover Strategy')
plt.legend()
plt.show()

# Mean Reversion Strategy
# Calculate the mean and standard deviation of the price over the past 20 days
df['mean'] = df['Close'].rolling(window=20).mean()
df['std'] = df['Close'].rolling(window=20).std()

# Create signals based on the z-score
df['z_score'] = (df['Close'] - df['mean']) / df['std']
df['signal'] = np.where(df['z_score'] > 1.0, -1.0, np.where(df['z_score'] < -1.0, 1.0, 0.0))
df['positions'] = df['signal'].diff()

# Plot the stock price and z-score
plt.figure(figsize=(10,7))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(df[df['positions'] == 1.0].index, df['Close'][df['positions'] == 1.0], '^', markersize=10, color='m')
plt.plot(df[df['positions'] == -1.0].index, df['Close'][df['positions'] == -1.0], 'v', markersize=10, color='k')
plt.title('Mean Reversion Strategy')
plt.legend()
plt.show()
```

This code uses Yahoo Finance data to implement and visualize the strategies. The Moving Average Crossover strategy generates a buy signal when the short-term moving average crosses above the long-term moving average, and a sell signal when the short-term moving average crosses below the long-term moving average. The Mean Reversion strategy generates a buy signal when the price falls one standard deviation below the mean, and a sell signal when the price rises one standard deviation above the mean.