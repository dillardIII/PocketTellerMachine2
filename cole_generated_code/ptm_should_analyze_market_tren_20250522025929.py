To analyze market trends and patterns, we can use Python libraries like pandas for data manipulation, matplotlib for data visualization, and yfinance to download historical market data from Yahoo Finance. 

Here's a simple example of how you could use these libraries to analyze the closing prices of a stock:

```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2022-12-31')

# Calculate the moving average
data['MA_50'] = data['Close'].rolling(window=50).mean()
data['MA_200'] = data['Close'].rolling(window=200).mean()

# Plot closing price and moving averages
plt.figure(figsize=(10,5))
plt.title('Closing Prices and Moving Averages of ' + ticker)
plt.plot(data['Close'], label='Close')
plt.plot(data['MA_50'], label='50-day Moving Average')
plt.plot(data['MA_200'], label='200-day Moving Average')
plt.legend(loc='upper left')
plt.show()
```

This script downloads the historical data for the Apple stock, calculates the 50-day and 200-day moving averages, and plots the closing prices and moving averages. 

The moving averages smooth out price data to create a single flowing line, making it easier to identify the direction of the trend. When the 50-day moving average is above the 200-day moving average, it may be a good time to buy. When it's below, it may be a good time to sell.

Please note that this is a very basic form of analysis and should not be used as the sole basis for any trading decisions. More sophisticated methods would take into account many other factors and use more complex mathematical models.