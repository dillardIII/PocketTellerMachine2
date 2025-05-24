Sure, I can provide a basic example of a Python code for a simple trading strategy. In this example, we will use a simple moving average crossover strategy. 

Please note that this is a very simple example and real trading strategies involve much more complex analysis and risk management.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the ticker list
tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP']

# Fetch the data
data = pdr.get_data_yahoo(tickers_list, start="2017-01-01", end="2021-12-31")['Adj Close']

# Print first 5 rows of the data
print(data.head())

# Calculate the 20 days moving average
data['20_SMA'] = data['AAPL'].rolling(window=20).mean()

# Calculate the 50 days moving average
data['50_SMA'] = data['AAPL'].rolling(window=50).mean()

# Create a function to signal when to buy and sell an asset
def buy_sell(signal):
    Buy = []
    Sell = []
    flag = -1

    for i in range(0, len(signal)):
        if signal['20_SMA'][i] > signal['50_SMA'][i]:
            Sell.append(np.nan)
            if flag != 1:
                Buy.append(signal['AAPL'][i])
                flag = 1
            else:
                Buy.append(np.nan)
        elif signal['20_SMA'][i] < signal['50_SMA'][i]:
            Buy.append(np.nan)
            if flag != 0:
                Sell.append(signal['AAPL'][i])
                flag = 0
            else:
                Sell.append(np.nan)
        else:
            Buy.append(np.nan)
            Sell.append(np.nan)

    return (Buy, Sell)

# Create buy and sell column
data['Buy_Signal_Price'] = buy_sell(data)[0]
data['Sell_Signal_Price'] = buy_sell(data)[1]

# Print the data
print(data)
```

This script fetches the historical price data of several stocks using Yahoo Finance, calculates the 20-day and 50-day moving averages for Apple's stock, and generates buy/sell signals based on a simple moving average crossover strategy. When the 20-day moving average crosses above the 50-day moving average, it generates a buy signal, and when it crosses below, it generates a sell signal. 

Please note that this is a very basic strategy and should not be used for actual trading without further enhancements.