Here is a simple Python code to analyze EMA crossover using pandas library. This code assumes that you have a pandas DataFrame 'df' with 'Close' prices of the stock.

```python
import pandas as pd
import numpy as np

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover(data, short_window, long_window):
    short_ema = calculate_ema(data, short_window)
    long_ema = calculate_ema(data, long_window)

    crossover = pd.DataFrame(index=data.index)
    crossover['signal'] = 0.0
    crossover['short_ema'] = short_ema
    crossover['long_ema'] = long_ema

    # Create signals
    crossover['signal'][short_window:] = np.where(crossover['short_ema'][short_window:] > crossover['long_ema'][short_window:], 1.0, 0.0)

    # Generate trading orders
    crossover['positions'] = crossover['signal'].diff()

    return crossover

# Assuming df is your DataFrame and 'Close' is the column with closing prices
df = pd.read_csv('your_file.csv')  # replace 'your_file.csv' with your actual file
crossover = ema_crossover(df['Close'], 12, 26)

# Print data
print(crossover)
```

This code calculates EMA for two different periods (short and long). When the short EMA crosses above the long EMA, it generates a buy signal (1.0). When the short EMA crosses below the long EMA, it generates a sell signal (-1.0). The 'positions' column in the resulting DataFrame indicates these trading signals. 

Please replace 'your_file.csv' with your actual file that contains the 'Close' prices of the stock. 

Note: This is a very basic EMA crossover strategy and may not be profitable without additional filters and risk management.