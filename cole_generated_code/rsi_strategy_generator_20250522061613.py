from ghost_env import INFURA_KEY, VAULT_ADDRESS
The Relative Strength Index (RSI) is a momentum oscillator that measures the speed and change of price movements. It is used to identify overbought or oversold conditions in a market.

Here is a simple Python code to generate RSI strategy:

```python
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

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

def implement_RSI_strategy(data, window):
    rsi = calculate_RSI(data, window)
    data['RSI'] = rsi

    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    signals['signal'][window:] = np.where(data['RSI'][window:] < 30, 1.0, 0.0)
    signals['positions'] = signals['signal'].diff()
    return signals

start_date = datetime(2020,1,1)
end_date = datetime(2021,12,31)

data = yf.download('AAPL', start=start_date, end=end_date)
data['Close'] = data['Adj Close']
data = data.dropna()

window = 14
signals = implement_RSI_strategy(data['Close'], window)

plt.figure(figsize=(15, 5))
plt.plot(data['Close'], color='g', lw=2.)
plt.plot(data.loc[signals.positions == 1.0].index, data['Close'][signals.positions == 1.0], '^', markersize=10, color='m')
plt.plot(data.loc[signals.positions == -1.0].index, data['Close'][signals.positions == -1.0], 'v', markersize=10, color='k')
plt.title('Apple Adj Close Price / RSI Strategy')
plt.show()
```

This code will download the historical data of Apple Inc. from Yahoo Finance, calculate the RSI, generate trading signals based on the RSI (buy when RSI < 30), and plot the strategy on a graph. The green line represents the adjusted close price of Apple, the magenta markers represent the buy signals, and the black markers represent the sell signals.