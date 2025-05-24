Sure, I can provide a simple example of a Python code that simulates a basic trading strategy. This strategy will be based on a simple moving average. 

Please note that this is a very basic example and real trading strategies involve much more complex analysis and risk management.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used in the strategy
stock = 'AAPL'

# Define the period for the moving average
period = 20

# Get the stock data
df = web.DataReader(stock, data_source='yahoo', start='01-01-2020')

# Calculate the moving average
df['SMA'] = df['Close'].rolling(window=period).mean()

# Create a column to hold the trading signals
df['Signal'] = 0.0

# Generate trading signals based on the crossover of the close price and the moving average
df['Signal'][period:] = np.where(df['Close'][period:] > df['SMA'][period:], 1.0, 0.0)

# Generate trading orders based on the trading signals
df['Positions'] = df['Signal'].diff()

# Plot the close price, the moving average and the trading signals
plt.figure(figsize=(20,10))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(df['SMA'], label='Simple Moving Average', color='red')
plt.plot(df.loc[df.Positions == 1.0].index, df['Close'][df.Positions == 1.0], '^', markersize=10, color='green', label='Buy')
plt.plot(df.loc[df.Positions == -1.0].index, df['Close'][df.Positions == -1.0], 'v', markersize=10, color='red', label='Sell')
plt.title('Trading Strategy for ' + stock)
plt.legend()
plt.show()
```

This script fetches the historical data for a specific stock (in this case, Apple Inc.), calculates a simple moving average over a defined period, and generates trading signals based on the crossover of the close price and the moving average. It then plots the close price, the moving average, and the trading signals on a chart.

Please make sure to install the necessary libraries (pandas, pandas_datareader, matplotlib, numpy) before running the script.