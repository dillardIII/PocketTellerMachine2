from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code to create an Exponential Moving Average (EMA) Crossover Analyzer. This code uses the pandas library for data manipulation and yfinance to download historical stock price data.

```python
import pandas as pd
import yfinance as yf

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover_analyzer(symbol, short_window, long_window):
    # Download historical data as dataframe
    data = yf.download(symbol, start='2020-01-01', end='2022-12-31')

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

This script downloads historical price data for a given symbol (in this case, 'AAPL' for Apple Inc.), calculates the short and long EMA (12 and 26 days, respectively), generates trading signals based on the crossover of the two EMAs, and prints the resulting data.

Please note that this is a simple implementation and may need to be adjusted based on your specific needs. Also, this script does not take into account trading fees or other factors that could impact actual trading results.