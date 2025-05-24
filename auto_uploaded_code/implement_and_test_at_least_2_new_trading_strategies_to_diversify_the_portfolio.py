Sure, here are two simple trading strategies implemented in Python. 

1. Moving Average Crossover Strategy: This strategy is based on the concept of moving averages, where we buy when the short term moving average crosses above the long term moving average and sell when the short term moving average crosses below the long term moving average.

2. Mean Reversion Strategy: This strategy is based on the concept that the high and low prices of an asset are a temporary phenomenon that revert to their mean value periodically. So, we buy when the price is low (a certain standard deviations below the mean) and sell when the price is high (a certain standard deviations above the mean).

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

# Moving Average Crossover Strategy
def moving_average_crossover_strategy(stock, short_window, long_window):
    # Get stock data
    df = web.DataReader(stock, 'yahoo', start='01/01/2010', end='01/01/2022')
    # Calculate short and long moving averages
    df['Short_MA'] = df['Close'].rolling(window=short_window, min_periods=1).mean()
    df['Long_MA'] = df['Close'].rolling(window=long_window, min_periods=1).mean()
    # Create signals
    df['Buy_Signal'] = np.where(df['Short_MA'] > df['Long_MA'], 1, 0)
    df['Sell_Signal'] = np.where(df['Short_MA'] < df['Long_MA'], -1, 0)
    df['Signal'] = df['Buy_Signal'] + df['Sell_Signal']
    return df

# Mean Reversion Strategy
def mean_reversion_strategy(stock, window, no_of_std):
    # Get stock data
    df = web.DataReader(stock, 'yahoo', start='01/01/2010', end='01/01/2022')
    # Calculate mean and standard deviation
    df['Mean'] = df['Close'].rolling(window=window).mean()
    df['Std'] = df['Close'].rolling(window=window).std()
    # Create signals
    df['Buy_Signal'] = np.where(df['Close'] < df['Mean'] - no_of_std * df['Std'], 1, 0)
    df['Sell_Signal'] = np.where(df['Close'] > df['Mean'] + no_of_std * df['Std'], -1, 0)
    df['Signal'] = df['Buy_Signal'] + df['Sell_Signal']
    return df

# Test strategies
apple_data = moving_average_crossover_strategy('AAPL', 50, 200)
print(apple_data)

google_data = mean_reversion_strategy('GOOGL', 20, 1)
print(google_data)
```

Please note that these are very simple strategies and may not be profitable in real trading. They are used here just for demonstration purposes. Always backtest your strategies before using them in live trading.