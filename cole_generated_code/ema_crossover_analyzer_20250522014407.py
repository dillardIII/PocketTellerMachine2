from ghost_env import INFURA_KEY, VAULT_ADDRESS
Here is a simple Python code that uses the `pandas` library to calculate the Exponential Moving Average (EMA) and analyze the crossover points.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover(data, short_window, long_window):
    short_ema = calculate_ema(data, short_window)
    long_ema = calculate_ema(data, long_window)

    buy_signals = (short_ema > long_ema) & (short_ema.shift() < long_ema.shift())
    sell_signals = (short_ema < long_ema) & (short_ema.shift() > long_ema.shift())

    return buy_signals, sell_signals

# Assume we have a DataFrame 'df' with 'Close' prices
df = pd.DataFrame(np.random.rand(100), columns=['Close'])

short_window = 12
long_window = 26

buy_signals, sell_signals = ema_crossover(df['Close'], short_window, long_window)

plt.figure(figsize=(12,5))
plt.plot(df.index, df['Close'], label='Close Price', color='blue')
plt.plot(df.index, calculate_ema(df['Close'], short_window), label='Short EMA', color='red')
plt.plot(df.index, calculate_ema(df['Close'], long_window), label='Long EMA', color='green')
plt.scatter(df.index, df['Close'][buy_signals], color='green', marker='^', alpha=1)
plt.scatter(df.index, df['Close'][sell_signals], color='red', marker='v', alpha=1)
plt.title('EMA Crossover')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend(loc='upper left')
plt.show()
```

This code calculates the EMA for a short window and a long window, then it finds the points where the short EMA crosses the long EMA. These points are potential buy and sell signals. The code also plots the close price, the two EMAs and the buy/sell signals. Please replace the DataFrame 'df' with your actual data.