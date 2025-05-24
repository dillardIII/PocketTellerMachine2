Sure, I can provide a simple example of a trading strategy using Python. This example will be a basic moving average crossover strategy. 

Please note that this is a simplified example and real-world trading strategies can be much more complex and require extensive knowledge of financial markets.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf

# Download historical data as dataframe
yf.pdr_override()
df = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2021-12-31")

# Calculate the short-window simple moving average
short_rolling = df.rolling(window=20).mean()

# Calculate the long-window simple moving average
long_rolling = df.rolling(window=100).mean()

# Create signals
signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0
signals['short_mavg'] = short_rolling['Close']
signals['long_mavg'] = long_rolling['Close']

# Generate trading orders
signals['signal'][short_rolling['Close'] > long_rolling['Close']] = 1.0
signals['orders'] = signals['signal'].diff()

# Print `signals`
print(signals)
```

In this code, we first download historical data for Apple Inc. (AAPL) using the Yahoo Finance API. We then calculate the short-window (20 days) and long-window (100 days) simple moving averages for the closing prices. 

We generate a trading signal whenever the short moving average crosses the long moving average. A buy signal (1.0) is generated when the short moving average is above the long moving average, and a sell signal (-1.0) is generated when the short moving average is below the long moving average.

Please note that this is a very basic trading strategy and should not be used for actual trading without further improvements and testing.