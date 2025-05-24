RSI (Relative Strength Index) is a momentum oscillator that measures the speed and change of price movements. Here is a simple Python RSI strategy:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from datetime import datetime

def calculate_RSI(data, window):
    delta = data.diff()
    up_days = delta.copy()
    up_days[delta<=0]=0.0
    down_days = abs(delta.copy())
    down_days[delta>0]=0.0
    RS_up = up_days.rolling(window).mean()
    RS_down = down_days.rolling(window).mean()
    rsi= 100-100/(1+RS_up/RS_down)
    return rsi

def RSI_Strategy(data, rsi, buy_level, sell_level):
    buy_price = []
    sell_price = []
    rsi_signal = []
    signal = 0

    for i in range(len(data)):
        if rsi[i-1] < buy_level:
            if rsi[i] > buy_level:
                signal = 1
                rsi_signal.append(signal)
                buy_price.append(data[i])
                sell_price.append(np.nan)
                continue
        elif rsi[i-1] > sell_level:
            if rsi[i] < sell_level:
                signal = -1
                rsi_signal.append(signal)
                sell_price.append(data[i])
                buy_price.append(np.nan)
                continue
        rsi_signal.append(0)
        buy_price.append(np.nan)
        sell_price.append(np.nan)
        
    return buy_price, sell_price, rsi_signal

# Get data
start = datetime(2020, 1, 1)
end = datetime.now()
data = web.DataReader('AAPL', 'yahoo', start, end)['Close']

# Calculate RSI
window = 14
rsi = calculate_RSI(data, window)
buy_level = 30
sell_level = 70
buy_price, sell_price, rsi_signal = RSI_Strategy(data, rsi, buy_level, sell_level)

# Plot
plt.figure(figsize=(12,5))
plt.plot(data)
plt.plot(data.index, buy_price, marker='^', markersize=10, color='g', label='buy signal')
plt.plot(data.index, sell_price, marker='v', markersize=10, color='r', label='sell signal')
plt.title('Apple price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.grid()
plt.show()
```

In this example, we got Apple's historical price from Yahoo finance and calculated RSI with a window of 14 days. We set the buy level at 30 and the sell level at 70, which are typical values used in RSI strategies. Then we generated and plotted the buy/sell signals according to these levels. 

You can specify your own ticker, start date, end date, window, buy level, and sell level to generate a personalized RSI strategy.