Sure, here's a simple example of a trading strategy implemented in Python using the pandas library. This strategy is based on a simple moving average (SMA) crossover, which is a common trading strategy. 

Please note that this is a very basic example and real trading strategies can be much more complex and require careful consideration of many factors.

```python
import pandas as pd
import pandas_datareader as pdr

# Define the trading strategy
def trading_strategy(data, short_window, long_window):
    # Initialize the 'signals' DataFrame with the 'signal' column
    data['signal'] = 0.0

    # Create short simple moving average over the short window
    data['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Create long simple moving average over the long window
    data['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    data['signal'][short_window:] = np.where(data['short_mavg'][short_window:] 
                                             > data['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    data['positions'] = data['signal'].diff()

# Load data
data = pdr.get_data_yahoo('AAPL', '2020-01-01', '2021-12-31')

# Apply the trading strategy
trading_strategy(data, 50, 200)
```

In this code, we first define a function `trading_strategy` that takes a DataFrame of price data and two window lengths for the moving averages. It calculates a short and long moving average of the closing prices, then generates a trading signal whenever the short moving average crosses the long moving average. A buy signal (1.0) is generated when the short moving average is above the long moving average, and a sell signal (0.0) when the short moving average is below the long moving average. The `positions` column represents the trading orders: a positive value indicates a buy order and a negative value indicates a sell order.

We then load historical price data for Apple Inc. (AAPL) from Yahoo Finance using the `pandas_datareader` library, and apply the trading strategy to this data.