from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide you with a simple example of a trading strategy implemented in Python. This strategy is called Moving Average Crossover. It's a basic strategy that involves two moving averages, one short and one long. When the short moving average crosses above the long moving average, it's a signal to buy. When it crosses below, it's a signal to sell.

Please note that this is a very simple strategy and real-world trading strategies can be much more complex and involve many more factors.

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

    signals['short_mavg'] = calculate_sma(data, short_window)
    signals['long_mavg'] = calculate_sma(data, long_window)

    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)

    signals['positions'] = signals['signal'].diff()

    return signals

def plot(data, signals):
    fig = plt.figure()

    ax1 = fig.add_subplot(111, ylabel='Price')
    data.plot(ax=ax1, color='r', lw=2.)

    signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

    ax1.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0], '^', markersize=10, color='m')
    ax1.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0], 'v', markersize=10, color='k')

    plt.show()

if __name__ == "__main__":
    data = web.DataReader('AAPL', 'yahoo', start='01/01/2010', end='01/01/2022')['Close']
    signals = trading_strategy(data, 40, 100)
    plot(data, signals)
```

This script will plot the closing prices of Apple Inc. (AAPL) from 2010 to 2022, the short and long moving averages, and the buy and sell signals. The '^' markers indicate buying points and the 'v' markers indicate selling points.

Please note that you will need to install `pandas_datareader` library to fetch the data from Yahoo Finance. You can install it using pip:

```shell
pip install pandas_datareader
```

Also, this is a very basic strategy and doesn't take into account trading costs, slippage, or other factors that could impact the profitability of a strategy. Always backtest your strategies with historical data before live trading.