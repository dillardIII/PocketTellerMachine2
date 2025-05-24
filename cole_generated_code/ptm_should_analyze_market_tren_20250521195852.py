Creating a Python script for analyzing market trends and data is a complex task and requires a deep understanding of both financial markets and data analysis. Here is a simple example of how you could start developing such a system using Python and pandas library. This code will fetch historical data, calculate simple moving average and generate a basic trading signal.

Please note that this is a very basic example and real-world trading systems are much more complex and take into account many more factors.

```python
import pandas as pd
import yfinance as yf

def calculate_sma(data, window):
    return data.rolling(window=window).mean()

def generate_trading_signals(data):
    buy_signals = (data['Close'] > data['SMA'])
    sell_signals = (data['Close'] < data['SMA'])
    return buy_signals, sell_signals

# Download historical data
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Calculate SMA
data['SMA'] = calculate_sma(data['Close'], window=14)

# Generate trading signals
buy_signals, sell_signals = generate_trading_signals(data)

# Print trading signals
print('Buy signals:')
print(buy_signals[buy_signals])
print('\nSell signals:')
print(sell_signals[sell_signals])
```

This script downloads historical data for Apple's stock, calculates a 14-day simple moving average (SMA), and generates trading signals based on the SMA. A buy signal is generated when the closing price is above the SMA, and a sell signal is generated when the closing price is below the SMA.

Please note that this is a very simplistic trading strategy and should not be used for real trading without further improvements and testing.