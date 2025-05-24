Creating a Python script to analyze market trends and patterns is a complex task and requires a deep understanding of both programming and financial markets. Here is a basic example of how you can start with Python using pandas and yfinance libraries. This code will fetch the historical data of a specific stock and calculate its moving average, which is a common indicator of market trends.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Calculate the moving average
tickerDf['MA_50'] = tickerDf['Close'].rolling(window=50).mean()
tickerDf['MA_200'] = tickerDf['Close'].rolling(window=200).mean()

# Plot the close price and the moving averages
plt.figure(figsize=(10,5))
plt.plot(tickerDf['Close'], label='Close Price')
plt.plot(tickerDf['MA_50'], label='50-day MA')
plt.plot(tickerDf['MA_200'], label='200-day MA')
plt.legend(loc='upper left')
plt.title('Market trends for ' + tickerSymbol)
plt.show()
```

This code will plot the close price and the 50-day and 200-day moving averages for Apple's stock. When the 50-day moving average crosses above the 200-day moving average, it's often seen as a bullish (positive) signal, and when it crosses below, it's seen as a bearish (negative) signal. 

Please note that this is a very basic form of market analysis and real trading algorithms use much more complex strategies and take into account many more factors. Also, this code does not make any trading decisions, it only analyzes and visualizes data.