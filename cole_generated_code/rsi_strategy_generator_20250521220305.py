Sure, here's a simple Python code for generating a Relative Strength Index (RSI) strategy. This code uses the `pandas` library for data manipulation and `yfinance` to download stock price data.

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

def rsi_strategy(data, window=14):
    # Calculate RSI
    rsi = calculate_rsi(data['Close'], window)
    data['RSI'] = rsi

    # Create signals
    data['Buy_Signal'] = (rsi < 30)
    data['Sell_Signal'] = (rsi > 70)
    return data

# Download historical data
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Apply RSI strategy
rsi_strategy(data)
```

This code first defines a function to calculate the RSI, then a function to generate buy/sell signals based on the RSI. A buy signal is generated when the RSI is below 30 (indicating the stock is oversold), and a sell signal is generated when the RSI is above 70 (indicating the stock is overbought).

Please note that this is a very simple strategy and may not be profitable in real trading. Always backtest your strategies before live trading.