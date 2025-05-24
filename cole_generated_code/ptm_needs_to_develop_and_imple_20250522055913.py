Here is a simple Python code to implement a basic trading strategy using Moving Average Crossover. This strategy is one of the most commonly used strategies in trading. It involves two moving averages, one short period and one long period. When the short period moving average crosses above the long period moving average, it's a signal to buy and when it crosses below, it's a signal to sell.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used in the trading strategy
stock = 'AAPL'

# Define the start and end dates for the trading strategy
start_date = '01-01-2010'
end_date = '01-01-2022'

# Get the stock data
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short term exponential moving average (EMA)
short_EMA = df.Close.ewm(span=12, adjust=False).mean()

# Calculate the long term exponential moving average (EMA)
long_EMA = df.Close.ewm(span=26, adjust=False).mean()

# Create signals based on the crossover of the short and long EMA
df['Buy_Signal'] = np.where(short_EMA > long_EMA, 1, 0)
df['Sell_Signal'] = np.where(short_EMA < long_EMA, -1, 0)

# Generate the trading orders
df['Trade_Orders'] = df['Buy_Signal'] + df['Sell_Signal']

print(df)

# Plot the stock close price, short EMA and long EMA
plt.figure(figsize=(12,5))
plt.title('Close Price, Short EMA and Long EMA', fontsize = 18)
plt.plot(df['Close'], label='Close Price', color = 'blue', alpha = 0.35)
plt.plot(short_EMA, label='Short EMA', color = 'red', alpha = 0.35)
plt.plot(long_EMA, label='Long EMA', color = 'green', alpha = 0.35)
plt.xlabel('Date', fontsize = 18)
plt.ylabel('Close Price', fontsize = 18)
plt.show()
```

Please note that this is a very simple trading strategy and may not generate wins consistently. It's always recommended to use more sophisticated strategies and consider other factors like trading volume, market sentiment, etc. Also, it's important to backtest any strategy before live trading.