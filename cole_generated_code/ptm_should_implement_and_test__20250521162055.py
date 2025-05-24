Before we can start with the task, you need to be aware that implementing trading strategies is a complex task that requires analysis of financial markets and careful code structuring. Also, we need trading data and possibly access to an online broker, which we obviously cannot realize in this context.

But I can show you a basic simulation of a trading strategy using a simple moving average (SMA) crossover strategy with artificial data:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Generate Random Trading Data for 1000 days
np.random.seed(0)
dates = pd.date_range('2010-01-01', periods=1000)
data = pd.DataFrame(np.random.randn(1000, 1)*2 + 10, index=dates, columns=['Price'])
data['Return'] = data['Price'].pct_change()

# Simple Moving Average (SMA) Strategy
short_window = 40
long_window = 100

signals = pd.DataFrame(index=data.index)
signals['signal'] = 0.0

# Create short simple moving average over the short window
signals['short_mavg'] = data['Price'].rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
signals['long_mavg'] = data['Price'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Plotting the Price and SMA strategy
plt.figure(figsize=(10,5))
plt.title('Trading strategy - Moving averages crossover')
plt.plot(data['Price'], 'k', label='Price')
plt.plot(signals['short_mavg'], 'r', label='Short Moving Average')
plt.plot(signals['long_mavg'], 'g', label='Long Moving Average')
plt.plot(signals.loc[signals.positions == 1.0].index, 
         signals.short_mavg[signals.positions == 1.0],
         '^', markersize=10, color='m', label='buy')
plt.plot(signals.loc[signals.positions == -1.0].index, 
         signals.short_mavg[signals.positions == -1.0],
         'v', markersize=10, color='k', label='sell')
plt.ylabel('Price in $')
plt.xlabel('Date')
plt.legend(loc='best')
plt.grid(True)
plt.show()
```
This Python code will generate a random stock price for 1000 days and apply a SMA crossover strategy. When the short-term average cross over the long-term average, it indicates the buy points. When the short-term average cross below the long-term average, it indicates sell points. 

Remember every strategy doesn't guarantee returns and has different results under different situations. So, a strategy should be backtested properly with historical data before deploying in the live market. Also, it should be used with proper risk management and money management techniques.