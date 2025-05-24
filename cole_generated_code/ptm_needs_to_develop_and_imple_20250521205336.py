Sure, I can provide you with a simple Python code that implements a basic trading strategy. This strategy is called Moving Average Crossover, which is used to identify when to buy and sell stocks.

Please note that this is a very basic strategy and real-world trading strategies can be much more complex and involve many more factors.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the period for the moving averages
short_period = 50
long_period = 200

# Get the stock data
df = web.DataReader(stock, data_source='yahoo', start='01-01-2010')

# Calculate the short and long period moving averages
df['Short_MA'] = df['Close'].rolling(window=short_period).mean()
df['Long_MA'] = df['Close'].rolling(window=long_period).mean()

# Create a column to hold the trading signals
df['Signal'] = 0.0
df['Signal'][short_period:] = np.where(df['Short_MA'][short_period:] > df['Long_MA'][short_period:], 1.0, 0.0)

# Generate trading orders
df['Position'] = df['Signal'].diff()

# Plot the data
plt.figure(figsize=(20,10))
plt.plot(df['Close'], label=stock)
plt.plot(df['Short_MA'], label='Short Moving Average')
plt.plot(df['Long_MA'], label='Long Moving Average')
plt.plot(df.loc[df.Position == 1.0].index, df.Short_MA[df.Position == 1.0], '^', markersize=10, color='g', label='buy')
plt.plot(df.loc[df.Position == -1.0].index, df.Short_MA[df.Position == -1.0], 'v', markersize=10, color='r', label='sell')
plt.title('Moving Average Crossover Trading Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()
```

This code will plot the closing price of the stock, the short moving average, the long moving average, and the points where the strategy indicates to buy (green up arrows) and sell (red down arrows).

Please note that this code requires the `pandas`, `numpy`, `matplotlib`, and `pandas_datareader` libraries. Also, this strategy does not take into account transaction costs or taxes, which could significantly impact the performance of the strategy. Always consult with a financial advisor before making trading decisions.