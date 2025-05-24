Here is a simple Python code implementing a basic trading strategy using Moving Average Crossover. This strategy increases the number of trades by making a trade every time the short-term moving average crosses the long-term moving average.

Please note that this is a simplified example and actual trading strategies can be much more complex and require thorough testing and analysis.

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

def calculate_sma(data, window):
    return data.rolling(window=window).mean()

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving averages
    sma_short = calculate_sma(data, short_window)
    sma_long = calculate_sma(data, long_window)

    # Create a 'signals' DataFrame with the signal information
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0

    # Generate trading signals based on the crossover of the short and long window SMAs
    signals['signal'][short_window:] = np.where(sma_short[short_window:] > sma_long[short_window:], 1.0, 0.0)

    # Generate trading orders based on the signals
    signals['positions'] = signals['signal'].diff()

    return signals

# Fetch the data
start_date = '2020-01-01'
end_date = '2021-12-31'
ticker = 'AAPL'
data = web.DataReader(ticker, 'yahoo', start_date, end_date)

# Apply the trading strategy
short_window = 40
long_window = 100
signals = trading_strategy(data['Close'], short_window, long_window)

# Print the resulting signals
print(signals)
```

This strategy will generate a trade (either buy or sell) every time the short-term moving average crosses the long-term moving average. Please note that this is a very basic strategy and may not be profitable in real trading. Always backtest your strategies before using them in live trading.