Sure, here's a simple example of a Python code implementing a basic trading strategy using Moving Average Crossover. This strategy is one of the most commonly used strategies in trading. It involves two moving averages, one short-term and one long-term. When the short-term moving average crosses above the long-term moving average, it's a signal to buy. When it crosses below, it's a signal to sell.

Please note that this is a very simplified example and real-world trading strategies are much more complex and involve many other factors.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = pdr.get_data_yahoo(tickerSymbol, start='2019-07-01', end='2021-07-01')

# Calculate short-term and long-term moving averages
tickerData['Short_MA'] = tickerData['Close'].rolling(window=20).mean()
tickerData['Long_MA'] = tickerData['Close'].rolling(window=100).mean()

# Create a column to hold the buy/sell signals
tickerData['Buy_Signal'] = np.where(tickerData['Short_MA'] > tickerData['Long_MA'], 1, 0)
tickerData['Sell_Signal'] = np.where(tickerData['Short_MA'] < tickerData['Long_MA'], -1, 0)

# Plot the close price and the moving averages
plt.figure(figsize=(12,5))
plt.plot(tickerData['Close'], label='Close Price', color='blue')
plt.plot(tickerData['Short_MA'], label='Short-term MA', color='red')
plt.plot(tickerData['Long_MA'], label='Long-term MA', color='green')
plt.title('Close Price and Moving Averages')
plt.legend()
plt.show()

# Print the last 10 rows of the data
print(tickerData.tail(10))
```

This code uses Yahoo Finance to get the historical data of a stock (in this case, Apple), calculates the moving averages, generates the buy/sell signals based on the moving averages, and plots the close price and the moving averages.

Please note that you need to install the `pandas_datareader` library to get the data from Yahoo Finance. You can install it using pip:

```bash
pip install pandas_datareader
```

Also, this is a very basic strategy and may not be profitable in real trading. Always backtest your strategies before using them in live trading.