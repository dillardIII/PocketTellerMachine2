To implement and test new trading strategies, we can create a simple Python code that simulates trading activity. In this example, we'll use a simple moving average crossover strategy. This strategy buys when the short-term moving average crosses above the long-term moving average and sells when the short-term moving average crosses below the long-term moving average.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr

# Define the trading strategy
def trading_strategy(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Long moving average
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Define backtesting
def backtest(data, signals):
    # Set the initial capital
    initial_capital= float(100000.0)

    # Create a DataFrame `positions`
    positions = pd.DataFrame(index=signals.index).fillna(0.0)

    # Buy a 100 shares
    positions['AAPL'] = 100*signals['signal']   
  
    # Initialize the portfolio with value owned   
    portfolio = positions.multiply(data['Close'], axis=0)

    # Store the difference in shares owned 
    pos_diff = positions.diff()

    # Add `holdings` to portfolio
    portfolio['holdings'] = (positions.multiply(data['Close'], axis=0)).sum(axis=1)

    # Add `cash` to portfolio
    portfolio['cash'] = initial_capital - (pos_diff.multiply(data['Close'], axis=0)).sum(axis=1).cumsum()   

    # Add `total` to portfolio
    portfolio['total'] = portfolio['cash'] + portfolio['holdings']

    # Add `returns` to portfolio
    portfolio['returns'] = portfolio['total'].pct_change()

    return portfolio

# Fetch the data
data = pdr.get_data_yahoo('AAPL', '2010-01-01', '2020-12-31')

# Implement the strategy
signals = trading_strategy(data, 40, 100)

# Run the backtest
portfolio = backtest(data, signals)

# Plot the results
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Portfolio value in $')
portfolio['total'].plot(ax=ax1, lw=2.)
plt.show()
```

Please note that this is a very basic trading strategy and is not recommended for actual trading. It's always important to thoroughly backtest any new trading strategy before live trading.