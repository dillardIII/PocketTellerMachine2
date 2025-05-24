Sure, I can provide a simple example of a Python code for a trading strategy using Moving Average Crossover. This strategy is one of the simplest to understand and implement. It involves two moving averages, one short and one long. When the short moving average crosses above the long moving average, it signals a buy, and when it crosses below, it signals a sell.

Before we start, please make sure you have the `pandas`, `numpy`, `matplotlib`, and `yfinance` libraries installed in your Python environment. If not, you can install them using pip:

```python
pip install pandas numpy matplotlib yfinance
```

Here's a simple Python code:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for required stocks
ticker = "AAPL"
ticker_data = yf.download(ticker,'2020-1-1','2022-12-31')

# Calculate Short/Long Moving Averages
short_window = 40
long_window = 100

signals = pd.DataFrame(index=ticker_data.index)
signals['signal'] = 0.0

# Short moving average
signals['short_mavg'] = ticker_data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Long moving average
signals['long_mavg'] = ticker_data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print DataFrame
print(signals)

# Plotting
fig = plt.figure()
ax1 = fig.add_subplot(111, ylabel='Price in $')
ticker_data["Close"].plot(ax=ax1, color='r', lw=2.)
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='m')

# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='k')

plt.show()
```

This code will plot the stock's closing price, the short moving average, and the long moving average. Buy signals are represented with a '^' and sell signals are represented with a 'v'.

Please note that this is a very basic trading strategy and might not be profitable in real trading. It's always recommended to use more sophisticated strategies and consider more factors like trading fees, slippage, etc.