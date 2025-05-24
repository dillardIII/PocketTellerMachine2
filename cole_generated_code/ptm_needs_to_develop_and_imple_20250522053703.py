Sure, I can provide a simple example of a trading strategy using Python. This strategy is a basic Moving Average Crossover strategy. 

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

# Download historical data as dataframe
yf.pdr_override()
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2021-12-31")

# Calculate the short-term simple moving average
short_sma= 50
df['ShortSMA'] = df['Close'].rolling(window=short_sma).mean()

# Calculate the long-term simple moving average
long_sma = 200
df['LongSMA'] = df['Close'].rolling(window=long_sma).mean()

# Create a function to signal when to buy and sell an asset
def buy_sell(signal):
    Buy = []
    Sell = []
    flag = -1

    for i in range(0,len(signal)):
        if signal['ShortSMA'][i] > signal['LongSMA'][i]:
            Sell.append(np.nan)
            if flag != 1:
                Buy.append(signal['Close'][i])
                flag = 1
            else:
                Buy.append(np.nan)
        elif signal['ShortSMA'][i] < signal['LongSMA'][i]:
            Buy.append(np.nan)
            if flag != 0:
                Sell.append(signal['Close'][i])
                flag = 0
            else:
                Sell.append(np.nan)
        else:
            Buy.append(np.nan)
            Sell.append(np.nan)
            
    return (Buy, Sell)

# Create buy and sell column
df['Buy_Signal_Price'] = buy_sell(df)[0]
df['Sell_Signal_Price'] = buy_sell(df)[1]

# Visually show the stock buy and sell signals
plt.figure(figsize=(12.2, 4.5))
plt.plot(df['Close'], label='Close Price', color='blue', alpha=0.35)
plt.plot(df['ShortSMA'], label='ShortSMA', color='red', alpha=0.35)
plt.plot(df['LongSMA'], label='LongSMA', color='green', alpha=0.35)
plt.scatter(df.index, df['Buy_Signal_Price'], color='green', marker='^', alpha=1)
plt.scatter(df.index, df['Sell_Signal_Price'], color='red', marker='v', alpha=1)
plt.title('Apple Close Price Buy & Sell Signals')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()
```

This script will fetch the historical data for Apple Inc. (AAPL) for the years 2020 and 2021. It will then calculate the short-term (50 days) and long-term (200 days) simple moving averages. When the short-term average crosses above the long-term average, it generates a buy signal, and when it crosses below, it generates a sell signal.

Please note that this is a very basic trading strategy and is used for illustrative purposes only. In real-world scenarios, trading strategies can get very complex and also take into account other factors like trading volumes, other technical indicators, fundamental analysis, etc.