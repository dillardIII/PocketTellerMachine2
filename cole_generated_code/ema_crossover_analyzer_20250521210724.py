Here is a simple Python code to implement an EMA (Exponential Moving Average) Crossover Analyzer. This code uses the `pandas` library to calculate the EMA and `matplotlib` to plot the results.

```python
import pandas as pd
import matplotlib.pyplot as plt

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover_analyzer(data, short_window, long_window):
    # Calculate short and long EMA
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

# Define EMA windows
short_window = 12
long_window = 26

# Run EMA crossover analyzer
signals = ema_crossover_analyzer(data['Close'], short_window, long_window)

# Plot
plt.figure(figsize=(15, 10))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(signals['short_ema'], label='Short EMA', color='red')
plt.plot(signals['long_ema'], label='Long EMA', color='green')
plt.plot(signals.loc[signals.positions == 1.0].index, signals.short_ema[signals.positions == 1.0], '^', markersize=10, color='m')
plt.plot(signals.loc[signals.positions == -1.0].index, signals.short_ema[signals.positions == -1.0], 'v', markersize=10, color='k')
plt.title('EMA Crossover')
plt.legend()
plt.show()
```

This code assumes that you have a CSV file named 'data.csv' with a 'Close' column for the closing prices. The `ema_crossover_analyzer` function calculates the short and long EMA, generates trading signals based on the crossover, and returns a DataFrame with the signals and EMA values.

The plot shows the closing prices, the short and long EMA, and the buy/sell signals. The '^' markers indicate a buy signal (short EMA crosses above long EMA), and the 'v' markers indicate a sell signal (short EMA crosses below long EMA).