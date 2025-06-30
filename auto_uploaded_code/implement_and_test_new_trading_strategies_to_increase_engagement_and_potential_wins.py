from ghost_env import INFURA_KEY, VAULT_ADDRESS
Please note that writing a full trading algorithm needs a deep understanding of stocks, trading and also fintech and this would require a lot of complex code that includes a variety of algorithms to predict the stock prices. However, I can give you a simple example of a trading strategy implemented in Python. This strategy is called the Moving Average Crossover Strategy.

The strategy will have two moving averages, a fast moving average(10 days) and a slow moving average(20 days). Here, when the fast moving average crosses above the slow moving average, it means the stock price is increasing and it's time to buy. Conversely, when the fast moving average falls below the slow moving average, it's time to sell.

Please replace `stock_name` with the appropriate stock symbol that you want to track. Also, you need to install the `pandas_datareader`, `numpy` and `matplotlib.pyplot` packages to run this script.

```python
import pandas_datareader as web
import matplotlib.pyplot as plt
import numpy as np

# Fetching historical stock data
stock_data = web.get_data_yahoo('stock_name', start='2020-01-01', end='2021-12-31')

# Calculating the moving averages
stock_data['Fast_MA'] = stock_data['Close'].rolling(window=10).mean()
stock_data['Slow_MA'] = stock_data['Close'].rolling(window=20).mean()

# Creating a function to signal when to buy and when to sell
def get_signals(data):
    buy_signal = []
    sell_signal = []
    for i in range(len(data)):
        if data['Fast_MA'].iloc[i] > data['Slow_MA'].iloc[i]:
            if i-1 not in buy_signal and i-2 not in buy_signal and i-3 not in buy_signal:
                buy_signal.append(i)
        elif data['Fast_MA'].iloc[i] < data['Slow_MA'].iloc[i]:
            if i-1 not in sell_signal and i-2 not in sell_signal and i-3 not in sell_signal:
                sell_signal.append(i)
    return buy_signal, sell_signal
 
 # Getting the signals
buy, sell = get_signals(stock_data)

# Plotting the stock price and signals
plt.figure(figsize=(12,5))
plt.plot(stock_data['Close'], label='Stock Close Price', alpha=0.3)
plt.plot(stock_data['Fast_MA'], label='Fast MA', linestyle='--', alpha=0.5)
plt.plot(stock_data['Slow_MA'], label='Slow MA', linestyle='--', alpha=0.5)
plt.scatter(stock_data.iloc[buy].index, stock_data.iloc[buy]['Close'], color='green', label='Buy Signal', marker='^', alpha=1)
plt.scatter(stock_data.iloc[sell].index, stock_data.iloc[sell]['Close'], color='red', label='Sell Signal', marker='v', alpha=1)
plt.title('Stock_Name Close Price, Buy & Sell Signals')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend(loc='upper left')
plt.show()
```

This is a simple example, please do ensure to build over it according to specific requirements and financial underpinnings.
