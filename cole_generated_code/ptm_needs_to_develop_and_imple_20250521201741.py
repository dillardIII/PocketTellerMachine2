Sure, I can provide a simple example of a Python code for a trading strategy. Please note that this is a basic example and real-world trading strategies can be much more complex and require thorough testing.

This strategy is called Moving Average Crossover. It's a simple strategy that buys when the short-term moving average crosses above the long-term moving average, and sells when the short-term moving average crosses below the long-term moving average.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the start and end dates
start_date = '01-01-2010'
end_date = '01-01-2022'

# Get the stock data
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short-term and long-term moving averages
df['ShortMA'] = df['Close'].rolling(window=20).mean()
df['LongMA'] = df['Close'].rolling(window=100).mean()

# Create signals
df['Buy_Signal'] = np.where(df['ShortMA'] > df['LongMA'], 1, 0)
df['Sell_Signal'] = np.where(df['ShortMA'] < df['LongMA'], -1, 0)

# Generate trades
df['Trade'] = df['Buy_Signal'] + df['Sell_Signal']

# Plot the stock price and moving averages
plt.figure(figsize=(12,5))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(df['ShortMA'], label='Short-term MA', color='red')
plt.plot(df['LongMA'], label='Long-term MA', color='green')
plt.legend(loc='upper left')
plt.show()

# Print the trades
print(df['Trade'])
```

This script will print out a series of 1s, -1s, and 0s. A 1 indicates a buy signal, a -1 indicates a sell signal, and a 0 indicates no action. 

Please note that this is a very simple strategy and doesn't take into account transaction costs, slippage, risk management, or other important factors for a real-world trading strategy. It's also using historical data, and past performance is not indicative of future results. Always test your strategies thoroughly before live trading.