Sure, I can provide you with a simple example of a trading strategy using Python. This strategy will be a simple Moving Average Crossover strategy. This strategy is based on the idea that if the short term moving average crosses the long term moving average, it may be a signal of a trend reversal.

Please note that this is a very basic strategy and real-world trading strategies involve much more complex analysis and risk management.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Fetching historical data
def fetch_data(stock, start, end):
    return pdr.get_data_yahoo(stock, start, end)

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

# Plotting the strategy
def plot_strategy(df, signals):
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

# Define the stock and the period to fetch the data
stock = 'AAPL'
start_date = '01-01-2010'
end_date = '01-01-2022'

# Fetch the data
df = fetch_data(stock, start_date, end_date)

# Define the short and long windows
short_window = 40
long_window = 100

# Calculate the signals
signals = calculate_moving_averages(df, short_window, long_window)

# Plot the strategy
plot_strategy(df, signals)
```

This code will fetch the historical data for the given stock, calculate the short and long term moving averages, generate trading signals based on these averages and plot the strategy. The '^' markers on the plot represent buying signals and the 'v' markers represent selling signals.