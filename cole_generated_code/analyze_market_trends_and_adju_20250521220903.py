Analyzing market trends and adjusting trading strategies is a complex task that involves a lot of data analysis and possibly machine learning. Here is a simplified example of how you might use Python to analyze stock market data and make trading decisions based on simple moving average (SMA) strategy.

```python
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

# Define the stock to be analyzed
stock = 'AAPL'

# Define the period for which the data will be obtained
start_date = '2020-01-01'
end_date = '2021-12-31'

# Get the stock data
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short-term and long-term moving averages
short_SMA = df.Close.rolling(window=20).mean()
long_SMA = df.Close.rolling(window=100).mean()

# Create a new column in the dataframe to hold the trading signals
df['signal'] = 0.0
df['signal'][short_SMA > long_SMA] = 1.0

# Create a new column in the dataframe to hold the trading positions
df['position'] = df['signal'].diff()

# Plot the stock price, short-term and long-term moving averages and the buy/sell signals
plt.figure(figsize=(20,10))
plt.plot(df.index, df['Close'], label='Close Price', color='blue')
plt.plot(short_SMA.index, short_SMA, label='20-days SMA', color='red')
plt.plot(long_SMA.index, long_SMA, label='100-days SMA', color='green')
plt.plot(df[df['position'] == 1].index, df['Close'][df['position'] == 1], '^', markersize=10, color='m')
plt.plot(df[df['position'] == -1].index, df['Close'][df['position'] == -1], 'v', markersize=10, color='k')
plt.ylabel('Price')
plt.xlabel('Date')
plt.title('Trading Strategy for ' + stock)
plt.legend()
plt.grid()
plt.show()
```

This script fetches historical data for a given stock, calculates short-term and long-term moving averages, generates trading signals based on these averages (buy when the short-term average goes above the long-term average, sell when it goes below), and plots the stock price, moving averages and trading signals.

Please note that this is a very basic trading strategy and is not guaranteed to be profitable. In a real-world scenario, you would likely need a much more complex strategy, possibly involving machine learning algorithms, and you would also need to take into account transaction costs and other factors.