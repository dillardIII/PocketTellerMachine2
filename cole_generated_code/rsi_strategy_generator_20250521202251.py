The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market.

Here is a simple Python code using the `pandas` and `yfinance` libraries to generate a basic RSI strategy:

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

def rsi_strategy(data, window=14):
    rsi = calculate_rsi(data['Close'], window)
    data['RSI'] = rsi

    # Create signals
    data['Buy_Signal'] = (rsi < 30)
    data['Sell_Signal'] = (rsi > 70)
    return data

# Download historical data
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Apply the RSI strategy
rsi_strategy(data)
```

In this code, we first calculate the RSI for the closing prices of the stock. We then add two new columns to our DataFrame: `Buy_Signal` and `Sell_Signal`. These columns are True when the RSI is below 30 (indicating the stock is oversold and it might be a good time to buy) and above 70 (indicating the stock is overbought and it might be a good time to sell), respectively.

Please note that this is a very basic strategy and should not be used for real trading without further improvements and testing. Always do your own research before trading in the stock market.