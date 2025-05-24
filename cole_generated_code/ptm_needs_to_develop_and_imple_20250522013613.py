Sure, I can provide a simple example of a Python code for a trading strategy using Moving Average Crossover. This strategy is one of the most commonly used strategies in trading. It involves tracking two moving averages: one fast and one slow. When the fast moving average crosses above the slow moving average, it's a signal to buy. When it crosses below, it's a signal to sell.

Please note that this is a very basic strategy and real-world trading strategies can be much more complex and involve many more factors.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the period for the short/fast moving average and the long/slow moving average
short_period = 20
long_period = 100

# Get the stock data
df = web.DataReader(stock, data_source='yahoo', start='01-01-2010')

# Calculate the short/fast moving average
df['Short'] = df['Close'].rolling(window=short_period).mean()

# Calculate the long/slow moving average
df['Long'] = df['Close'].rolling(window=long_period).mean()

# Create a column 'Signal' such that if the short moving average is greater than the long moving average, 
# then set 'Signal' as 1 else 0
df['Signal'] = 0.0  
df['Signal'][short_period:] = np.where(df['Short'][short_period:] > df['Long'][short_period:], 1.0, 0.0)   

# Create a column 'Position' which is the difference of the 'Signal' column and its previous row
df['Position'] = df['Signal'].diff()

# Plotting
plt.figure(figsize=(20,10))
plt.plot(df['Close'], label='Close Price', color='blue',alpha=0.35)
plt.plot(df['Short'], label='Short Moving Average', color='red',alpha=0.35)
plt.plot(df['Long'], label='Long Moving Average', color='green',alpha=0.35)
plt.plot(df.loc[df.Position == 1.0].index, 
         df.Short[df.Position == 1.0],
         '^', markersize=10, color='m',label='buy')
plt.plot(df.loc[df.Position == -1.0].index, 
         df.Short[df.Position == -1.0],
         'v', markersize=10, color='k',label='sell')
plt.ylabel('Price in $')
plt.xlabel('Date')
plt.title('Trading strategy for '+ stock)
plt.legend()
plt.grid()
plt.show()
```

This code will plot the close price, short moving average and long moving average of the stock. It will also plot buy signals when the short moving average crosses above the long moving average and sell signals when the short moving average crosses below the long moving average.

Please note that you need to install pandas_datareader, matplotlib and pandas libraries in your Python environment to run this code. You can install them using pip:

```python
pip install pandas_datareader matplotlib pandas
```

Also, this is a very basic trading strategy and should not be used for real trading without proper backtesting and risk management.