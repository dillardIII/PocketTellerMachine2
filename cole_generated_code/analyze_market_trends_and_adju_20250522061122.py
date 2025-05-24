To analyze market trends and adjust trading parameters, we would need access to real-time market data. This data is usually provided by APIs from financial market data providers like Alpha Vantage, Yahoo Finance, etc. 

Below is a simple example of how you might use Python to analyze market trends using the pandas library for data manipulation and matplotlib for data visualization. This example uses the yfinance library to download stock price data from Yahoo Finance.

Please note that this is a simplified example and real trading algorithms can be very complex and involve many factors.

```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = 'AAPL'
tickerData = yf.Ticker(ticker)
df = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Calculate moving averages
short_rolling = df.Close.rolling(window=20).mean()
long_rolling = df.Close.rolling(window=100).mean()

# Plot closing price, short and long moving averages
plt.figure(figsize=(16,9))
plt.title('Close Price History')
plt.plot(df['Close'], label=ticker, color='blue')
plt.plot(short_rolling, label='20 day rolling mean', color='red')
plt.plot(long_rolling, label='100 day rolling mean', color='green')
plt.legend(loc='upper left')
plt.show()

# Adjust trading parameters based on moving averages
# This is a simple strategy where we buy when the short moving average is above the long moving average
# and we sell when it's the opposite
df['Buy_Signal'] = (short_rolling > long_rolling)
df['Sell_Signal'] = (short_rolling < long_rolling)
```

This code will plot the closing price of the stock along with its short-term and long-term moving averages. It will also create a buy signal when the short-term moving average is above the long-term moving average and a sell signal when it's the opposite. This is a very basic trading strategy and should not be used for real trading without further refinement and testing.