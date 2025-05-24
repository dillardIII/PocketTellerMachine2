Sure, here is a simple example of a Python code for a trading strategy. This strategy is based on moving averages crossover. When the short-term average crosses the long-term average, it may signal a good time to buy or sell.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window).mean()
    return ema

def trading_strategy(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Simple Moving Average
    signals['short_sma'] = calculate_sma(data, short_window)
    signals['long_sma'] = calculate_sma(data, long_window)

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_sma'][short_window:] 
                                                > signals['long_sma'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

def plot(data, signals):
    # Plot buy signals
    plt.plot(signals.loc[signals.positions == 1.0].index, 
             signals.short_sma[signals.positions == 1.0],
             '^', markersize=10, color='g')
   
    # Plot sell signals
    plt.plot(signals.loc[signals.positions == -1.0].index, 
             signals.short_sma[signals.positions == -1.0],
             'v', markersize=10, color='r')

    plt.show()

# Define the ticker list
tickers_list = ['AAPL']

# Fetch the data
data = pd.DataFrame(columns=tickers_list)
for ticker in tickers_list:
    data[ticker] = web.DataReader(ticker, data_source='yahoo', start='01-01-2010', end='01-01-2022')['Adj Close']

# Define the short and long windows
short_window = 40
long_window = 100

# Generate signals
signals = trading_strategy(data, short_window, long_window)

# Plot
plot(data, signals)
```

Please note that this is a simple trading strategy and may not be profitable in real trading. You should backtest any strategy before live trading. Also, this code assumes that you have the `pandas_datareader` package installed. If not, you can install it using pip:

```shell
pip install pandas_datareader
```

This code also uses Yahoo Finance as the data source, which may not be available in all regions. You may need to replace it with another data source if Yahoo Finance is not available in your region.