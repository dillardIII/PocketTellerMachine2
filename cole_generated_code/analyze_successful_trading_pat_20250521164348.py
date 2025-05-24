Your task is quite broad and complex, therefore information like the type of data, the strategy you want to implement, etc. are not available.

Here is a simplified example of how you could start using Python to analyze a hypothetical trading dataset from previous days. 

```python
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt

# Load trading data from previous days
def load_data():
    df = pd.read_csv('trading_data.csv') # loading data from csv, assuming you have one
    # if trading data is from an online source, you might need to use the pandas_datareader module
    return df

df = load_data()

# function to calculate moving average
def moving_average(data, window_size):
    return data.rolling(window=window_size).mean()

# An example of a simple trading strategy. Buy when 50 days moving average crosses above 200 days moving average and sell when it crosses below
def simple_trading_strategy(data):
    # Calculate moving averages
    short_window = moving_average(data['Close'], 50)
    long_window = moving_average(data['Close'], 200)

    # Create signals
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Generate trading signals (buy=1.0, sell=-1.0)
    signals['signal'][50:] = np.where(short_window[50:] > long_window[50:], 1.0, -1.0)

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

signals = simple_trading_strategy(df)
```

Note that this code is quite simplified and your actual implementation can be much more complicated. Also, note that it uses the moving average crossover strategy, which might not be the best strategy for your case. You might want to perform more in-depth analysis, possibly including machine learning or other forms of AI, to create your trading strategy.

Implementing these strategies within a trading software such as PTM would also require connecting the Python script with the software's API, which is beyond the scope of this question.