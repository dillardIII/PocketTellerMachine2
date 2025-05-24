Sure, here is a simple Python code to analyze EMA (Exponential Moving Average) crossover. This code uses the `pandas` library for data manipulation and `yfinance` to download stock price data. 

```python
import pandas as pd
import yfinance as yf

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover_analyzer(stock, short_window, long_window):
    # Download historical data as dataframe
    data = yf.download(stock, start='2020-01-01', end='2022-12-31')

    # Calculate short and long EMA
    data['short_ema'] = calculate_ema(data['Close'], short_window)
    data['long_ema'] = calculate_ema(data['Close'], long_window)

    # Create signals
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_ema'][short_window:] > data['long_ema'][short_window:], 1.0, 0.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

    # Print data
    print(data)

# Test the function
ema_crossover_analyzer('AAPL', 12, 26)
```

This script first downloads historical data for the specified stock. Then it calculates short and long EMA for the closing prices. A signal is generated when the short EMA crosses the long EMA. Finally, trading positions are generated based on the signals.

Please note that this is a very basic version of an EMA crossover analyzer. In a real-world scenario, you would need to consider trading fees, slippage, and other factors. It's also important to remember that past performance is not indicative of future results.