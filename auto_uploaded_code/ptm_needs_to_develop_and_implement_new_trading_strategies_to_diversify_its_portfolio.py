from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop and implement new trading strategies, we would need to use various Python libraries such as pandas, numpy, matplotlib, and sklearn. Here is a simple example of a trading strategy using moving average crossover. 

Please note that this is a very basic strategy and real-world trading strategies involve much more complex analysis and risk management.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the stock to be used
stock = 'AAPL'

# Define the data range
start_date = '01-01-2010'
end_date = '01-01-2022'

# Get the data from Yahoo Finance
df = web.DataReader(stock, 'yahoo', start_date, end_date)

# Calculate the short-term simple moving average (SMA)
short_sma = df['Close'].rolling(window=20).mean()

# Calculate the long-term SMA
long_sma = df['Close'].rolling(window=100).mean()

# Create a new DataFrame to store the data
signals = pd.DataFrame(index=df.index)
signals['signal'] = 0.0

# Generate signals
signals['short_sma'] = short_sma
signals['long_sma'] = long_sma
signals['signal'][short_sma > long_sma] = 1.0

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Plot the data
plt.figure(figsize=(20, 15))
plt.plot(df['Close'], label='Close Price', color='blue')
plt.plot(signals['short_sma'], label='Short SMA', color='red')
plt.plot(signals['long_sma'], label='Long SMA', color='green')
plt.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_sma[signals.positions == 1.0],
         '^', markersize=10, color='m')
plt.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_sma[signals.positions == -1.0],
         'v', markersize=10, color='k')
plt.title('AAPL: SMA Crossover Trading Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()
```

In this code, we are using a simple moving average (SMA) crossover strategy. When the short-term SMA crosses above the long-term SMA, it generates a buy signal. Conversely, when the short-term SMA crosses below the long-term SMA, it generates a sell signal. The generated signals are then plotted on a graph. 

Please note that this is a very basic strategy and real-world trading strategies involve much more complex analysis and risk management. Always consult with a financial advisor before making trading decisions.