The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate an RSI strategy using the `pandas` and `yfinance` libraries.

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
    data['RSI'] = calculate_rsi(data['Close'], window)
    
    # Create signals
    data['Buy_Signal'] = (data['RSI'] < 30) # oversold
    data['Sell_Signal'] = (data['RSI'] > 70) # overbought
    return data

# Download historical data
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Apply RSI strategy
rsi_strategy(data)
```

This script downloads historical data for Apple Inc. (AAPL) from Yahoo Finance, calculates the RSI with a window of 14 days (which is the most commonly used), and generates buy signals when the RSI is below 30 (oversold conditions) and sell signals when the RSI is above 70 (overbought conditions). 

Please note that this is a very simple strategy and should not be used for real trading without further enhancements. For instance, it does not consider transaction costs, slippage, or risk management.