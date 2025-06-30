from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market.

Here is a simple Python code to generate a trading strategy based on RSI:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf

def calculate_RSI(data, window):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    average_gain = up.rolling(window=window).mean()
    average_loss = abs(down.rolling(window=window).mean())
    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def implement_RSI_strategy(data, window):
    data['RSI'] = calculate_RSI(data['Adj Close'], window)
    data['Buy_Signal'] = np.where((data['RSI'] < 30), 1, 0) 
    data['Sell_Signal'] = np.where((data['RSI'] > 70), -1, 0) 
    return data

start_date = datetime(2020,1,1)
end_date = datetime.now()

df = yf.download('AAPL', start=start_date, end=end_date)
df = implement_RSI_strategy(df, 14)

plt.figure(figsize=(12,5))
plt.plot(df['Adj Close'], label='Price', color='blue')
plt.title('RSI Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()

plt.figure(figsize=(12,5))
plt.title('RSI')
plt.plot(df['RSI'], label='RSI', color='orange')
plt.axhline(0, linestyle='--', alpha=0.5, color='black')
plt.axhline(10, linestyle='--', alpha=0.5, color='red')
plt.axhline(20, linestyle='--', alpha=0.5, color='orange')
plt.axhline(30, linestyle='--', alpha=0.5, color='green')
plt.axhline(70, linestyle='--', alpha=0.5, color='green')
plt.axhline(80, linestyle='--', alpha=0.5, color='orange')
plt.axhline(90, linestyle='--', alpha=0.5, color='red')
plt.axhline(100, linestyle='--', alpha=0.5, color='black')
plt.xlabel('Date')
plt.ylabel('RSI')
plt.show()
```

This code first calculates the RSI for a given window of days. Then it generates buy signals when the RSI is below 30 (oversold condition) and sell signals when the RSI is above 70 (overbought condition). It uses the 'yfinance' library to download historical stock data from Yahoo Finance. The code then plots the price and RSI over time.

Please note that this is a simple strategy and may not be profitable in real trading. Always backtest your strategies before live trading.