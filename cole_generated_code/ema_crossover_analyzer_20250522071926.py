from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can help you with that. Here's a simple Python code snippet that uses the `pandas` library to calculate the Exponential Moving Average (EMA) and identify crossover points.

```python
import pandas as pd
import numpy as np
import yfinance as yf

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover_analyzer(symbol, short_window, long_window):
    # Download historical data as dataframe
    df = yf.download(symbol, start="2020-01-01", end="2022-12-31")

    # Calculate short and long EMA
    df['short_ema'] = calculate_ema(df['Close'], short_window)
    df['long_ema'] = calculate_ema(df['Close'], long_window)

    # Create signals
    df['signal'] = 0.0
    df['signal'][short_window:] = np.where(df['short_ema'][short_window:] > df['long_ema'][short_window:], 1.0, 0.0)

    # Generate trading orders
    df['positions'] = df['signal'].diff()

    # Print the dataframe
    print(df)

    # Identify crossover points
    crossover_points = df[df['positions'] != 0]
    print("\nCrossover points:")
    print(crossover_points)

# Test the function
ema_crossover_analyzer('AAPL', 12, 26)
```

This script downloads historical data for a given symbol (in this case, 'AAPL' for Apple Inc.) and calculates the short-term and long-term EMA. It then generates trading signals based on these EMAs and identifies the points where these signals change, which are the crossover points.

Please note that you need to install `yfinance` and `pandas` libraries. You can install them using pip:

```bash
pip install yfinance pandas
```

Also, please remember to replace 'AAPL', 12, and 26 with the stock symbol and EMA periods you're interested in.