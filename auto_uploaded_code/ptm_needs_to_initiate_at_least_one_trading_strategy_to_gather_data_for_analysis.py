Sure, to accomplish that, we could define a very simple trading strategy based on moving average. For this, we will use `pandas` for handling data, and `yfinance` to download stock price data from Yahoo Finance.

Below is an example of a Python code implementing a simple trading strategy called Moving Average Crossover Strategy:

```python
import pandas as pd
import yfinance as yf

# Download historical data
data = yf.download('AAPL', start='2019-01-01', end='2020-12-31')

# Calculate the short-term exponential moving average(EMA)
shortEMA = data.Close.ewm(span=12, adjust=False).mean()

# Calculate the long-term EMA
longEMA = data.Close.ewm(span=26, adjust=False).mean()

# Create Trading Signals
data['Signal'] = 0.0  
data['Signal'][shortEMA > longEMA] = 1.0
data['Signal'][shortEMA < longEMA] = -1.0

# Generate Trading Orders
data['Order'] = data['Signal'].diff()

# print data
print(data)
```

In this strategy, when the short-term moving average exceeds the long-term moving average, it generates a buy signal, represented by '1.0'. When the short-term moving average drops below the long-term moving average, it generates a sell signal, represented by '-1.0'. 

This trading strategy is only for demonstration and not recommended for real trading without proper validation and modification. Also, it's highly advised to include transaction costs in your backtesting process to get more accurate and reliable results.