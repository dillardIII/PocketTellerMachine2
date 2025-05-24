To analyze market trends and adjust trading parameters, we can use Python's Pandas library to handle data and Matplotlib for data visualization. We also need to fetch market data. For this, we can use yfinance library which allows us to access Yahoo Finance data. Here's a simple example:

```python
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Fetch data
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Calculate moving averages
data['MA10'] = data['Close'].rolling(window=10).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()

# Create a function to signal when to buy and sell an asset
def buy_sell(data):
    buy_list = []
    sell_list = []
    flag = -1

    for i in range(len(data)):
        if data['MA10'][i] > data['MA50'][i]:
            if flag != 1:
                buy_list.append(data['Close'][i])
                sell_list.append(np.nan)
                flag = 1
            else:
                buy_list.append(np.nan)
                sell_list.append(np.nan)
        elif data['MA10'][i] < data['MA50'][i]:
            if flag != 0:
                sell_list.append(data['Close'][i])
                buy_list.append(np.nan)
                flag = 0
            else:
                buy_list.append(np.nan)
                sell_list.append(np.nan)
        else:
            buy_list.append(np.nan)
            sell_list.append(np.nan)

    return (buy_list, sell_list)

# Add the buy and sell signals to the data
data['Buy_Signal_Price'] = buy_sell(data)[0]
data['Sell_Signal_Price'] = buy_sell(data)[1]

# Plot
plt.figure(figsize=(12.2, 4.5))
plt.plot(data['Close'], label='Close Price', alpha=0.35)
plt.plot(data['MA10'], label='MA10', alpha=0.35)
plt.plot(data['MA50'], label='MA50', alpha=0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], color='green', label='Buy Signal', marker='^', alpha=1)
plt.scatter(data.index, data['Sell_Signal_Price'], color='red', label='Sell Signal', marker='v', alpha=1)
plt.title('Apple Close Price History with Buy & Sell Signals')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend(loc='upper left')
plt.show()
```

This code fetches historical data for Apple Inc. (AAPL) from Yahoo Finance, calculates 10-day and 50-day moving averages, and generates buy and sell signals based on these moving averages. It then plots the closing prices, moving averages, and buy/sell signals.

Please note that this is a simple moving average crossover strategy and may not be suitable for all market conditions. Always use trading strategies suitable for your risk tolerance and investment goals.