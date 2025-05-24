Sure, I can provide you with a simple Python code that uses pandas library to calculate Exponential Moving Average (EMA) and analyze its crossover. Please note that you need to provide the data for the analysis.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assuming 'data' is your DataFrame and 'Close' is the column with closing prices
def calculate_ema(data, window, column='Close'):
    return data[column].ewm(span=window, adjust=False).mean()

def plot_crossovers(data, column='Close'):
    # Calculate short and long term EMAs
    short_ema = calculate_ema(data, window=12, column=column)
    long_ema = calculate_ema(data, window=26, column=column)

    # Create signals
    data['Buy_Signal'] = np.where(short_ema > long_ema, 1, 0)
    data['Sell_Signal'] = np.where(short_ema < long_ema, -1, 0)

    # Plot
    plt.figure(figsize=(12,5))
    plt.plot(data[column], label=column, color='blue', alpha=0.35)
    plt.plot(short_ema, label='Short EMA', color='red', alpha=0.35)
    plt.plot(long_ema, label='Long EMA', color='green', alpha=0.35)
    plt.scatter(data.index, data['Buy_Signal']*data[column], color='green')
    plt.scatter(data.index, data['Sell_Signal']*data[column], color='red')
    plt.title('EMA Crossover')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend(loc='upper left')
    plt.show()

# Use the function
plot_crossovers(data)
```

This script calculates short-term (12 periods) and long-term (26 periods) EMAs, then it creates buy signals when the short EMA crosses above the long EMA, and sell signals when it crosses below. These signals are then plotted on a graph.

Please replace 'data' with your actual DataFrame and 'Close' with your actual column name that contains the closing prices.

Also, please note that this is a very basic strategy and may not be profitable in real trading. Always backtest your strategies before live trading.