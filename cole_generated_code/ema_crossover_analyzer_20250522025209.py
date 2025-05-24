Sure, here is a simple Python code to analyze EMA (Exponential Moving Average) crossover. It uses pandas for data manipulation and yfinance to download stock price data. 

```python
import pandas as pd
import yfinance as yf

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def analyze_ema_crossover(symbol, short_window, long_window):
    # Download historical data as dataframe
    data = yf.download(symbol, start="2020-01-01", end="2021-12-31")

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

# Analyze EMA crossover for Apple with short window of 12 days and long window of 26 days
analyze_ema_crossover('AAPL', 12, 26)
```

This script will print out the stock price data with additional columns for short EMA, long EMA, signals, and positions. 

- When the short EMA crosses above the long EMA, it generates a buy signal (1.0). 
- When the short EMA crosses below the long EMA, it generates a sell signal (-1.0). 

Please note that you need to install yfinance and pandas if you haven't done so. You can install them using pip:

```python
pip install yfinance pandas
```

Also, this is a very basic EMA crossover strategy. In real trading, you should consider transaction costs, slippage, and other factors. Always backtest your strategy before live trading.