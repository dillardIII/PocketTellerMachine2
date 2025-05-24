Sure, here's a simple implementation of an RSI (Relative Strength Index) strategy generator in Python. This code uses the `pandas` library to handle data and the `yfinance` library to download stock price data.

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

def rsi_strategy(ticker, start, end, rsi_window, rsi_upper, rsi_lower):
    data = yf.download(ticker, start=start, end=end)
    data['RSI'] = calculate_rsi(data['Close'], rsi_window)

    data['Buy_Signal'] = (data['RSI'] < rsi_lower)
    data['Sell_Signal'] = (data['RSI'] > rsi_upper)

    return data

# Test the strategy
data = rsi_strategy('AAPL', '2020-01-01', '2021-12-31', 14, 70, 30)
print(data)
```

This code first calculates the RSI for the given ticker symbol over the specified date range. It then generates buy signals when the RSI drops below the lower threshold and sell signals when the RSI rises above the upper threshold.

Please note that this is a very basic implementation of an RSI strategy. In a real-world scenario, you would likely want to incorporate additional factors and safeguards. For example, you might want to consider the overall trend of the market or the specific stock, use stop-loss orders to limit potential losses, and so forth.