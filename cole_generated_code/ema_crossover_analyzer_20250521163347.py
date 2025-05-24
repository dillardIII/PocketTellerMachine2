Sure, I can certainly help with writing the EMA Crossover Analyzer. For this, I will use the 'pandas' module for data manipulation and 'yfinance' to download stock data. Here is a simple implementation for it:

Please install the necessary packages using pip, if not installed:

```python
pip install pandas yfinance
```

Here is the code:

```python
import pandas as pd
import yfinance as yf

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def EMA_crossover(symbol, short_window=12, long_window=26):
    # Download historical data as dataframe
    data = yf.download(symbol, start='2020-01-01')

    # Calculate Short Term EMA and Long Term EMA
    data['Short_EMA'] = calculate_ema(data['Close'], short_window)
    data['Long_EMA'] = calculate_ema(data['Close'], long_window)

    # Create column for EMA crossover trading signal
    data['Signal'] = 0.0
    data['Signal'][short_window:] = np.where(data['Short_EMA'][short_window:] > data['Long_EMA'][short_window:], 1.0, 0.0)

    # Generate trading orders based on signals
    data['Position'] = data['Signal'].diff()

    return data

# Example usage:
df = EMA_crossover('AAPL')
print(df)
```

Note: You should adjust the `short_window` and `long_window` according to your strategy.

Disclaimer: This strategy is overly simplified and does not include other trading costs or considerations. Please use this as a starting point only.