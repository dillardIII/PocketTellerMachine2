The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code that generates an RSI strategy:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr

# Download historical data as dataframe
yf.pdr_override()
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2021-12-31")

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

# Calculate RSI
df['RSI'] = calculate_RSI(df['Adj Close'], 14)

# Create signals
df['Buy_Signal'] = np.where((df['RSI'] < 30), 1, 0)
df['Sell_Signal'] = np.where((df['RSI'] > 70), -1, 0)

# Print dataframe
print(df)
```

In this code, we first download the historical data of a stock (in this case, AAPL) using the `yfinance` library. Then, we calculate the RSI for the 'Adj Close' price with a window of 14 days. The RSI is calculated by first finding the average gain and average loss over the window period, then calculating the relative strength (RS) as the ratio of average gain to average loss, and finally calculating the RSI.

We then create two new columns in the dataframe: 'Buy_Signal' and 'Sell_Signal'. If the RSI is less than 30, it indicates that the stock is oversold and it might be a good time to buy, so we set 'Buy_Signal' to 1. If the RSI is more than 70, it indicates that the stock is overbought and it might be a good time to sell, so we set 'Sell_Signal' to -1.