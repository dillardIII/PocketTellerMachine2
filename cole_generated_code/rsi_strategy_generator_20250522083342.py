The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate an RSI strategy:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

yf.pdr_override()

def calculate_RSI(data, window):
    delta = data.diff()
    delta = delta[1:]
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    average_gain = up.rolling(window).mean()
    average_loss = abs(down.rolling(window).mean())
    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def implement_RSI_strategy(data, window):
    data['RSI'] = calculate_RSI(data['Adj Close'], window)
    data['Buy_Signal'] = np.where((data['RSI'] < 30), 1, 0) 
    data['Sell_Signal'] = np.where((data['RSI'] > 70), -1, 0) 
    return data

ticker = 'AAPL'
start_date = datetime(2020, 1, 1)
end_date = datetime(2021, 12, 31)

data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
window = 14
data = implement_RSI_strategy(data, window)

data[['Adj Close', 'RSI']].plot(subplots=True, figsize=(10, 8))
plt.show()
```

In this code, we first calculate the RSI for a given window of days. Then, we generate buy signals when the RSI is less than 30 (indicating that the stock is oversold) and sell signals when the RSI is greater than 70 (indicating that the stock is overbought). We then plot the adjusted close price and the RSI to visualize our strategy. This code uses the yfinance library to download historical stock data from Yahoo Finance.