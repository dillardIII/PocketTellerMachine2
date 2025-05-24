To develop and apply a trading strategy, we need to use some financial libraries in Python such as pandas, numpy, and yfinance. Here is a simple example of a trading strategy using Moving Average Crossover, which is a common trading strategy.

```python
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for required stocks
ticker = "AAPL"
ticker_data = yf.download(ticker,'2020-1-1','2021-12-31')

# Calculate Simple Moving Average with 20 days window
sma20 = ticker_data['Close'].rolling(window=20).mean()

# Calculate Simple Moving Average with 50 days window
sma50 = ticker_data['Close'].rolling(window=50).mean()

ticker_data['sma20'] = sma20
ticker_data['sma50'] = sma50

# Create a function to signal when to buy and sell an asset
def generate_signals(data):
    buy_signal = []
    sell_signal = []
    flag = -1

    for i in range(len(data)):
        if data['sma20'][i] > data['sma50'][i]:
            if flag != 1:
                buy_signal.append(data['Close'][i])
                sell_signal.append(np.nan)
                flag = 1
            else:
                buy_signal.append(np.nan)
                sell_signal.append(np.nan)
        elif data['sma20'][i] < data['sma50'][i]:
            if flag != 0:
                sell_signal.append(data['Close'][i])
                buy_signal.append(np.nan)
                flag = 0
            else:
                buy_signal.append(np.nan)
                sell_signal.append(np.nan)
        else:
            buy_signal.append(np.nan)
            sell_signal.append(np.nan)
            
    return buy_signal, sell_signal

# Create buy and sell column
ticker_data['Buy_Signal_Price'] = generate_signals(ticker_data)[0]
ticker_data['Sell_Signal_Price'] = generate_signals(ticker_data)[1]

# Plotting the stock price, short-term and long-term moving averages and Buy-Sell signals
plt.figure(figsize=(12,5))
plt.plot(ticker_data['Close'], label='Stock Price', color='blue',alpha=0.35)
plt.plot(sma20, label='Short-term average (20 days)', color='red',alpha=0.35)
plt.plot(sma50, label='Long-term average (50 days)', color='green',alpha=0.35)
plt.scatter(ticker_data.index, ticker_data['Buy_Signal_Price'], color = 'green', label='Buy Signal', marker = '^', alpha = 1)
plt.scatter(ticker_data.index, ticker_data['Sell_Signal_Price'], color = 'red', label='Sell Signal', marker = 'v', alpha = 1)
plt.title('Apple Stock Price - Moving Average Crossover Trading Signals')
plt.xlabel('Date')
plt.ylabel('USD Price ($)')
plt.legend(loc='upper left')
plt.grid()
plt.show()
```

This script will download the historical data of Apple's stock price, calculate the 20-day and 50-day moving averages, generate buy and sell signals based on the crossover of these two averages, and plot the stock price, moving averages, and trading signals.

Please note that this is a simple trading strategy and might not be profitable in real trading. Always backtest your strategy before live trading.