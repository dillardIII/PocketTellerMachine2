Sure, I will provide a simple example of a trading strategy using Python. We will use the Moving Average Crossover strategy. This strategy is one of the most commonly used strategies in the trading world. It's based on the principle of buying a security when its short-term moving average crosses above its long-term moving average, and selling the security when its short-term moving average crosses below its long-term moving average.

Firstly, we need to install the necessary libraries. You can do this by running the following commands in your terminal:

```python
pip install pandas_datareader
pip install matplotlib
pip install numpy
```

Here is the Python code:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

# Fetching the data
data = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2022-12-31")

# Calculate the short-term exponential moving average (EMA)
ShortEMA = data.Close.ewm(span=12, adjust=False).mean() 

# Calculate the long-term exponential moving average (EMA)
LongEMA = data.Close.ewm(span=26, adjust=False).mean() 

# Calculate the Moving Average Convergence/Divergence (MACD)
MACD = ShortEMA - LongEMA

# Calculate the signal line
signal = MACD.ewm(span=9, adjust=False).mean()

# Create a new column to hold the trading strategy signals
data['Buy_Signal_Price'] = np.where(MACD > signal, data['Close'], np.nan)
data['Sell_Signal_Price'] = np.where(MACD < signal, data['Close'], np.nan)

# Plot the stock price, short-term EMA, long-term EMA, buy signals and sell signals
plt.figure(figsize=(12,5))
plt.title('Buy and Sell Plot', fontsize=18)
plt.plot(data['Close'], label='Close Price', color='blue', alpha=0.35)
plt.plot(ShortEMA, label='Short EMA', color='red', alpha=0.35)
plt.plot(LongEMA, label='Long EMA', color='green', alpha=0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], color='green', marker='^', alpha=1)
plt.scatter(data.index, data['Sell_Signal_Price'], color='red', marker='v', alpha=1)
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.legend(loc='upper left')
plt.show()
```

This code will plot the stock price, the short-term EMA, the long-term EMA, and points where the buy and sell signals occur. 

Please note that this is a very basic trading strategy and does not take into account many factors that could influence the performance of the strategy such as transaction costs, slippage, risk management, etc. Always backtest your strategy with historical data before live trading.