The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought and oversold conditions in a market.

Here is a simple Python code to generate a RSI strategy:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr
from datetime import datetime

# Download historical data for required stocks
ticker = "AAPL"
yf.pdr_override()
start_date = datetime(2020, 1, 1)
end_date = datetime(2021, 1, 1)
df = pdr.get_data_yahoo(ticker, start_date, end_date)

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

df['RSI'] = calculate_RSI(df['Close'], 14)

# Create a function to signal when to buy and sell an asset
def generate_signals(data):
    buy_signal, sell_signal = [], []

    for i in range(len(data['RSI'])):
        if data['RSI'][i] > 70:  # if RSI > 70, sell signal
            buy_signal.append(np.nan)
            sell_signal.append(data['Close'][i])
        elif data['RSI'][i] < 30:  # if RSI < 30, buy signal
            buy_signal.append(data['Close'][i])
            sell_signal.append(np.nan)
        else:
            buy_signal.append(np.nan)
            sell_signal.append(np.nan)

    return buy_signal, sell_signal

df['Buy_Signal_Price'], df['Sell_Signal_Price'] = generate_signals(df)

print(df)
```

This code calculates the RSI for the given ticker symbol (in this case, AAPL) and generates buy and sell signals based on the RSI. If the RSI is above 70, it generates a sell signal, and if it is below 30, it generates a buy signal.