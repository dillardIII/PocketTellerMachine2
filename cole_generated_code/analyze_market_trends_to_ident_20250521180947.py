In this program, we are going to use the yfinance library to fetch stock market data of a particular company. We will analyze its Close prices using Simple Moving Average (SMA) strategy. 

One of the most popular and simple strategies is called the Moving Average Crossover. This will be our trading signal. If the short-term moving average crosses above the long-term moving average, it may be a good time to buy. If it crosses below, it may be a good time to sell.

```python
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Fetch the data
data = yf.download('AAPL', start='2021-01-01', end='2022-12-31')

# Calculate Simple Moving Average with 20 days window
data['SMA_20'] = data['Close'].rolling(window=20).mean()

# Calculate Simple Moving Average with 50 days window
data['SMA_50'] = data['Close'].rolling(window=50).mean()

data = data.dropna()

# Create a function to signal when to buy and sell
def create_signal(data):
    buy_signal = []
    sell_signal = []
    
    for i in range(len(data)):
        if data['SMA_20'].iloc[i] > data['SMA_50'].iloc[i]:
            if len(buy_signal) > 1:
                if sell_signal[-1] > buy_signal[-1]:
                    buy_signal.append(data['Close'].iloc[i])
                    sell_signal.append(float('nan'))
                else:
                    buy_signal.append(float('nan'))
                    sell_signal.append(float('nan'))
            else:
                buy_signal.append(data['Close'].iloc[i])
                sell_signal.append(float('nan'))
        elif data['SMA_20'].iloc[i] < data['SMA_50'].iloc[i]:
            if len(sell_signal) > 1:
                if buy_signal[-1] > sell_signal[-1]:
                    buy_signal.append(float('nan'))
                    sell_signal.append(data['Close'].iloc[i])
                else:
                    buy_signal.append(float('nan'))
                    sell_signal.append(float('nan'))
            else:
                buy_signal.append(float('nan'))
                sell_signal.append(data['Close'].iloc[i])
        else:
            buy_signal.append(float('nan'))
            sell_signal.append(float('nan'))

    return buy_signal, sell_signal

data['Buy_Signal_Price'] = create_signal(data)[0]
data['Sell_Signal_Price'] = create_signal(data)[1]

# Plot the data
plt.figure(figsize=(12.2, 6.4))
plt.plot(data['Close'], label='Close Price', color='blue', alpha=0.35)
plt.plot(data['SMA_20'], label='SMA_20', color='green', alpha=0.35)
plt.plot(data['SMA_50'], label='SMA_50', color='red', alpha=0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], color='green', label='Buy Signal', marker='^', alpha=1)
plt.scatter(data.index, data['Sell_Signal_Price'], color='red', label='Sell Signal', marker='v', alpha=1)
plt.title('Apple Stock Price History Buy and Sell Signals')
plt.xlabel('Jan 01, 2021 - Dec 31, 2022')
plt.ylabel('Close Price USD($)')
plt.legend(loc='upper left')
plt.show()
```

In this script, first, we fetch the data from yahoo finance using the `download` function. Then we use the pandas `rolling` function to calculate the simple moving averages (SMA) using windows of 20 and 50 days. We then create a function to generate buy and sell signals based on the SMA crossover strategy. If the short term SMA is above the long term SMA, we generate a buy signal and vice versa.

Remember, this is a simple analysis and real trading systems will use more complex analyses and strategies. Also, past performance is not indicative of future results. Always do your own research before making trading decisions.