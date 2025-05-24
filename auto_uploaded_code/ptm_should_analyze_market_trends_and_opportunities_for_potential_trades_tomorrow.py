To analyze market trends and opportunities for potential trades, we'll need to use a library like pandas for data manipulation and analysis, and yfinance to download stock price data. We'll also use matplotlib for data visualization.

Here's a simple Python script that downloads historical data for a specific stock, calculates its moving average, and plots the data:

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for desired ticker symbol
ticker = 'AAPL'
tickerData = yf.Ticker(ticker)
df = tickerData.history(period='1d', start='2020-1-1', end='2022-12-31')

# Calculate moving average
df['MA_50'] = df['Close'].rolling(window=50).mean()
df['MA_200'] = df['Close'].rolling(window=200).mean()

# Plot closing price and moving averages
plt.figure(figsize=(12,6))
plt.plot(df['Close'], label='Closing Price')
plt.plot(df['MA_50'], label='50 Day MA')
plt.plot(df['MA_200'], label='200 Day MA')
plt.title('Historical Stock Value')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend(loc='best')
plt.show()
```

This script will plot the closing price, 50-day moving average, and 200-day moving average for Apple's stock. The moving averages are commonly used to identify trends and trading opportunities.

Please note that this is a very basic form of market trend analysis and doesn't take into account many factors that can influence stock prices. For more sophisticated analysis, you might want to consider using machine learning algorithms or other advanced statistical techniques.