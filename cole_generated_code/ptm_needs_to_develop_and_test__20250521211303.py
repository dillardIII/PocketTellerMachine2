Sure, I can give you a basic example of a trading strategy using Python. This strategy will be a simple moving average crossover strategy. This strategy is used to identify points in time when you might want to buy or sell stocks based on the crossing of two moving averages of different periods.

Here's the Python code:

```python
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

# Define the stock symbol and the time period
stock = 'AAPL'
start_date = '01-01-2020'
end_date = '12-31-2020'

# Fetch the stock data
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short-term simple moving average
short_sma = df.Close.rolling(window=20).mean()

# Calculate the long-term simple moving average
long_sma = df.Close.rolling(window=100).mean()

# Create a new dataframe to store all the data
data = pd.DataFrame()
data[stock] = df.Close
data['short_sma'] = short_sma
data['long_sma'] = long_sma

# Create signals
data['buy_signal'] = (short_sma > long_sma)
data['sell_signal'] = (short_sma < long_sma)

# Plot the stock price and the buy and sell signals
plt.figure(figsize=(12,5))
plt.plot(data[stock], label=stock, color='blue')
plt.plot(data['short_sma'], label='Short-term SMA', color='red')
plt.plot(data['long_sma'], label='Long-term SMA', color='green')
plt.scatter(data.index, data[data['buy_signal']].short_sma, color='green', marker='^', alpha=1)
plt.scatter(data.index, data[data['sell_signal']].short_sma, color='red', marker='v', alpha=1)
plt.title('Stock Price with Buy & Sell Signals')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.grid()
plt.show()
```

This code fetches historical stock data for a given stock symbol from Yahoo Finance, calculates the short-term and long-term simple moving averages, generates buy and sell signals based on when these two averages cross, and plots the stock price along with the buy and sell signals.

Please note that this is a very simple strategy and may not be profitable in real trading. It's just a starting point for developing and testing more complex strategies.