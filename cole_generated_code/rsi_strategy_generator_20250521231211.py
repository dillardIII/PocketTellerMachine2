The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a trading strategy based on the RSI.

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
from pandas_datareader import data as pdr

# Download historical data as dataframe
yf.pdr_override()
stock = input("Enter a stock ticker: ")
df = pdr.get_data_yahoo(stock, start="2020-01-01", end=datetime.now())

# Calculate the RSI
delta = df['Adj Close'].diff()
up = delta.clip(lower=0)
down = -1*delta.clip(upper=0)
ema_up = up.ewm(com=13, adjust=False).mean()
ema_down = down.ewm(com=13, adjust=False).mean()
rs = ema_up/ema_down
df['RSI'] = 100 - (100/(1 + rs))

# Create a function to signal when to buy and sell an asset
def RSI_Strategy(df):
    Buy, Sell = [], []
    flag = -1
    for i in range(0,len(df)):
        if df['RSI'][i] < 30:
            if flag != 1:
                Buy.append(df['Adj Close'][i])
                Sell.append(np.nan)
                flag = 1
            else:
                Buy.append(np.nan)
                Sell.append(np.nan)
        elif df['RSI'][i] > 70:
            if flag != 0:
                Buy.append(np.nan)
                Sell.append(df['Adj Close'][i])
                flag = 0
            else:
                Buy.append(np.nan)
                Sell.append(np.nan)
        else:
            Buy.append(np.nan)
            Sell.append(np.nan)
    return (Buy, Sell)

# Implement the function
df['Buy_Signal_Price'], df['Sell_Signal_Price'] = RSI_Strategy(df)

# Print the dataframe
print(df)
```

This script will download historical data for a specific stock ticker, calculate the RSI, and generate buy/sell signals based on the RSI. The buy signal is generated when the RSI drops below 30 (oversold condition), and the sell signal is generated when the RSI rises above 70 (overbought condition).