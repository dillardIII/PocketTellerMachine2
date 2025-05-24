Sure, let's create a simple Python code for a basic trading strategy using moving averages. We'll use the pandas library for data manipulation and matplotlib for visualization. Please note that this is a very basic strategy and should be used for educational purposes only.

```python
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the data range
start_date = '01/01/2020'
end_date = '12/31/2020'

# Get the stock data
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short-term simple moving average (SMA)
short_sma = df.Close.rolling(window=20).mean()

# Calculate the long-term SMA
long_sma = df.Close.rolling(window=100).mean()

# Create a new column in the DataFrame to hold the trading signals
df['signal'] = 0.0

# Generate trading signals based on the crossover of the short and long SMAs
df['signal'][short_sma > long_sma] = 1.0

# Create a new column in the DataFrame to hold the trading positions
df['position'] = df['signal'].diff()

# Plot the stock price, short-term SMA, long-term SMA, and the trading positions
plt.figure(figsize=(10, 5))
plt.plot(df['Close'], label=stock)
plt.plot(short_sma, label='20-day SMA')
plt.plot(long_sma, label='100-day SMA')
plt.plot(df[df['position'] == 1.0].index, df['Close'][df['position'] == 1.0], '^', markersize=10, color='g', label='buy')
plt.plot(df[df['position'] == -1.0].index, df['Close'][df['position'] == -1.0], 'v', markersize=10, color='r', label='sell')
plt.title('Trading Strategy Based on Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()
```

This script implements a simple moving average crossover strategy. When the short-term SMA crosses above the long-term SMA, it generates a buy signal. Conversely, when the short-term SMA crosses below the long-term SMA, it generates a sell signal. The script then plots the stock price, the two SMAs, and the trading positions on a chart.