To analyze market trends and patterns, we can use Python libraries like pandas for data manipulation, numpy for numerical computations, and matplotlib for data visualization. We can also use yfinance to download historical market data from Yahoo Finance.

Here's a simple example of how you can analyze market trends for a specific stock (e.g., Apple Inc. - AAPL):

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for desired ticker symbol 
data = yf.download('AAPL','2016-01-01','2021-12-31')

# Calculate the simple moving average
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()

# Create a function to signal when to buy and sell an asset
def buy_sell(data):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1

    for i in range(len(data)):
        if data['SMA_50'][i] > data['SMA_200'][i]:
            if flag != 1:
                sigPriceBuy.append(data['Close'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data['SMA_50'][i] < data['SMA_200'][i]:
            if flag != 0:
                sigPriceSell.append(data['Close'][i])
                sigPriceBuy.append(np.nan)
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)

    return (sigPriceBuy, sigPriceSell)

# Store the buy and sell data into a variable
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

# Plot the data
plt.figure(figsize=(12.5, 4.5))
plt.plot(data['Close'], label='Close Price', alpha=0.35)
plt.plot(data['SMA_50'], label='SMA_50', alpha=0.35)
plt.plot(data['SMA_200'], label='SMA_200', alpha=0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], color='green', label='Buy Signal', marker='^', alpha=1)
plt.scatter(data.index, data['Sell_Signal_Price'], color='red', label='Sell Signal', marker='v', alpha=1)
plt.title('Apple Inc. Close Price History with Buy & Sell signals')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()
```

This script will download the historical data for Apple Inc. from Yahoo Finance, calculate the 50-day and 200-day simple moving averages, generate buy and sell signals based on these averages, and plot the closing price history along with the buy and sell signals.

Please note that this is a very basic form of market trend analysis and should not be used as the sole decision-making tool for trading. It's always recommended to use additional indicators and strategies to confirm the signals.