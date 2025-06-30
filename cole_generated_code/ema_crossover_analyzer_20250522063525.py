from ghost_env import INFURA_KEY, VAULT_ADDRESS
To complete this task, we need to use the pandas library in Python to calculate the Exponential Moving Average (EMA) and then analyze the crossover points. Here's a simple implementation of an EMA Crossover Analyzer:

```python
import pandas as pd
import pandas_datareader as pdr
import datetime

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover_analyzer(stock, short_window, long_window):
    end = datetime.datetime.now()
    start = datetime.datetime(end.year - 1, end.month, end.day)
    data = pdr.get_data_yahoo(stock, start, end)
    
    # Calculate short and long EMA
    short_ema = calculate_ema(data['Close'], short_window)
    long_ema = calculate_ema(data['Close'], long_window)
    
    # Create signals
    data['short_ema'] = short_ema
    data['long_ema'] = long_ema
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_ema'][short_window:] > data['long_ema'][short_window:], 1.0, 0.0)
    data['positions'] = data['signal'].diff()
    
    # Print crossover points
    print(data[data['positions'] == 1.0])
    print(data[data['positions'] == -1.0])

# Test the function
ema_crossover_analyzer('AAPL', 12, 26)
```

This code will print out the points where the short EMA crosses above the long EMA (a potential buy signal) and where it crosses below (a potential sell signal). Please replace 'AAPL' with the stock symbol you want to analyze.

The function `ema_crossover_analyzer` takes three arguments: the stock symbol, the short EMA window, and the long EMA window. It fetches the stock data for the past year, calculates the short and long EMA, and then determines the crossover points.

Note: This code requires the pandas_datareader library to fetch stock data. If you don't have this library, you can install it using pip:

```python
pip install pandas-datareader
```

Also, please be aware that this is a very basic implementation of an EMA Crossover Analyzer. In a real-world scenario, you would likely want to include additional features and checks, such as handling missing data, checking for API errors, and so on.