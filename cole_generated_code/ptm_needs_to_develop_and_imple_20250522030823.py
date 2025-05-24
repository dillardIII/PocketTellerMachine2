Sure, but please note that a trading strategy is a complex topic and requires a lot more information and data to be effective. However, I can provide a simple example of a Python code that uses a basic trading strategy. This strategy is based on moving averages, a common indicator used in technical analysis.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

# Fetching the data
def get_data(symbol, start_date, end_date):
    data = pdr.get_data_yahoo(symbol, start=start_date, end=end_date)
    return data

# Calculating the moving averages
def calculate_moving_averages(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)   
    signals['positions'] = signals['signal'].diff()
    return signals

# Plotting the data
def plot_data(data, signals):
    fig = plt.figure()
    ax1 = fig.add_subplot(111, ylabel='Price in $')
    data['Close'].plot(ax=ax1, color='r', lw=2.)
    signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)
    ax1.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0], '^', markersize=10, color='m')
    ax1.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0], 'v', markersize=10, color='k')
    plt.show()

if __name__ == "__main__":
    data = get_data('AAPL', '2010-01-01', '2020-12-31')
    signals = calculate_moving_averages(data, 40, 100)
    plot_data(data, signals)
```

In this example, we fetch the historical data for a stock (AAPL in this case) from Yahoo Finance. We then calculate the short-term (40 days) and long-term (100 days) moving averages. If the short-term average is above the long-term average, we generate a 'buy' signal, and if it's below, we generate a 'sell' signal. Finally, we plot the stock price, the moving averages, and the buy/sell signals.

Please note that this is a very basic strategy and should not be used for actual trading without further refinement and testing.