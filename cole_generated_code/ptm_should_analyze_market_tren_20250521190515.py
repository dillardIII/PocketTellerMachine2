To write a Python code for analyzing market trends and opportunities for potential profitable trades, we need to use libraries like pandas for data manipulation, matplotlib for data visualization, and yfinance to download the stock data. Here is a simple example:

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
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

# See your data
print(tickerDf)

# Plot the close prices
plt.figure(figsize=(10,6))
plt.grid(True)
plt.plot(tickerDf['Close'])
plt.title('Close Prices')
plt.xlabel('Date')
plt.ylabel('Close Prices')
plt.show()

# Calculate the moving average
tickerDf['MA_50'] = tickerDf['Close'].rolling(50).mean()
tickerDf['MA_200'] = tickerDf['Close'].rolling(200).mean()

# Plot the close prices and moving averages
plt.figure(figsize=(10,6))
plt.grid(True)
plt.plot(tickerDf['Close'],label='Close')
plt.plot(tickerDf['MA_50'], label='MA 50 day')
plt.plot(tickerDf['MA_200'], label='MA 200 day')
plt.title('Close Prices & Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc=2)
plt.show()
```

This script downloads the historical price data for the Apple stock from 2010 to 2020, plots the close prices, calculates the 50-day and 200-day moving averages, and plots these moving averages. 

The moving averages are used to identify the trend direction. If the 50-day moving average is above the 200-day moving average, it could be an upward trend, which might be a good opportunity to buy. If the 50-day moving average is below the 200-day moving average, it could be a downward trend, which might be a good opportunity to sell.

Please note that this is a very basic form of analysis and should not be used as the sole decision-making tool for trading. It's always recommended to use more sophisticated tools and techniques for market analysis.