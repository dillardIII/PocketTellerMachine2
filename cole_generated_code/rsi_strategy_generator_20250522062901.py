The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate an RSI strategy:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
from pandas_datareader import data as pdr

# Download historical data as dataframe
yf.pdr_override()
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end=datetime.now())

def calculate_RSI(df, period=14):
    delta = df['Close'].diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    avg_gain = up.rolling(window=period).mean()
    avg_loss = abs(down.rolling(window=period).mean())
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    df['RSI'] = rsi
    return df

# Calculate RSI
df = calculate_RSI(df)

# Create a column in the DataFrame showing "TRUE" if sell entry signal is given and "FALSE" otherwise. 
# A sell is initiated when the RSI crosses above 70
df['Sell Entry'] = ((df['RSI'] < 70) & (df['RSI'].shift(1) > 70))

# Create a column in the DataFrame showing "TRUE" if buy entry signal is given and "FALSE" otherwise. 
# A buy is initiated when the RSI crosses below 30
df['Buy Entry'] = ((df['RSI'] > 30) & (df['RSI'].shift(1) < 30))

print(df)
```

This script downloads historical price data for Apple Inc. (AAPL) from Yahoo Finance, calculates the RSI, and then generates buy and sell signals based on the RSI. A sell signal is generated when the RSI crosses above 70, indicating overbought conditions, and a buy signal is generated when the RSI crosses below 30, indicating oversold conditions.