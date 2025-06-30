from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple example of an EMA Crossover Analyzer using Python and the pandas library. 

```python

import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

# input
symbol = 'AAPL'
start = '2019-01-01'
end = '2022-12-31'

# Read data 
df = pdr.get_data_yahoo(symbol, start, end)

# View Columns
df.head()

# Create Short simple moving average
ShortEMA = df.Close.ewm(span=12, adjust=False).mean()

# Create Long simple moving average 
LongEMA = df.Close.ewm(span=26, adjust=False).mean()

# Create Exponential moving average
df['Short'] = ShortEMA
df['Long'] = LongEMA

# Create signals
df['signal'] = 0.0
df['signal'][short_window:] = np.where(df['Short'][short_window:] 
                                            > df['Long'][short_window:], 1.0, 0.0)   

# Generate trading orders
df['positions'] = df['signal'].diff()

# Print the DataFrame
print(df)
```

Please replace 'symbol', 'start', 'end' with your desired values. Note that different libraries would have different ways to calculate EMA and crossover. Above code simply demonstrates one of them. 

This example fetches historical data for AAPL, and computes two Exponential Moving Averages (EMA): one short (12 days) and one long (26 days). When the short EMA is greater than the long EMA, it is usually considered a bullish signal, and this code will generate a '1' signal. When the short EMA goes below the long EMA, it is a bearish signal and the code will regenerate a '0' signal. The 'positions' column tells us when the signals change - i.e. when there is a crossover. This purely TA based signal generating system is one of the most widely used in day trading systems.