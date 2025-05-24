Here is a simple Python code for a trading strategy using Moving Average Crossover. This strategy is used to identify potential buy and sell signals. 

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Fetching the data
def get_data(symbol, start_date, end_date):
    df = web.DataReader(symbol, 'yahoo', start_date, end_date)
    return df

# Calculating Moving Averages
def calculate_MA(df, short_window, long_window):
    signals = pd.DataFrame(index=df.index)
    signals['signal'] = 0.0
    
    # Short moving average
    signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    
    # Long moving average
    signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    
    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   
    # Generate trading orders
    signals['positions'] = signals['signal'].diff()
    
    return signals

# Plotting the data
def plot_data(df, signals):
    fig = plt.figure()
    
    ax1 = fig.add_subplot(111, ylabel='Price in $')
    df['Close'].plot(ax=ax1, color='r', lw=2.)
    signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)
    
    ax1.plot(signals.loc[signals.positions == 1.0].index, 
             signals.short_mavg[signals.positions == 1.0],
             '^', markersize=10, color='m')
             
    ax1.plot(signals.loc[signals.positions == -1.0].index, 
             signals.short_mavg[signals.positions == -1.0],
             'v', markersize=10, color='k')
             
    plt.show()

if __name__ == "__main__":
    symbol = 'AAPL'
    start_date = '2016-01-01'
    end_date = '2021-12-31'
    short_window = 40
    long_window = 100
    
    df = get_data(symbol, start_date, end_date)
    signals = calculate_MA(df, short_window, long_window)
    plot_data(df, signals)
```

This code fetches the data of a particular stock symbol from Yahoo Finance, calculates the short and long moving averages, generates signals when these averages cross each other, and plots the data along with the buy and sell signals.

Please note that this is a simple trading strategy and may not always result in wins. It's always recommended to use more sophisticated strategies and consider other factors like trading volume, market trends, etc.