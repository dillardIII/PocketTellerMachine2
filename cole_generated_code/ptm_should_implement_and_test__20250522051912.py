Sure, here is a simple implementation of a moving average crossover strategy using Python and pandas. This strategy is one of the most common systematic strategies used by traders. It uses two moving averages, one short and one long. When the short moving average crosses above the long moving average, it's a signal to buy. Conversely, when the short moving average crosses below the long moving average, it's a signal to sell.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for desired ticker symbol
data = yf.download('AAPL','2020-01-01','2021-12-31')

# Calculate short-term simple moving average
short_sma = data.Close.rolling(window=20).mean()

# Calculate long-term simple moving average
long_sma = data.Close.rolling(window=100).mean()

# Create signals based on crossover
data['signal'] = 0.0
data['signal'][short_sma > long_sma] = 1.0

# Generate trading orders
data['position'] = data['signal'].diff()

# Print data
print(data)

# The result is a DataFrame that includes the price, the signal (1 for buy, 0 for sell) and the position (1 for entering a position, -1 for exiting).
```

Please note that this is a very basic strategy and should not be used for actual trading without further improvements and risk management. Also, it's important to remember that past performance is not indicative of future results. 

This script uses the `yfinance` library to download historical data from Yahoo Finance. If you haven't installed it yet, you can do so using pip:

```
pip install yfinance
```

Also, this script doesn't take into account transaction costs, slippage, or other factors that could impact the performance of a real trading strategy.