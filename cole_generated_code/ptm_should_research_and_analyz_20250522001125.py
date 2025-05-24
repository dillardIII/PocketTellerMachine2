To complete this task, we would need to use a Python library such as pandas for data analysis, and yfinance to download the historical market data from Yahoo Finance. Here's a simple example of how you might start this task:

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# See your data
print(tickerDf)

# Plot the close prices
plt.figure(figsize=(10,6))
plt.grid(True)
plt.plot(tickerDf['Close'])
plt.title('Close Prices')
plt.show()

# Calculate the 20 days moving average
tickerDf['MA20'] = tickerDf['Close'].rolling(window=20).mean()

# Plot the close prices and moving average
plt.figure(figsize=(10,6))
plt.grid(True)
plt.plot(tickerDf['Close'],label='Close')
plt.plot(tickerDf['MA20'], label='MA 20 day')
plt.legend(loc=2)
plt.title('Close Prices with Moving Average')
plt.show()
```

This code will download the historical data for Apple Inc. from 2010 to 2020, plot the close prices, calculate the 20-day moving average, and plot it. 

Please note that this is a very basic example and real trading algorithms can be very complex and take into account many other factors. Also, this code does not identify potential trading opportunities, it just calculates and plots the moving average. Identifying trading opportunities usually involves complex strategies and risk management techniques.