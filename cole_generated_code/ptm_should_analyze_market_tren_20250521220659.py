Creating a Python script to analyze market trends and patterns is a complex task that involves several steps. Here's a simplified example using Python's pandas library to analyze historical stock data. We'll use Yahoo Finance to get the data and matplotlib to visualize the data.

Please note that this is a very basic example and real-world trading algorithms are much more complex and also consider many other factors.

```python
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

# Use Yahoo Finance to get historical market data
yf.pdr_override()

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Collect data on this ticker
tickerData = pdr.get_data_yahoo(tickerSymbol, start='2010-1-1', end='2020-12-31')

# Calculate moving averages
tickerData['MA10'] = tickerData['Close'].rolling(10).mean()
tickerData['MA50'] = tickerData['Close'].rolling(50).mean()

# Plot closing price and moving averages
plt.figure(figsize=(10, 4))
plt.grid(True)
plt.plot(tickerData['Close'], label='Close')
plt.plot(tickerData['MA10'], label='MA10')
plt.plot(tickerData['MA50'], label='MA50')
plt.legend(loc=2)
plt.show()
```

In this script, we're fetching historical data for Apple's stock (AAPL), calculating 10-day and 50-day moving averages, and plotting the closing prices and moving averages. A moving average is a commonly used indicator that can help identify trends and patterns.

Please note that this is a very basic form of analysis and should not be used for actual trading decisions without further enhancements. Real-world trading algorithms take into account many other factors and use much more sophisticated statistical techniques.