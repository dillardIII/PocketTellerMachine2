from ghost_env import INFURA_KEY, VAULT_ADDRESS
To diversify PTM's strategies, we could introduce a few different trading strategies such as Mean Reversion, Momentum Trading, and Breakout Trading. Here's a simple Python code for these strategies:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

# Define the instruments to download
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']

# Define which online source to use
data_source = 'yahoo'

# Define the start and end dates
start_date = '2015-01-01'
end_date = '2020-12-31'

# User pandas_reader.data.DataReader to load the desired data
panel_data = pdr.get_data_yahoo(tickers, start_date, end_date)

# Getting just the adjusted closing prices
adj_close = panel_data['Adj Close']

# Calculate the short and long windows
short_window = 40
long_window = 100

# Initialize the signals DataFrame with the signal column
signals = pd.DataFrame(index=adj_close.index)
signals['signal'] = 0.0

# Create short simple moving average over the short window
signals['short_mavg'] = adj_close.rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
signals['long_mavg'] = adj_close.rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print `signals`
print(signals)
```

This is a simple Moving Average Crossover strategy that could be a part of PTM's diversified strategies. The strategy is to buy when the short moving average exceeds the long moving average, and to sell when the short moving average falls below the long moving average.

Please note that this is a very basic strategy and in real trading scenario, you would need to consider transaction costs, slippage, risk management, etc. Also, you would need to backtest any strategy before live trading.