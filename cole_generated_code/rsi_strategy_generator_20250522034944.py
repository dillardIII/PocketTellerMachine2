The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a RSI Strategy.

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
from pyti.relative_strength_index import relative_strength_index as rsi

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end=datetime.today().strftime('%Y-%m-%d'))

# Calculate RSI
tickerDf['RSI'] = rsi(tickerDf['Close'].values, 14)

# Define a signal flag
tickerDf['Signal'] = 0.0
tickerDf['Signal'][tickerDf['RSI'] < 30] = 1.0
tickerDf['Signal'][tickerDf['RSI'] > 70] = -1.0

# Generate trading orders
tickerDf['Order'] = tickerDf['Signal'].diff()

# Print data
print(tickerDf)
```

In this code, we first download the historical price data for a given ticker symbol using the `yfinance` library. We then calculate the 14-day RSI for the closing prices. A signal flag is set to 1.0 when the RSI is below 30 (indicating an oversold condition and a potential buying opportunity) and -1.0 when the RSI is above 70 (indicating an overbought condition and a potential selling opportunity). Trading orders are generated when the signal changes.

Please note that this is a very simplistic trading strategy and should not be used for actual trading without further refinement and testing.