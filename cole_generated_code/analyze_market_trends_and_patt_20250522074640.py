Analyzing market trends and patterns involves complex algorithms and requires historical market data. Here is a simple example of how you might use Python to analyze stock prices using the pandas library for data manipulation and matplotlib for data visualization. 

This code fetches historical stock data from Yahoo Finance, calculates the moving average of the stock price, and plots the stock price and its moving average.

```python
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

# Fetch historical stock data from Yahoo Finance
df = web.DataReader('AAPL', data_source='yahoo', start='2012-01-01', end='2022-12-31')

# Calculate the moving average
df['Moving Average'] = df['Close'].rolling(window=50).mean()

# Plot the stock price and its moving average
plt.figure(figsize=(12,6))
plt.plot(df['Close'], label='Close Price')
plt.plot(df['Moving Average'], label='50 Day Moving Avg')
plt.title('Apple Stock Price History')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend(loc='upper left')
plt.show()
```

Please note that this is a very basic example and real-world trading decisions would require a much more sophisticated analysis, possibly involving machine learning algorithms to predict future prices. It's also important to remember that past performance is not always indicative of future results in stock trading.