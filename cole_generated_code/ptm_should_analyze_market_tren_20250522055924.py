Sure, here is a simple Python code using pandas and yfinance to analyze market trends and patterns. This code will fetch historical data for a specific stock, calculate its moving averages, and plot the data. 

Please note that this is a very basic example and real trading algorithms are much more complex and take into account many more factors.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for desired ticker symbol
ticker = 'AAPL'
tickerData = yf.Ticker(ticker)
df = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Calculate moving averages
df['MA10'] = df['Close'].rolling(10).mean()
df['MA50'] = df['Close'].rolling(50).mean()

# Create a plot
plt.figure(figsize=(12,6))
plt.grid(True)
plt.plot(df['Close'],label='Close Price')
plt.plot(df['MA10'], label='MA 10 day')
plt.plot(df['MA50'], label='MA 50 day')
plt.legend(loc=2)

# Show the plot
plt.show()
```

This script will plot the closing price, 10-day moving average, and 50-day moving average for Apple's stock. When the 10-day moving average crosses above the 50-day moving average, it might be a good time to buy. Conversely, when the 10-day moving average crosses below the 50-day moving average, it might be a good time to sell.

Please note that this is a very simplistic trading strategy and should not be used for actual trading without further enhancements and testing.