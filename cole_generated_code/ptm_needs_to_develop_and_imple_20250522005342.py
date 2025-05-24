Here is a simple Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is one of the most commonly used strategies in trading. It involves two moving averages, one short period and one long period. When the short period moving average crosses above the long period moving average, it's a signal to buy. Conversely, when the short period moving average crosses below the long period moving average, it's a signal to sell.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the period for the short and long moving averages
short_period = 50
long_period = 200

# Get the stock data
df = pdr.get_data_yahoo(stock)

# Calculate the short and long moving averages
df['Short_MA'] = df['Close'].rolling(window=short_period).mean()
df['Long_MA'] = df['Close'].rolling(window=long_period).mean()

# Create a column 'Signal' such that if the short moving average is greater than the long moving average, 
# then set Signal as 1 else 0
df['Signal'] = 0.0  
df['Signal'][short_period:] = np.where(df['Short_MA'][short_period:] > df['Long_MA'][short_period:], 1.0, 0.0)   

# Create a column 'Position' which is the difference of the present and previous day's 'Signal'
df['Position'] = df['Signal'].diff()

# Plotting
plt.figure(figsize=(20,10))
# plot close price, short-term and long-term moving averages 
df['Close'].plot(color='blue', label= 'Close Price') 
df['Short_MA'].plot(color='red', label='Short-term MA') 
df['Long_MA'].plot(color='green', label='Long-term MA')

# plot 'buy' signals
plt.plot(df[df['Position'] == 1].index, 
         df['Short_MA'][df['Position'] == 1], 
         '^', markersize=10, color='m', label='buy')

# plot 'sell' signals
plt.plot(df[df['Position'] == -1].index, 
         df['Short_MA'][df['Position'] == -1], 
         'v', markersize=10, color='k', label='sell')
plt.ylabel('Price in $')
plt.xlabel('Date')
plt.title('Trading strategy for ' + stock)
plt.legend()
plt.grid()
plt.show()
```

Please note that this is a very basic trading strategy and should not be used for actual trading without further refinement. Also, this code assumes that you have pandas, pandas_datareader, numpy and matplotlib installed in your Python environment.