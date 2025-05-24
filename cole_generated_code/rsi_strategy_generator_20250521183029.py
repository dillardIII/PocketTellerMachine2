Sure, here is a simple implementation of a Relative Strength Index (RSI) strategy generator using Python. This code uses the `pandas` library for data manipulation and `yfinance` to download historical stock price data.

```python
import pandas as pd
import yfinance as yf

def calculate_rsi(data, window):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    average_gain = up.rolling(window).mean()
    average_loss = abs(down.rolling(window).mean())

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def rsi_strategy(ticker, start, end, rsi_window, rsi_threshold):
    data = yf.download(ticker, start=start, end=end)
    data['RSI'] = calculate_rsi(data['Close'], rsi_window)
    
    data['Buy_Signal'] = (data['RSI'] < rsi_threshold)
    data['Sell_Signal'] = (data['RSI'] > rsi_threshold)
    
    return data

# Example usage:
df = rsi_strategy('AAPL', '2020-01-01', '2021-12-31', 14, 30)
print(df)
```

This code first calculates the RSI for a given stock over a specified time period. It then generates a buy signal when the RSI is below a certain threshold (indicating the stock is oversold and potentially undervalued) and a sell signal when the RSI is above this threshold (indicating the stock is overbought and potentially overvalued).

Please note that this is a very simplistic trading strategy and should not be used for real trading without further refinement and testing. The RSI is just one of many indicators that traders use, and it's often used in conjunction with other indicators and strategies.