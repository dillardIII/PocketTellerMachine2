RSI (Relative Strength Index) is a popular technical indicator used in trading to identify overbought or oversold conditions in the market. Here is a simple Python code to generate a basic RSI strategy:

```python
# Import necessary libraries
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Define the RSI function
def RSI(data, period=14, column='Close'):
    delta = data[column].diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    gain = up.rolling(period).mean()
    loss = abs(down.rolling(period).mean())
    RS = gain / loss
    return 100 - (100 / (1 + RS))

# Fetch data
data = pdr.get_data_yahoo('AAPL', '2020-01-01', '2022-01-01')

# Calculate RSI
data['RSI'] = RSI(data)

# Create signals
data['Buy_Signal'] = np.where((data['RSI'] < 30), 1, 0) # Oversold condition
data['Sell_Signal'] = np.where((data['RSI'] > 70), -1, 0) # Overbought condition

print(data)
```

This script fetches historical data for Apple Inc. (AAPL) from Yahoo Finance, calculates the RSI, and generates trading signals based on the RSI value. A buy signal is generated when the RSI drops below 30 (oversold condition), and a sell signal is generated when the RSI rises above 70 (overbought condition).

Please note that this is a very basic strategy and should not be used for live trading without further refinement and testing. Always consult with a financial advisor before making trading decisions.