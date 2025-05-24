To create an EMA (Exponential Moving Average) Crossover Analyzer, we'll need to use a library like pandas for data manipulation and yfinance to download the stock data. Here's a simple implementation:

```python
import pandas as pd
import yfinance as yf

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover_analyzer(symbol, short_window, long_window):
    # Download historical data as dataframe
    data = yf.download(symbol, start='2020-01-01', end='2022-12-31')

    # Calculate short and long EMA
    data['short_EMA'] = calculate_ema(data['Close'], short_window)
    data['long_EMA'] = calculate_ema(data['Close'], long_window)

    # Create signals
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_EMA'][short_window:] > data['long_EMA'][short_window:], 1.0, 0.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

    # Print data
    print(data)

# Test the function
ema_crossover_analyzer('AAPL', 12, 26)
```

This script will download the historical data for the specified symbol (in this case, 'AAPL' for Apple Inc.), calculate the short and long EMA, generate a trading signal when the short EMA crosses the long EMA, and print the resulting dataframe.

Please note that this is a very basic implementation and might need to be adjusted based on your specific requirements. Also, this script doesn't include any error handling or data validation, which should be added in a real-world application.