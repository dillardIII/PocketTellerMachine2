Sure, here's a simple Python code that implements a basic trading strategy known as the Moving Average Crossover Strategy. This strategy is used to identify new trading opportunities by comparing a short-term moving average with a long-term moving average.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def implement_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving averages
    sma_short = calculate_sma(data, short_window)
    sma_long = calculate_sma(data, long_window)

    # Create a 'signals' DataFrame with the `signal` column
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Generate trading signals (1 for buy, -1 for sell)
    signals['signal'][short_window:] = np.where(sma_short[short_window:] > sma_long[short_window:], 1.0, -1.0)

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Fetch the data
start_date = '2016-01-01'
end_date = '2021-12-31'
ticker = 'AAPL'
data = web.DataReader(ticker, 'yahoo', start_date, end_date)

# Implement the strategy
short_window = 40
long_window = 100
signals = implement_strategy(data['Close'], short_window, long_window)

# Plot the data
plt.figure(figsize=(10,5))
plt.plot(data['Close'], label=ticker)
plt.plot(calculate_sma(data['Close'], short_window), label='40-days SMA')
plt.plot(calculate_sma(data['Close'], long_window), label='100-days SMA')
plt.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0], '^', markersize=10, color='g', label='buy')
plt.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0], 'v', markersize=10, color='r', label='sell')
plt.title('Apple Inc. - Moving Average Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()
```

Please note that this is a simple trading strategy and may not be suitable for real-world trading. It's always recommended to backtest any strategy before live trading. Also, this code assumes that you have the necessary libraries installed and that you have a stable internet connection to fetch the stock data.