Sure, I can provide a simple example of a trading strategy using Python. This strategy will be based on Moving Average Crossover, which is a popular strategy used in algorithmic trading. 

The strategy is simple: 
- Buy when the short-term moving average crosses above the long-term moving average.
- Sell when the short-term moving average crosses below the long-term moving average.

Here is a simple Python code that implements this strategy using pandas library.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

# Fetching the data
data = pdr.get_data_yahoo('AAPL', start='2020-01-01', end='2021-12-31')

# Calculating the short-term simple moving average
short_sma = data.Close.rolling(window=20).mean()

# Calculating the long-term simple moving average
long_sma = data.Close.rolling(window=100).mean()

# Creating a new DataFrame
signals_df = pd.DataFrame(index=data.index)
signals_df['signal'] = 0.0

# Creating signals
signals_df['short_mavg'] = short_sma
signals_df['long_mavg'] = long_sma

# Generate trading signals (1 for buy, -1 for sell)
signals_df['signal'][short_sma > long_sma] = 1.0
signals_df['signal'][short_sma < long_sma] = -1.0

# Generate trading orders
signals_df['positions'] = signals_df['signal'].diff()

print(signals_df)
```

This code fetches the historical data for Apple Inc. (AAPL) from Yahoo Finance, calculates the short-term and long-term moving averages, generates trading signals based on the crossover of these moving averages, and finally generates trading orders.

Please note that this is a very basic trading strategy and may not be profitable in real-world trading. It's always recommended to backtest any strategy extensively before live trading. Also, this strategy doesn't take into account trading fees or slippage. 

You need to install pandas_datareader and yfinance to run this code. You can install them using pip:

```bash
pip install pandas_datareader yfinance
```