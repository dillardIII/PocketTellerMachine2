Sure, here is a simple Python code that implements a basic moving average crossover strategy. This strategy is one of the most common systematic trading strategies that uses two moving averages, one short and one long. When the short moving average crosses above the long moving average, it signals a buy signal. When the short moving average crosses below the long moving average, it signals a sell signal.

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime

# Download historical data for required stocks
ticker = "AAPL"
ticker_data = yf.download(ticker, start="2020-01-01", end=datetime.today().strftime('%Y-%m-%d'))

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

# Calculate short-term/simple moving average
short_sma = calculate_sma(ticker_data['Close'], window=20)
# Calculate long-term/simple moving average
long_sma = calculate_sma(ticker_data['Close'], window=100)

# Create signals
signals = pd.DataFrame(index=ticker_data.index)
signals['signal'] = 0.0
signals['short_sma'] = short_sma
signals['long_sma'] = long_sma

# Generate trading signals (buy=1 , sell=-1)
signals['signal'][short_sma > long_sma] = 1.0
signals['signal'][short_sma < long_sma] = -1.0

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print `signals`
print(signals)
```

Please note that this is a very basic strategy and might not be profitable in real trading. Always backtest your strategies before live trading. Also, this code requires the `yfinance`, `pandas`, and `numpy` libraries. If you don't have them installed, you can do so by using pip:

```bash
pip install yfinance pandas numpy
```

This code uses Yahoo Finance to download the historical data. You can replace "AAPL" with the ticker symbol of the stock you want to test this strategy on.