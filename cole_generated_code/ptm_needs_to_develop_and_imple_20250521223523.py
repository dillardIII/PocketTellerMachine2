Sure, here's a simple example of a Python code that implements a basic trading strategy using Moving Average Crossover. This strategy is not guaranteed to increase chances of success, but it's a common starting point for developing more complex strategies.

Please note that this code requires `pandas` for data manipulation and `yfinance` to download stock price data. 

```python
import pandas as pd
import yfinance as yf

def calculate_sma(data, window):
    sma = data.rolling(window=window).mean()
    return sma

def calculate_ema(data, window):
    ema = data.ewm(span=window, adjust=False).mean()
    return ema

def trading_strategy(data, short_window, long_window):
    # Calculate the short and long window simple moving averages
    data['short_sma'] = calculate_sma(data['Close'], short_window)
    data['long_sma'] = calculate_sma(data['Close'], long_window)

    # Create signals based on the crossover of the short and long SMA
    data['signal'] = 0.0
    data['signal'][short_window:] = np.where(data['short_sma'][short_window:] 
                                             > data['long_sma'][short_window:], 1.0, 0.0)

    # Generate trading orders based on the signals
    data['positions'] = data['signal'].diff()

    return data

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

# Use the trading strategy
trading_df = trading_strategy(tickerDf, 50, 200)
```

In this code, a buy signal is generated when the short-term SMA crosses above the long-term SMA, and a sell signal is generated when the short-term SMA crosses below the long-term SMA. The signals are stored in the 'positions' column, where 1.0 represents a buy signal and -1.0 represents a sell signal.

Please note that this is a very simple trading strategy and may not be profitable in real trading. It's recommended to use more complex strategies and risk management techniques in actual trading. Also, this code does not take into account trading fees or slippage.