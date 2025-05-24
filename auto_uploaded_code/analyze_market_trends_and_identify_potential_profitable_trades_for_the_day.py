To analyze market trends and identify potential profitable trades, we need to use some sort of financial data. Here, we will use Yahoo Finance data with the help of the `yfinance` library in Python. 

Please note that this is a simple example and real trading systems are much more complex and take into account many more factors.

```python
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Download historical data for desired ticker symbol 
def download_data(stock, start, end):
    data = {}
    ticker = yf.download(stock, start, end)
    data['Price'] = ticker['Adj Close']
    return pd.DataFrame(data)

# Calculate simple moving average
def SMA(data, window):
    return data['Price'].rolling(window = window).mean()

# Calculate Bollinger Bands
def BB(data, window):
    data['SMA'] = data['Price'].rolling(window = window).mean()
    data['BB_up'] = data['SMA'] + 2*data['Price'].rolling(window = window).std()
    data['BB_down'] = data['SMA'] - 2*data['Price'].rolling(window = window).std()
    return data

# Implement the trading strategy
def implement_BB_strategy(data, window):
    data = BB(data, window)
    buy_price = []
    sell_price = []
    BB_signal = []
    signal = 0

    for i in range(len(data)):
        if data['Price'][i] < data['BB_down'][i]:
            if signal != 1:
                buy_price.append(data['Price'][i])
                sell_price.append(np.nan)
                signal = 1
                BB_signal.append(signal)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                BB_signal.append(0)
        elif data['Price'][i] > data['BB_up'][i]:
            if signal != -1:
                sell_price.append(data['Price'][i])
                buy_price.append(np.nan)
                signal = -1
                BB_signal.append(signal)
            else:
                buy_price.append(np.nan)
                sell_price.append(np.nan)
                BB_signal.append(0)
        else:
            buy_price.append(np.nan)
            sell_price.append(np.nan)
            BB_signal.append(0)
            
    return buy_price, sell_price, BB_signal

# Define the ticker list
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB']

# Fetch the data
start_date = '2020-01-01'
end_date = '2021-12-31'
for ticker in tickers:
    data = download_data(ticker, start_date, end_date)
    buy_price, sell_price, signals = implement_BB_strategy(data, 20)

    # Plot the data
    plt.figure(figsize=(12,5))
    plt.plot(data['Price'], label='Close Price', color='blue', alpha=0.35)
    plt.plot(data['BB_up'], label='Upper Bollinger Band', color='green')
    plt.plot(data['BB_down'], label='Lower Bollinger Band', color='red')
    plt.scatter(data.index, buy_price, color='green', marker='^', alpha=1)
    plt.scatter(data.index, sell_price, color='red', marker='v', alpha=1)
    plt.title(ticker + ' Bollinger Band Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()
```

This script downloads the historical data for the specified ticker symbols, calculates the Bollinger Bands for each, and