The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market.

Here is a simple Python code to generate a RSI strategy:

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
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    average_gain = up.rolling(window=window).mean()
    average_loss = abs(down.rolling(window=window).mean())

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Calculate RSI
df['RSI'] = calculate_RSI(df['Adj Close'], 14)

# Create signals
df['Buy_Signal'] = np.where((df['RSI'] < 30), 1, 0) # oversold condition
df['Sell_Signal'] = np.where((df['RSI'] > 70), -1, 0) # overbought condition

print(df)
```

In this code, we are downloading historical data for Apple Inc. (AAPL) from Yahoo Finance. We calculate the RSI based on the 'Adj Close' prices with a window of 14 days (which is the most commonly used period). 

Then we generate trading signals based on the RSI. If the RSI is below 30, it indicates an oversold condition and we generate a buy signal. If the RSI is above 70, it indicates an overbought condition and we generate a sell signal. 

Please note that this is a very simplistic strategy and should not be used for actual trading without further refinement and testing.