Sure, here's a simple implementation of a Relative Strength Index (RSI) strategy generator in Python using the `pandas` and `yfinance` libraries. This code will fetch historical data for a given stock symbol, calculate the RSI, and generate a simple trading strategy based on the RSI.

```python
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override() 

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

def generate_strategy(data):
    buy_signals = (data['RSI'] < 30)
    sell_signals = (data['RSI'] > 70)

    data['Buy_Signal'] = buy_signals
    data['Sell_Signal'] = sell_signals
    return data

def rsi_strategy(symbol, window=14):
    data = pdr.get_data_yahoo(symbol, start="2020-01-01", end="2022-12-31")
    data['RSI'] = calculate_rsi(data['Close'], window)
    strategy = generate_strategy(data)
    return strategy

# Example usage:
df = rsi_strategy("AAPL")
print(df)
```

This code will print a DataFrame with the historical price data for the stock, along with the calculated RSI and the generated buy/sell signals. The buy signals are generated when the RSI drops below 30 (indicating the stock is oversold), and the sell signals are generated when the RSI rises above 70 (indicating the stock is overbought).

Please note that this is a very simplistic trading strategy and should not be used for actual trading without further refinement and testing.