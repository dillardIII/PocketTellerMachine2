from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple example of a Python code that could be used to develop and test a new trading strategy. This strategy is based on moving averages, a common indicator used in trading. 

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf

# Use Yahoo Finance to get historical market data
yf.pdr_override()

# Input the stock you are interested in
stock = 'AAPL'
df = pdr.get_data_yahoo(stock, start="2020-01-01", end="2022-12-31")

# Calculate the short-term simple moving average
short_sma = 20
df['ShortSMA'] = df['Close'].rolling(window=short_sma).mean()

# Calculate the long-term simple moving average
long_sma = 50
df['LongSMA'] = df['Close'].rolling(window=long_sma).mean()

# Create a function to signal when to buy and sell the asset/stock
def buy_sell(signal):
  Buy = []
  Sell = []
  flag = -1

  for i in range(len(signal)):
    if signal['ShortSMA'][i] > signal['LongSMA'][i]:
      if flag != 1:
        Buy.append(signal['Close'][i])
        Sell.append(np.nan)
        flag = 1
      else:
        Buy.append(np.nan)
        Sell.append(np.nan)
    elif signal['ShortSMA'][i] < signal['LongSMA'][i]:
      if flag != 0:
        Sell.append(signal['Close'][i])
        Buy.append(np.nan)
        flag = 0
      else:
        Buy.append(np.nan)
        Sell.append(np.nan)
    else:
      Buy.append(np.nan)
      Sell.append(np.nan)
        
  return (Buy, Sell)

# Implement the function
df['Buy_Signal_Price'] = buy_sell(df)[0]
df['Sell_Signal_Price'] = buy_sell(df)[1]

# Print the DataFrame
print(df)
```

This code will print a DataFrame with the stock's closing price, short-term moving average, long-term moving average, and the buy and sell signals.

Please note that this is a very basic trading strategy and should not be used for actual trading without further improvements and considerations of other factors. Always do thorough research and consider seeking advice from financial advisors before making any trading decisions.