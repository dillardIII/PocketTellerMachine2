Sure, here is a simple implementation of a Relative Strength Index (RSI) strategy generator in Python using the `pandas` and `yfinance` libraries:

```python
import pandas as pd
import yfinance as yf

def calculate_rsi(data, window):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    average_gain = up.rolling(window=window).mean()
    average_loss = abs(down.rolling(window=window).mean())

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def rsi_strategy(ticker, window=14):
    data = yf.download(ticker, start='2020-01-01', end='2022-12-31')
    data['RSI'] = calculate_rsi(data['Close'], window)
    buy_signals, sell_signals = [], []

    for i in range(1, len(data)):
        if data['RSI'][i-1] > 30 and data['RSI'][i] <= 30:
            buy_signals.append(data['Close'][i])
            sell_signals.append(float('nan'))
        elif data['RSI'][i-1] < 70 and data['RSI'][i] >= 70:
            sell_signals.append(data['Close'][i])
            buy_signals.append(float('nan'))
        else:
            buy_signals.append(float('nan'))
            sell_signals.append(float('nan'))

    data['Buy_Signal_Price'] = buy_signals
    data['Sell_Signal_Price'] = sell_signals
    return data

# Test the function
print(rsi_strategy('AAPL'))
```

This script downloads historical data for a given ticker symbol (e.g., 'AAPL' for Apple Inc.), calculates the RSI for each day, and generates buy/sell signals based on the RSI. A buy signal is generated when the RSI crosses below 30 (indicating oversold conditions), and a sell signal is generated when the RSI crosses above 70 (indicating overbought conditions). The resulting DataFrame includes the closing price, RSI, and buy/sell signal prices for each day.

Please note that this is a very basic implementation of the RSI strategy and may not be suitable for live trading without further refinement and testing. Also, the `yfinance` library used here is a third-party library that is not officially supported by Yahoo Finance, so it may not always work as expected.