Sure, I can provide you with a simple Python code that simulates a basic trading strategy. However, please note that this is a very simplified version and real trading strategies involve complex algorithms, risk management and are based on deep financial knowledge.

This Python code uses a simple moving average crossover strategy. When the short-term average is above the long-term average, it indicates a buy signal, and when the short-term average is below the long-term average, it indicates a sell signal.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be analyzed
stock = 'AAPL'

# Define the data range
start_date = '01/01/2010'
end_date = '31/12/2020'

# Get the stock data
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short-term and long-term moving averages
short_term_avg = df['Close'].rolling(window=20).mean()
long_term_avg = df['Close'].rolling(window=100).mean()

# Create signals based on crossover
df['Buy_Signal'] = np.where(short_term_avg > long_term_avg, 1, 0)
df['Sell_Signal'] = np.where(short_term_avg < long_term_avg, -1, 0)

# Plot the stock price and the buy and sell signals
plt.figure(figsize=(12,5))
plt.plot(df['Close'], label='Stock Price', color='blue')
plt.plot(short_term_avg, label='Short-term Average', color='red')
plt.plot(long_term_avg, label='Long-term Average', color='black')
plt.plot(df['Buy_Signal'], label='Buy', color='green')
plt.plot(df['Sell_Signal'], label='Sell', color='red')
plt.legend(loc='best')
plt.show()
```

This code will plot the stock price, the moving averages and the buy/sell signals. You can adjust the window size for the short-term and long-term averages to test different strategies. Please note that you will need to install the `pandas_datareader` library to fetch the stock data.