To develop and implement a variety of trading strategies, we need to use some libraries such as pandas for data manipulation, numpy for mathematical calculations, and yfinance to download the stock data. Here is a simple example of a moving average crossover strategy:

```python
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for required stocks
ticker = "AAPL"
ticker_data = yf.download(ticker,'2020-1-1','2021-12-31')

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

# Calculate SMA and EMA
ticker_data['SMA_20'] = calculate_sma(ticker_data['Close'],20)
ticker_data['EMA_20'] = calculate_ema(ticker_data['Close'],20)

# Create a function to signal when to buy and sell an asset
def implement_strategy(data):
    buy_list = []
    sell_list = []
    flag = False

    for i in range(0,len(data)):
        if data['SMA_20'][i] > data['EMA_20'][i]:
            if flag != 1:
                buy_list.append(data['Close'][i])
                sell_list.append(np.nan)
                flag = 1
            else:
                buy_list.append(np.nan)
                sell_list.append(np.nan)
        elif data['SMA_20'][i] < data['EMA_20'][i]:
            if flag != 0:
                buy_list.append(np.nan)
                sell_list.append(data['Close'][i])
                flag = 0
            else:
                buy_list.append(np.nan)
                sell_list.append(np.nan)
        else:
            buy_list.append(np.nan)
            sell_list.append(np.nan)

    return (buy_list, sell_list)

# Implement the strategy
ticker_data['Buy_Signal_Price'], ticker_data['Sell_Signal_Price'] = implement_strategy(ticker_data)

# Visually Show The Stock buy and sell signals
plt.figure(figsize=(12.2,4.5))
plt.plot(ticker_data['Close'], label='Close Price', color='blue', alpha=0.35)
plt.plot(ticker_data['SMA_20'], label='SMA_20', color='red',alpha=0.35)
plt.plot(ticker_data['EMA_20'], label='EMA_20', color='green', alpha=0.35)
plt.scatter(ticker_data.index, ticker_data['Buy_Signal_Price'], color='green', marker='^', alpha=1)
plt.scatter(ticker_data.index, ticker_data['Sell_Signal_Price'], color='red', marker='v', alpha=1)
plt.title('Stock Buy / Sell Signals')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()
```

This is a simple moving average crossover strategy where we buy the stock when the short-term moving average crosses above the long-term moving average, and sell the stock when the short-term moving average crosses below the long-term moving average.

Please note that this is a very basic strategy and in real trading scenarios, you would need to consider transaction costs, risk management, portfolio optimization, etc.