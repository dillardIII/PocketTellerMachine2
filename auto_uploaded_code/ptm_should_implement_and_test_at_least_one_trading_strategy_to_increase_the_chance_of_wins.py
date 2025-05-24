Sure, here is a simple Python code implementing a Moving Average Crossover strategy using pandas. This strategy is based on the idea that if the short term moving average crosses above the long term moving average, it's a signal to buy and vice versa.

Please note that this is a very basic strategy and real-world trading strategies can be much more complex and involve many other factors.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Download historical data as dataframe
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2021-12-31")

# Calculate short-term simple moving average
ShortEMA = df.Close.ewm(span=12, adjust=False).mean()

# Calculate long-term simple moving average
LongEMA = df.Close.ewm(span=26, adjust=False).mean()

# Create signals based on crossover
df['Buy_Signal'] = np.where(ShortEMA > LongEMA, 1, 0)
df['Sell_Signal'] = np.where(ShortEMA < LongEMA, -1, 0)

# Implement the trading strategy
df['Buy_Trade'] = np.where(df['Buy_Signal'] > df['Buy_Signal'].shift(1), df['Close'], 0)
df['Sell_Trade'] = np.where(df['Sell_Signal'] < df['Sell_Signal'].shift(1), df['Close'], 0)

# Plot the trading strategy
plt.figure(figsize=(12,5))
plt.plot(df['Close'], label='Close Price', color='blue', alpha=0.35)
plt.plot(ShortEMA, label='Short/Fast EMA', color='red', alpha=0.35)
plt.plot(LongEMA, label='Long/Slow EMA', color='green', alpha=0.35)
plt.scatter(df.index, df['Buy_Trade'], color='green', marker='^', alpha=1)
plt.scatter(df.index, df['Sell_Trade'], color='red', marker='v', alpha=1)
plt.title('Apple Close Price Buy & Sell Signals')
plt.xlabel('Date',fontsize=15)
plt.ylabel('Close Price USD ($)',fontsize=15)
plt.legend(loc='upper left')
plt.show()
```

This code will plot the closing price of Apple's stock along with the short and long term moving averages. Buy signals are marked with a green up arrow and sell signals are marked with a red down arrow.

Please note that this is a simulation and the results may not reflect actual trading conditions. Always consult with a financial advisor before making trading decisions.