from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate an RSI strategy:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

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

def implement_RSI_strategy(data, window=14):
    close = data['Close']
    rsi = calculate_RSI(close, window)
    buy_signal, sell_signal = [], []

    for i in range(len(rsi)):
        if rsi[i] < 30:  # oversold condition
            buy_signal.append(close[i])
            sell_signal.append(np.nan)
        elif rsi[i] > 70:  # overbought condition
            sell_signal.append(close[i])
            buy_signal.append(np.nan)
        else:
            buy_signal.append(np.nan)
            sell_signal.append(np.nan)

    return buy_signal, sell_signal

# Download historical data
ticker = 'AAPL'
start_date = datetime(2020, 1, 1)
end_date = datetime(2021, 12, 31)
data = yf.download(ticker, start=start_date, end=end_date)

buy_signal, sell_signal = implement_RSI_strategy(data)

# Plotting
plt.figure(figsize=(12,5))
plt.plot(data.index, data['Close'], label='Price', color='blue', alpha=0.35)
plt.plot(data.index, buy_signal, label='Buy Signal', color='green', marker='^', alpha=1)
plt.plot(data.index, sell_signal, label='Sell Signal', color='red', marker='v', alpha=1)
plt.title('RSI Strategy - ' + ticker)
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.show()
```

This code downloads historical data for a given ticker using the `yfinance` library, calculates the RSI, and generates buy/sell signals based on the RSI. The buy/sell signals are then plotted on a graph. The RSI window is set to 14 days by default, but can be adjusted. The buy signal is generated when the RSI falls below 30 (oversold condition), and the sell signal is generated when the RSI rises above 70 (overbought condition).