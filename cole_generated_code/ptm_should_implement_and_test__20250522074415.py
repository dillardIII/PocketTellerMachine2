from ghost_env import INFURA_KEY, VAULT_ADDRESS
To implement and test new trading strategies, we can use the Python libraries like pandas for data manipulation, numpy for numerical computation and matplotlib for visualization. We will also use the yfinance library to download the historical market data from Yahoo finance.

Here is a simple implementation of a Moving Average Crossover strategy. This strategy is one of the most commonly used strategies in the trading world. It's based on the principle that the short-term moving average crossing the long-term moving average can be an indicator of the market direction.

```python
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for desired ticker symbol
def download_data(stock, start, end):
    data = {}
    ticker = yf.download(stock, start, end)
    data['Price'] = ticker['Adj Close']
    return pd.DataFrame(data)

# Calculate moving averages
def calculate_MA(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    signals['short_mavg'] = data['Price'].rolling(window=short_window, min_periods=1, center=False).mean()
    signals['long_mavg'] = data['Price'].rolling(window=long_window, min_periods=1, center=False).mean()
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)
    signals['positions'] = signals['signal'].diff()
    return signals

# Plot the data
def plot_data(data, signals):
    fig = plt.figure()
    ax1 = fig.add_subplot(111, ylabel='Price in $')
    data['Price'].plot(ax=ax1, color='r', lw=2.)
    signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)
    ax1.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0], '^', markersize=10, color='m')
    ax1.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0], 'v', markersize=10, color='k')
    plt.show()

# Define the main function
def main():
    stock = 'AAPL'
    start_date = '01-01-2010'
    end_date = '01-01-2022'
    short_window = 40
    long_window = 100
    data = download_data(stock, start_date, end_date)
    signals = calculate_MA(data, short_window, long_window)
    plot_data(data, signals)

if __name__ == "__main__":
    main()
```
This code will download the historical data for the desired ticker symbol, calculate the short and long moving averages, generate trading signals and plot the data. The green triangles represent the buy signals and the red triangles represent the sell signals.

Please note that this is a very basic trading strategy and might not be profitable in real trading. Always backtest your strategies before live trading.