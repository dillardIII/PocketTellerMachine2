The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a basic RSI strategy.

```python
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

# Download historical data as dataframe
yf.pdr_override()
stock = 'AAPL'
df = pdr.get_data_yahoo(stock, start="2020-01-01", end=datetime.now())

# Calculate the RSI
delta = df['Adj Close'].diff()
up = delta.clip(lower=0)
down = -1*delta.clip(upper=0)
ema_up = up.ewm(com=13, adjust=False).mean()
ema_down = down.ewm(com=13, adjust=False).mean()
rs = ema_up/ema_down
df['RSI'] = 100 - (100/(1 + rs))

# Create a simple RSI strategy
df['long_entry'] = df.RSI < 30
df['long_exit'] = df.RSI > 70
df['positions_long'] = df.long_entry.cumsum() - df.long_exit.cumsum()

# Plotting
plt.figure(figsize=(10,5))
plt.plot(df.index, df['Adj Close'])
plt.title('Price chart (Adj Close)')

plt.figure(figsize=(10,5))
plt.plot(df.index, df['RSI'])
plt.title('RSI chart')
plt.show()
```

This code downloads historical data for a given stock (in this case, 'AAPL') and calculates the RSI. It then creates a simple strategy that enters a long position when the RSI is below 30 (oversold) and exits when the RSI is above 70 (overbought). The results are plotted on a chart.

Please note that this is a very basic strategy and should not be used for actual trading without further refinement and testing.