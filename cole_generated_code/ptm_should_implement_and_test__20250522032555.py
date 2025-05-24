Sure, here is a simple Python code implementing a basic Moving Average Crossover trading strategy using pandas library. This strategy generates a buy signal when the short-term moving average crosses above the long-term moving average, and a sell signal when the short-term moving average crosses below the long-term moving average.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = pdr.get_data_yahoo(tickerSymbol, start='2010-1-1', end='2020-12-31')

# Calculate the short-term simple moving average (SMA)
short_rolling = tickerData.rolling(window=20).mean()

# Calculate the long-term SMA
long_rolling = tickerData.rolling(window=100).mean()

# Create signals
signals = pd.DataFrame(index=tickerData.index)
signals['signal'] = 0.0
signals['short_mavg'] = short_rolling['Close']
signals['long_mavg'] = long_rolling['Close']

# Generate signals
signals['signal'][short_rolling['Close'] > long_rolling['Close']] = 1.0
signals['signal'][short_rolling['Close'] < long_rolling['Close']] = -1.0

# Plot
fig, ax = plt.subplots(figsize=(16,9))

ax.plot(tickerData.index, tickerData['Close'], label='Price')
ax.plot(short_rolling.index, short_rolling['Close'], label='20-days SMA')
ax.plot(long_rolling.index, long_rolling['Close'], label='100-days SMA')

ax.legend(loc='best')
ax.set_ylabel('Price in $')
plt.show()
```

Please note that this is a very basic trading strategy and should not be used for real trading without further improvements and adjustments. It's always recommended to backtest any strategy thoroughly before live trading. Also, this code assumes that you have the pandas_datareader library installed and a stable internet connection to fetch the data.