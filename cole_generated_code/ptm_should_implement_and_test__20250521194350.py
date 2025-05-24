Sure, I can provide a simple example of how you might implement a new trading strategy in Python. This is a very basic example and in real-world trading, strategies can become very complex. 

First, let's define a simple trading strategy: we will buy when the 50-day moving average crosses above the 200-day moving average, and sell when the 50-day moving average crosses below the 200-day moving average. This is known as a "Golden Cross" strategy.

Here's a simple implementation of this strategy using the `pandas` library to handle our data:

```python
import pandas as pd
import numpy as np

# Assuming 'data' is a pandas DataFrame and 'Close' is the column with closing prices
def calculate_moving_averages(data):
    data['50_MA'] = data['Close'].rolling(window=50).mean()
    data['200_MA'] = data['Close'].rolling(window=200).mean()
    return data

def implement_strategy(data):
    data = calculate_moving_averages(data)
    
    Buy = []
    Sell = []
    flag = -1

    for i in range(len(data)):
        if data['50_MA'][i] > data['200_MA'][i]:
            if flag != 1:
                Buy.append(data['Close'][i])
                Sell.append(np.nan)
                flag = 1
            else:
                Buy.append(np.nan)
                Sell.append(np.nan)
        elif data['50_MA'][i] < data['200_MA'][i]:
            if flag != 0:
                Sell.append(data['Close'][i])
                Buy.append(np.nan)
                flag = 0
            else:
                Buy.append(np.nan)
                Sell.append(np.nan)
        else:
            Buy.append(np.nan)
            Sell.append(np.nan)

    return (Buy, Sell)
```

This code will return two lists: one with the prices at which we should buy and another with the prices at which we should sell. 

Note: This is a very basic strategy and doesn't take into account many factors that you would need to consider in a real trading system, such as trading fees, slippage, and the fact that you can't trade fractional shares.