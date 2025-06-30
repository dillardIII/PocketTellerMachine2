from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple Python code for a trading strategy using Moving Average Crossover. This strategy is based on two moving averages, one short and one long. When the short moving average crosses above the long moving average, it's a signal to buy. When it crosses below, it's a signal to sell.

Please note that this is a very basic strategy and may not be suitable for real trading. You should consider factors like transaction costs, slippage, and risk management.

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

# Generate trading signals (1 for buy, -1 for sell)
signals['signal'][short_rolling['Close'] > long_rolling['Close']] = 1.0
signals['signal'][short_rolling['Close'] < long_rolling['Close']] = -1.0

# Plot the data
fig, ax = plt.subplots(figsize=(16,9))
ax.plot(tickerData.index, tickerData['Close'], label='Price')
ax.plot(short_rolling.index, short_rolling['Close'], label='20-days SMA')
ax.plot(long_rolling.index, long_rolling['Close'], label='100-days SMA')

ax.legend(loc='best')
ax.set_ylabel('Price in $')
plt.show()
```

This code will plot the price of the stock along with the short and long moving averages. When the short moving average crosses above the long moving average, it's a signal to buy. When it crosses below, it's a signal to sell.

Please note that you will need to install the `pandas_datareader` package to fetch the stock data. You can install it using pip:

```bash
pip install pandas_datareader
```

Also, this code uses Yahoo Finance to fetch the stock data. If you want to use another source, you will need to modify the code accordingly.