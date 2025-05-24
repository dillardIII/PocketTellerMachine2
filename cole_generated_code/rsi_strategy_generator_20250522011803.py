The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market.

Here is a simple Python code to generate RSI strategy:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

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
    rsi = calculate_rsi(data['Close'], window)
    data['RSI'] = rsi

    data['Buy_Signal'] = np.where((data['RSI'] < 30), 1, 0)
    data['Sell_Signal'] = np.where((data['RSI'] > 70), -1, 0)
    return data

# Download historical data as dataframe
data = pdr.get_data_yahoo("AAPL", start="2020-01-01", end="2022-12-31")

# Generate RSI strategy
rsi_strategy(data)
print(data)
```

In this code, we first calculate the RSI by taking the average gain and average loss over a specified window (default is 14 days). Then, we generate buy signals when the RSI is below 30 (oversold conditions) and sell signals when the RSI is above 70 (overbought conditions).

Please make sure to install necessary libraries by using pip:
```bash
pip install pandas numpy yfinance pandas-datareader
```

Remember this is a very basic strategy and should be used as a starting point. Always backtest your strategies before live trading.