Sure, here's a simple Python code that uses the `pandas` library to calculate the Exponential Moving Average (EMA) and analyze the EMA crossover for a given dataset.

```python
import pandas as pd
import matplotlib.pyplot as plt

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def analyze_ema_crossover(data, short_window, long_window):
    short_ema = calculate_ema(data, short_window)
    long_ema = calculate_ema(data, long_window)

    # Create signals
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    signals['short_ema'] = short_ema
    signals['long_ema'] = long_ema

    # Generate trading signals (1 for buy, -1 for sell)
    signals['signal'][short_window:] = np.where(signals['short_ema'][short_window:] > signals['long_ema'][short_window:], 1.0, -1.0)

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Load data
data = pd.read_csv('data.csv')  # replace with your data file

# Analyze EMA crossover
signals = analyze_ema_crossover(data['Close'], 12, 26)  # replace 'Close' with your column name

# Plot
plt.figure(figsize=(15, 10))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(signals['short_ema'], label='Short EMA', color='red')
plt.plot(signals['long_ema'], label='Long EMA', color='green')
plt.plot(signals.loc[signals.positions == 1.0].index, signals.short_ema[signals.positions == 1.0], '^', markersize=10, color='m')
plt.plot(signals.loc[signals.positions == -1.0].index, signals.short_ema[signals.positions == -1.0], 'v', markersize=10, color='k')
plt.title('EMA Crossover')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()
```

This code first calculates the short and long EMA for the given data. Then it generates trading signals based on the EMA crossover: it signals to buy when the short EMA crosses above the long EMA, and to sell when the short EMA crosses below the long EMA. Finally, it plots the close price, the short and long EMA, and the buy/sell signals.

Please replace `'data.csv'` with your actual data file, and `'Close'` with the actual column name that contains the price data. Also, adjust the short and long window parameters as needed.