Sure, I can provide a simple example of a trading strategy using Python. This strategy is called Moving Average Crossover, which is a popular strategy used in algorithmic trading. 

Please note that this is a very basic strategy and in real-world trading, more complex strategies and risk management techniques are used. Also, you need to install the `pandas_datareader` and `matplotlib` libraries to run this code.

Here's the Python code:

```python
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

# Define the stock to be traded
stock = 'AAPL'

# Define the start and end dates for the trading period
start_date = '01-01-2020'
end_date = '31-12-2020'

# Download the stock price data
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short-term (fast) moving average
short_MA = df['Close'].rolling(window=20).mean()

# Calculate the long-term (slow) moving average
long_MA = df['Close'].rolling(window=100).mean()

# Create a 'signal' column where if the short-term MA is greater than the long-term MA, then set to 1 (buy), else 0 (sell)
df['signal'] = 0.0  
df['signal'][short_MA > long_MA] = 1.0

# Create a 'positions' column which is the difference of the 'signal' column
df['positions'] = df['signal'].diff()

# Plotting
plt.figure(figsize=(20,10))
plt.plot(df['Close'], label='Close Price', color='blue', alpha=0.35)
plt.plot(short_MA, label='20-day MA', color='red', alpha=0.35)
plt.plot(long_MA, label='100-day MA', color='green', alpha=0.35)
plt.plot(df.loc[df.positions == 1.0].index, 
         short_MA[df.positions == 1.0],
         '^', markersize=10, color='m', label='buy')
plt.plot(df.loc[df.positions == -1.0].index, 
         short_MA[df.positions == -1.0],
         'v', markersize=10, color='k', label='sell')
plt.title('AAPL Moving Average Crossover Trading Signals')
plt.legend()
plt.grid()
plt.show()
```

This code will plot the closing price of the stock, the moving averages, and the buy/sell signals. When the short-term moving average crosses above the long-term moving average, it generates a buy signal, and when it crosses below, it generates a sell signal.

Remember, this is a very simplified example and does not take into account trading fees, slippage, and many other factors that could affect the profitability of a trading strategy. Always backtest your strategies before live trading.