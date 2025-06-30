from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I'll provide a simple example of a trading strategy using Python. This strategy is called Moving Average Crossover, which is a popular strategy used in algorithmic trading.

Please note that this is a very basic strategy and real-world trading involves a lot more factors like transaction costs, market impact, risk management etc.

We'll use `pandas` for data manipulation and `yfinance` to download the stock data.

```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for desired ticker symbol
def download_data(stock, start='2000-01-01', end='2020-12-31'):
    data = yf.download(stock, start, end)
    return pd.DataFrame(data)

# Implement Moving Average Crossover strategy
def implement_ma_crossover(data, short_window=40, long_window=100):
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

# Plot the data
def plot_data(data, signals):
    fig = plt.figure()

    ax1 = fig.add_subplot(111, ylabel='Price in $')

    data['Close'].plot(ax=ax1, color='r', lw=2.)
    signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

    ax1.plot(signals.loc[signals.positions == 1.0].index, 
             signals.short_mavg[signals.positions == 1.0],
             '^', markersize=10, color='m')
             
    ax1.plot(signals.loc[signals.positions == -1.0].index, 
             signals.short_mavg[signals.positions == -1.0],
             'v', markersize=10, color='k')

    plt.show()

# Test the strategy with AAPL stock
data = download_data('AAPL')
signals = implement_ma_crossover(data)
plot_data(data, signals)
```

This script downloads historical data for a given stock symbol, calculates short and long moving averages, generates signals when these averages cross, and plots the results.

Please note that you need to install the `pandas`, `yfinance` and `matplotlib` libraries if you haven't already. You can install them using pip:

```bash
pip install pandas yfinance matplotlib
```