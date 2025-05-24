To diversify trading strategies, we can implement different types of trading strategies such as Mean Reversion, Momentum, Statistical Arbitrage etc. However, without specific details about PTM's current strategies and trading data, it's hard to provide a specific code. 

Here is a simple example of a Mean Reversion strategy using Python:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

# Fetching data
def fetch_data(stock, start, end):
    df = pdr.get_data_yahoo(stock, start, end)
    return df['Adj Close']

# Mean Reversion Strategy
def mean_reversion_strategy(data, window, z):
    # Calculate the moving average
    ma = data.rolling(window=window).mean()
    
    # Calculate the standard deviation
    std = data.rolling(window=window).std()
    
    # Create a dataframe
    df = pd.DataFrame(data)
    df['ma'] = ma
    df['std'] = std
    
    # Create signals
    df['signal'] = 0
    df.loc[df.index > ma.index[window], 'signal'] = np.where(df['Adj Close'] > ma + z*std, -1, 0)
    df.loc[df.index > ma.index[window], 'signal'] = np.where(df['Adj Close'] < ma - z*std, 1, df['signal'])
    
    return df

# Fetch data
data = fetch_data('AAPL', '2010-01-01', '2020-12-31')

# Apply strategy
df = mean_reversion_strategy(data, 50, 1)

# Print the dataframe
print(df)
```

This is a simple mean reversion strategy that goes long when the price is below the moving average by a certain standard deviation and goes short when the price is above the moving average by a certain standard deviation.

Please note that this is a very basic strategy and may not be profitable in real trading. It's always recommended to thoroughly backtest any trading strategy before live trading. Also, this code assumes that we have the necessary permissions to fetch data from Yahoo Finance.