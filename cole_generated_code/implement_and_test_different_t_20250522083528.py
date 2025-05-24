In order to implement and test different trading strategies, we can use Python libraries such as pandas, numpy, and yfinance to fetch and analyze stock data. Here's a simple example of how you might implement and test a moving average crossover strategy:

```python
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for desired ticker symbol 
df = yf.download('AAPL','2020-01-01','2021-12-31')

# Calculate short-term simple moving average
ShortEMA = df.Close.ewm(span=12, adjust=False).mean()

# Calculate long-term simple moving average
LongEMA = df.Close.ewm(span=26, adjust=False).mean()

# Create signals based on crossover
df['Buy_Signal'] = np.where(ShortEMA > LongEMA, 1, 0)
df['Sell_Signal'] = np.where(ShortEMA < LongEMA, -1, 0)

# Calculate daily returns
df['Return'] = df.Close.pct_change()

# Calculate strategy returns
df['Strategy_Return'] = df.Return * df.Buy_Signal.shift()

# Calculate cumulative returns
df['Buy_and_Hold'] = np.cumprod(1 + df['Return'])
df['Strategy'] = np.cumprod(1 + df['Strategy_Return'])

# Plot the strategy and buy and hold cumulative returns
plt.figure(figsize=(12,5))
plt.plot(df['Buy_and_Hold'], color='blue', label="Buy and Hold Strategy")
plt.plot(df['Strategy'], color='red', label="EMA Crossover Strategy")
plt.title('Buy and Hold Strategy Vs EMA Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.show()
```

This code implements a simple moving average crossover strategy, where you buy when the short-term moving average crosses above the long-term moving average, and sell when the short-term moving average crosses below the long-term moving average. It then calculates the daily and cumulative returns for this strategy, and compares it to a simple buy and hold strategy.

Please note that this is a simplified example and doesn't take into account trading costs or slippage. Also, past performance is not indicative of future results. It's important to thoroughly backtest any trading strategy before live trading.