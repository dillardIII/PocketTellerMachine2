from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market. Here is a simple Python code to generate a trading strategy based on RSI:

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

def RSI_Strategy(data):
    # Calculate RSI
    data['RSI'] = calculate_RSI(data)

    # Create signals
    data['Buy_Signal'] = np.where((data['RSI'] < 30), 1, 0)  # Oversold condition
    data['Sell_Signal'] = np.where((data['RSI'] > 70), 1, 0)  # Overbought condition

    return data

# Download historical data
data = yf.download('AAPL', start='2020-01-01', end='2022-12-31')

# Apply RSI strategy
RSI_Strategy(data)
```

In this code, we first calculate the RSI for a given period (default is 14 days). Then, we generate trading signals based on the RSI: if the RSI is below 30, we generate a buy signal (since the asset is oversold), and if the RSI is above 70, we generate a sell signal (since the asset is overbought).

Please note that this is a very simple strategy and may not be profitable in real trading. Always backtest your strategies before using them in live trading.