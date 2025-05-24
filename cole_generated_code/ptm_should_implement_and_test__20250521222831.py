Sure, I'll provide a simple example of a Python code implementing a basic Moving Average Crossover trading strategy. This strategy is one of the most commonly used strategies in trading. It involves two moving averages, one short (fast) and one long (slow). When the fast moving average crosses above the slow moving average, it's a signal to buy. Conversely, when the fast moving average crosses below the slow moving average, it's a signal to sell.

Please note that this is a very basic strategy and real-world trading involves many more factors.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Fetching historical data
def fetch_data(stock_symbol):
    df = pdr.get_data_yahoo(stock_symbol)
    return df

# Calculate moving averages
def calculate_moving_averages(df, short_window, long_window):
    signals = pd.DataFrame(index=df.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Long moving average
    signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   
    signals['positions'] = signals['signal'].diff()

    return signals

# Plotting
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

# Main function to run the strategy
def run_strategy(stock_symbol, short_window, long_window):
    df = fetch_data(stock_symbol)
    signals = calculate_moving_averages(df, short_window, long_window)
    plot_data(df, signals)

run_strategy('AAPL', 40, 100)
```
This code fetches historical data for a given stock symbol, calculates short and long moving averages, generates trading signals based on these averages, and plots the results. The 'run_strategy' function is the main function that runs the strategy. It takes three arguments: the stock symbol, the short moving average window, and the long moving average window.