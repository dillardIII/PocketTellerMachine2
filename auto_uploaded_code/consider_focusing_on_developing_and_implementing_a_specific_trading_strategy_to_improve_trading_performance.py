from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, one common algorithmic trading strategy is a Moving Average Crossover, which can be implemented in Python. Here's an example with some dummy data. This strategy involves trading when a short-term moving average crosses a long-term moving average.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

# Define the trading strategy
def trading_strategy(data, short_window, long_window):
    data['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    data['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_mavg'][short_window:] > data['long_mavg'][short_window:], 1.0, 0.0)   
    data['orders'] = data['signal'].diff()

#Fetching data and applying strategy
def main():
    # Download daily prices 
    data = web.DataReader('AAPL', 'yahoo', start='01/01/2010', end='01/01/2022')
    
    # Moving average parameters
    short_window = 40
    long_window = 100
    
    # Apply the strategy
    trading_strategy(data, short_window, long_window)
    
    # Plot stock price, short-term and long-term moving averages and buy/sell signals
    plt.figure(figsize=(15,9))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['short_mavg'], label='40-days MA', color='red')
    plt.plot(data['long_mavg'], label='100-days MA', color='black')
    plt.plot(data.loc[data.orders== 1.0].index, data.short_mavg[data.orders == 1.0], '^' , markersize=10, color='g')
    plt.plot(data.loc[data.orders== -1.0].index, data.short_mavg[data.orders == -1.0], 'v' , markersize=10, color='r')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('AAPL trading signals')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()
```

In this code, we download the stock data of `AAPL` (Apple Inc.) from `yahoo` finance. We then compute short-term (40 days) and long-term (100 days) moving averages of its closing price. When the short-term moving average crosses above the long-term moving average, we generate a buy signal. When the short-term-moving average crosses below the long-term moving average, we generate a sell signal. These signals are then plotted on a graph alongside the stock price and moving averages.

Please note, backtesting is required to evaluate this trading strategy. Live trading solely based on this strategy is not recommended as it is a simplistic approach not taking into account many factors that could influence the stock price. For real trading strategy, more sophisticated and complex algorithm considering various other factors is required. It is always advised to thoroughly backtest any trading strategy before live trading. Also, using this strategy does not guarantee any profit and can result in significant losses, and should be used for educational purposes only.
