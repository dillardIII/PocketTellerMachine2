To analyze market trends and patterns, we need historical data of the market. We can use libraries like `pandas` for data manipulation, `numpy` for numerical computation, `matplotlib` and `seaborn` for visualization, and `yfinance` to download the historical market data from Yahoo finance.

Here is a simple Python code snippet that uses moving average strategy to identify potential trading opportunities. Please note that this is a very basic strategy and real-world trading involves more complex strategies and risk management.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for desired ticker symbol
ticker = 'AAPL'
tickerData = yf.Ticker(ticker)
df = tickerData.history(period='1d', start='2010-1-1', end='2020-12-31')

# Calculate moving averages
short_rolling = df.Close.rolling(window=20).mean()
long_rolling = df.Close.rolling(window=100).mean()

# Plot closing price, short-term and long-term moving averages 
plt.figure(figsize=(16,9))
plt.plot(df.Close.index, df.Close, label='{} price'.format(ticker))
plt.plot(short_rolling.index, short_rolling, label='20 days rolling')
plt.plot(long_rolling.index, long_rolling, label='100 days rolling')
plt.xlabel('Date')
plt.ylabel('Adjusted closing price ($)')
plt.legend()
plt.show()

# Create signals
signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0
signals['short_mavg'] = df.Close.rolling(window=20, min_periods=1, center=False).mean()
signals['long_mavg'] = df.Close.rolling(window=100, min_periods=1, center=False).mean()
signals['signal'][short_rolling > long_rolling] = 1.0

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print signals
print(signals)
```

In this code, we first download the historical data of Apple Inc. (AAPL) from Yahoo finance. Then we calculate the short-term (20 days) and long-term (100 days) moving averages of the closing prices. We plot the closing prices and moving averages to visualize the trends.

We then create a signal (1 or 0) when the short-term average is above or below the long-term average. We generate trading orders based on the changes in signals. If the signal changes from 0 to 1, it means we should buy, and if it changes from 1 to 0, we should sell.

Please note that this is a very simplistic trading strategy and is used only for demonstration purposes. Real-world trading strategies are much more complex and involve considerations for transaction costs, risk management, portfolio diversification, etc.