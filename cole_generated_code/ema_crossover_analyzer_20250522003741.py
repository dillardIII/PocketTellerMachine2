Sure, here's a simple Python code to analyze EMA crossover using the `pandas` library. The code assumes that you have a DataFrame `df` with a 'Close' column for close prices. 

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def plot_graph(data):
    plt.figure(figsize=(14,7))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['Short_EMA'], label='Short EMA', color='red')
    plt.plot(data['Long_EMA'], label='Long EMA', color='green')
    plt.title('EMA Crossover')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend(loc='upper left')
    plt.show()

def ema_crossover(data, short_window, long_window):
    # Calculate the short and long EMA
    data['Short_EMA'] = calculate_ema(data['Close'], short_window)
    data['Long_EMA'] = calculate_ema(data['Close'], long_window)
    
    # Create signals
    data['Buy_Signal'] = np.where(data['Short_EMA'] > data['Long_EMA'], 1, 0)
    data['Sell_Signal'] = np.where(data['Short_EMA'] < data['Long_EMA'], -1, 0)
    
    return data

# Assuming df is your DataFrame and it has a 'Close' column
df = ema_crossover(df, 12, 26)
plot_graph(df)
```

This code calculates the short and long EMA (Exponential Moving Average) for the given data. It then creates a buy signal when the short EMA crosses above the long EMA and a sell signal when the short EMA crosses below the long EMA. 

Please replace `df` with your actual dataframe and make sure it has a 'Close' column. You may also adjust the short and long window parameters as per your needs.

The `plot_graph` function plots the close price, short EMA, and long EMA. The EMA crossover points can be visually identified from this plot.