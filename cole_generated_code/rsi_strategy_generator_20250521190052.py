The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate an RSI strategy using the pandas library.

```python
import pandas as pd
import numpy as np
import yfinance as yf

def calculate_RSI(data, window):
    delta = data.diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0

    average_gain = up.rolling(window=window).mean()
    average_loss = abs(down.rolling(window=window).mean())

    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def RSI_Strategy(data, window=14):
    # Calculate RSI
    rsi = calculate_RSI(data['Close'], window)
    data['RSI'] = rsi

    # Create signals
    data['Buy_Signal'] = np.where((data['RSI'] < 30), 1, 0)  # oversold condition
    data['Sell_Signal'] = np.where((data['RSI'] > 70), -1, 0)  # overbought condition

    return data

# Download historical data
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Generate RSI strategy
RSI_Strategy(data)
```

This code first calculates the RSI for a given window (default is 14 days, as is common in RSI analysis). It then generates trading signals based on the RSI: a buy signal is generated when the RSI is below 30 (indicating an oversold condition), and a sell signal is generated when the RSI is above 70 (indicating an overbought condition). The code uses the yfinance library to download historical data for a specific ticker symbol (in this case, AAPL for Apple Inc.).