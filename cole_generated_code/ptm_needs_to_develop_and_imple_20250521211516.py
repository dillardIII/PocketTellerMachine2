Sure, here is a simple Python code that uses a basic trading strategy called Moving Average Crossover. This strategy is used to identify when to buy and sell stocks based on the moving averages of the stock prices.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the data period
start_date = '01-01-2010'
end_date = '01-01-2022'

# Get the stock data
df = pdr.get_data_yahoo(stock, start=start_date, end=end_date)

# Calculate the short-term exponential moving average (EMA)
ShortEMA = df.Close.ewm(span=12, adjust=False).mean()

# Calculate the long-term EMA
LongEMA = df.Close.ewm(span=26, adjust=False).mean()

# Create signals based on the crossover of the short and long EMA
df['Buy_Signal'] = np.where(ShortEMA > LongEMA, 1, 0)
df['Sell_Signal'] = np.where(ShortEMA < LongEMA, -1, 0)

# Plot the stock price and the buy and sell signals
plt.figure(figsize=(12,5))
plt.title('Buy and Sell Plot')
plt.plot(df['Close'], label='Close Price', color='blue', alpha=0.35)
plt.plot(ShortEMA, label='Short/Fast EMA', color='red', alpha=0.35)
plt.plot(LongEMA, label='Long/Slow EMA', color='green', alpha=0.35)
plt.scatter(df.index, df[df['Buy_Signal'] == 1]['Close'], color='green', marker='^', alpha=1)
plt.scatter(df.index, df[df['Sell_Signal'] == -1]['Close'], color='red', marker='v', alpha=1)
plt.xlabel('Date',fontsize=18)
plt.ylabel('Close Price USD ($)',fontsize=18)
plt.show()
```

This code will plot the stock prices and the buy and sell signals based on the EMA crossover. When the short-term EMA crosses above the long-term EMA, it's a signal to buy. Conversely, when the short-term EMA crosses below the long-term EMA, it's a signal to sell.

Please note that this is a very simple trading strategy and may not be suitable for all types of markets or stocks. It's always recommended to use more sophisticated strategies and consider other factors such as volume, volatility, and fundamental analysis.