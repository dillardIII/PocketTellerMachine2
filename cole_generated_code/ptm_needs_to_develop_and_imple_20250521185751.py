Here is a simple Python code that uses a basic trading strategy called Moving Average Crossover. This strategy is used to identify changes in trends and can be used as a basis for a trading strategy.

In this strategy, we calculate two moving averages of different periods, like a 50-day and a 200-day moving average. When the short-term moving average crosses above the long-term moving average, it may be a good time to buy. Conversely, when the short-term moving average crosses below the long-term moving average, it may be a good time to sell.

Please note that this is a simple trading strategy and may not be suitable for all trading scenarios. Always use trading strategies with caution and discretion.

```python
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

# Define the stock to be used
stock = 'AAPL'

# Load the data
df = web.DataReader(stock, 'yahoo', start='01-01-2020')

# Calculate the short-term moving average
df['short_mavg'] = df['Close'].rolling(window=50, min_periods=1).mean()

# Calculate the long-term moving average
df['long_mavg'] = df['Close'].rolling(window=200, min_periods=1).mean()

# Create a "signal" column where if the short-term moving average is greater than the long-term, then 1, else 0.
df['signal'] = 0.0  
df['signal'][50:] = np.where(df['short_mavg'][50:] > df['long_mavg'][50:], 1.0, 0.0)   

# Create a "positions" column which is the difference of the "signal" column. This column will give us the actual trading orders.
df['positions'] = df['signal'].diff()

# Plotting
plt.figure(figsize=(20,10))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(df['short_mavg'], label='50-day SMA', color='red')
plt.plot(df['long_mavg'], label='200-day SMA', color='green')

# Plot buy signals
plt.plot(df[df['positions'] == 1].index, df['short_mavg'][df['positions'] == 1], '^', markersize=10, color='m')

# Plot sell signals
plt.plot(df[df['positions'] == -1].index, df['short_mavg'][df['positions'] == -1], 'v', markersize=10, color='k')

plt.title('Apple Inc. - Moving Average Crossover Trading Strategy')
plt.legend()
plt.grid()
plt.show()
```

This script will plot the closing price of the stock, the short-term moving average, the long-term moving average, and the points where the strategy would suggest to buy (magenta up-pointing triangles) or sell (black down-pointing triangles).

Please note that you need to install the `pandas_datareader` and `matplotlib` libraries to run this script. You can install them using pip:

```
pip install pandas_datareader matplotlib
```