from ghost_env import INFURA_KEY, VAULT_ADDRESS
Below, I will be considering a very simple trading strategy named "Moving Average Crossover", which is commonly used in algorithmic trading. Please note that this strategy operates on the basis of historical data and does not guarantee future performance. It's recommended to use it in conjunction with other strategies and tools to determine optimal trading decisions.

Assumptions:
- We have access to daily historical price data.
- When the short-term average crosses the long-term average, we will make a trade.
- When the short-term average is above the long-term average, we are long.
- When the short-term average is below the long-term average, we are short.

Here's the code:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr

def calculate_moving_average(data, window):
    return data['Close'].rolling(window=window).mean()

def implement_strategy(data, short_window, long_window):
    # Calculate the moving averages
    data['short_mavg'] = calculate_moving_average(data, short_window)
    data['long_mavg'] = calculate_moving_average(data, long_window)

    # Create signals
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_mavg'][short_window:] 
                                              > data['long_mavg'][short_window:], 1.0, 0.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

    # Print the DataFrame
    print(data)

def test_strategy(symbol, start_date, end_date, short_window, long_window):
    # Obtain the historical price data from Yahoo Finance
    data = pdr.get_data_yahoo(symbol, start=start_date, end=end_date)

    # Implement the strategy
    implement_strategy(data, short_window, long_window)

test_strategy('AAPL', '01-01-2016', '01-01-2022', 40, 100)
```

This is a demonstration using Python and libraries such as pandas and Yahoo Finance for data. Remember that trading algorithms involve significant risk, and past performance is not always indicative of future results. Always debug and validate your strategies before each use. You may need to adjust the parameters for the short and long windows.

(Please replace 'AAPL', '01-01-2016', '01-01-2022', 40, 100 with your appropriate values)