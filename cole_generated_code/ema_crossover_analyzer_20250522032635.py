from ghost_env import INFURA_KEY, VAULT_ADDRESS
To complete this task, we'll need to use the pandas library in Python to calculate the Exponential Moving Average (EMA) and then analyze the crossover points.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover(data, short_window, long_window):
    short_ema = calculate_ema(data, short_window)
    long_ema = calculate_ema(data, long_window)

    buy_signals = (short_ema > long_ema) & (short_ema.shift(1) < long_ema.shift(1))
    sell_signals = (short_ema < long_ema) & (short_ema.shift(1) > long_ema.shift(1))

    return buy_signals, sell_signals

# Assuming 'data' is a pandas DataFrame and 'price' is the column with the price information
data = pd.DataFrame(np.random.rand(100), columns=['price'])

short_window = 12
long_window = 26

buy_signals, sell_signals = ema_crossover(data['price'], short_window, long_window)

plt.figure(figsize=(12,5))
plt.plot(data['price'], label='Price', color='blue')
plt.plot(data['price'][buy_signals], '^', markersize=10, color='g', label='buy signal')
plt.plot(data['price'][sell_signals], 'v', markersize=10, color='r', label='sell signal')
plt.title('EMA Crossover')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.grid()
plt.show()
```

This script calculates the EMA for the given short and long windows, identifies the crossover points, and plots the price along with the buy and sell signals. The buy signals are represented by green up arrows, and the sell signals are represented by red down arrows.