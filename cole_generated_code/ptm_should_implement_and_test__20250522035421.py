To implement and test new trading strategies, we can use Python libraries like pandas for data manipulation, numpy for numerical computations, and matplotlib for visualizations. We will also use yfinance to download historical market data from Yahoo Finance.

Here is a simple implementation of a Moving Average Crossover strategy:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for desired ticker symbol
def download_data(stock, start='2000-01-01', end='2020-12-31'):
    data = yf.download(stock, start, end)
    return pd.DataFrame(data)

# Implement the Moving Average Crossover strategy
def implement_strategy(data, short_window=40, long_window=100):
    # Create a 'signals' DataFrame with signal information
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Create short simple moving average over the short window
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Create long simple moving average over the long window
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Plotting the strategy
def plot_strategy(data, signals):
    # Initialize the plot figure
    fig = plt.figure()

    # Add a subplot and label for y-axis
    plt1 = fig.add_subplot(111,  ylabel='Price in $')

    # Plot the closing price
    data['Close'].plot(ax=plt1, color='r', lw=2.)

    # Plot the short and long moving averages
    signals[['short_mavg', 'long_mavg']].plot(ax=plt1, lw=2.)

    # Plot the buy signals
    plt1.plot(signals.loc[signals.positions == 1.0].index, 
             signals.short_mavg[signals.positions == 1.0],
             '^', markersize=10, color='m')
    
    # Plot the sell signals
    plt1.plot(signals.loc[signals.positions == -1.0].index, 
             signals.short_mavg[signals.positions == -1.0],
             'v', markersize=10, color='k')
    
    # Show the plot
    plt.show()

# Test the strategy with a stock, for example, Apple
data = download_data('AAPL')
signals = implement_strategy(data)
plot_strategy(data, signals)
```

This script downloads the historical data for Apple stock, implements a Moving Average Crossover strategy, and plots the strategy. The pink arrows represent buying signals and the black arrows represent selling signals. 

Please note that this is a very basic trading strategy and it's used for illustrative purposes. Real-world trading strategies are much more complex and take into account many other factors.