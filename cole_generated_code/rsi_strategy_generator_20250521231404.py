The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here's a simple Python code that generates a trading strategy based on RSI.

```python
import pandas as pd
import numpy as np
import yfinance as yf
from ta import add_all_ta_features
from ta.utils import dropna
from ta.momentum import RSIIndicator

def calculate_RSI(data, period=14):
    close = data['Close']
    delta = close.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    average_gain = up.rolling(window=period).mean()
    average_loss = abs(down.rolling(window=period).mean())

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def implement_RSI_strategy(data, rsi_period, buy_threshold, sell_threshold):
    data['RSI'] = calculate_RSI(data, rsi_period)
    data['Buy_Signal'] = np.where(data['RSI'] < buy_threshold, 1, 0)
    data['Sell_Signal'] = np.where(data['RSI'] > sell_threshold, -1, 0)
    return data

# Download historical data
data = yf.download('AAPL', start='2020-01-01', end='2020-12-31')

# Implement RSI strategy
data = implement_RSI_strategy(data, rsi_period=14, buy_threshold=30, sell_threshold=70)

# Print data
print(data)
```

In this code, we first calculate the RSI for the given period. Then, we generate buy signals when the RSI goes below the buy threshold (indicating oversold conditions) and sell signals when the RSI goes above the sell threshold (indicating overbought conditions). The thresholds are typically set at 30 and 70, respectively, but you can adjust these according to your trading strategy.

Please note that this is a very simplistic trading strategy and doesn't take into account many factors that could influence the performance of a real trading strategy. Always backtest your strategies before using them in live trading.