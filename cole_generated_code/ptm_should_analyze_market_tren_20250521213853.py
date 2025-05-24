To analyze market trends and patterns, you would need historical market data. This data can be obtained from various sources, such as Yahoo Finance, Google Finance, or any other financial data provider. Here is a basic example of how you can use Python to analyze market trends and patterns using pandas, numpy, matplotlib, and yfinance libraries.

Please note that this is a simple example and real-world trading systems are much more complex and take into account many more factors.

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

# Plot closing price, short and long windows of moving averages
plt.figure(figsize=(16,9))
plt.title('Close Prices & Moving Averages', fontsize=16)
plt.plot(df.Close.index, df.Close, label=f'{ticker} close price', color='blue')
plt.plot(short_rolling.index, short_rolling, label='20 days rolling', color='red')
plt.plot(long_rolling.index, long_rolling, label='100 days rolling', color='black')
plt.legend()
plt.show()

# Create signals
signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0
signals['short_mavg'] = df.Close.rolling(window=20, min_periods=1, center=False).mean()
signals['long_mavg'] = df.Close.rolling(window=100, min_periods=1, center=False).mean()
signals['signal'][20:] = np.where(signals['short_mavg'][20:] > signals['long_mavg'][20:], 1.0, 0.0)   
signals['positions'] = signals['signal'].diff()

# Print potential trading opportunities
print(signals[signals.positions != 0.0])
```

In this code, we first download historical data for the Apple stock (ticker symbol 'AAPL') using the yfinance library. We then calculate the 20-day and 100-day moving averages of the closing prices. We plot these moving averages along with the closing prices.

Next, we create a signal (1 for buy, 0 for sell) whenever the short moving average crosses the long moving average. We then print the dates where such a crossover occurs, which could be potential trading opportunities.

Please note that this is a very simplistic trading strategy and should not be used for real trading without proper backtesting and risk management.