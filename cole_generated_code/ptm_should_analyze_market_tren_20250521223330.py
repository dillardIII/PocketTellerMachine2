To analyze market trends and identify potential trading opportunities, we can use Python libraries like pandas for data manipulation, numpy for numerical computation, matplotlib for visualization, and yfinance to download the stock data. 

Here is a simple example of how you might start:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = "AAPL"
tickerData = yf.Ticker(ticker)
df = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Calculate moving averages
short_rolling = df.Close.rolling(window=20).mean()
long_rolling = df.Close.rolling(window=100).mean()

# Plot closing price, short-term and long-term moving averages 
plt.figure(figsize=(16,9))
plt.title('Close Prices & Moving Averages', fontsize=16)
plt.plot(df.Close, label=ticker)
plt.plot(short_rolling, label='20 day rolling mean')
plt.plot(long_rolling, label='100 day rolling mean')
plt.legend(loc='upper left')
plt.show()

# Identify potential trading opportunities
# Buy when the short-term MA crosses above the long-term MA, sell when it crosses below
df['Buy_Signal'] = np.where(short_rolling > long_rolling, 1, 0)
df['Sell_Signal'] = np.where(short_rolling < long_rolling, -1, 0)

# Print potential trading opportunities
print(df[df['Buy_Signal'] == 1])
print(df[df['Sell_Signal'] == -1])
```

This script downloads historical data for a specific ticker symbol (in this case, Apple), calculates short-term (20-day) and long-term (100-day) moving averages, and plots these along with the closing price. It then identifies potential trading opportunities based on the moving averages: a buy signal is generated when the short-term moving average crosses above the long-term moving average, and a sell signal is generated when it crosses below.

Please note that this is a very basic form of trend analysis and should not be used for actual trading without further refinement and testing. For instance, you might want to consider additional factors like trading volume, other technical indicators, or fundamental analysis.