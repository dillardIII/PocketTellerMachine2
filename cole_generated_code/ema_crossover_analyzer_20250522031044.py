from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple Python code snippet that uses the `pandas` library to calculate the Exponential Moving Average (EMA) and analyze EMA crossover for a given stock price data. This code assumes that you have a pandas DataFrame `df` with 'Close' prices.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your DataFrame and it includes 'Close' prices.

def calculate_ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def ema_crossover(data, short_window, long_window):
    short_EMA = calculate_ema(data, short_window)
    long_EMA = calculate_ema(data, long_window)

    # Create signals
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    signals['short_ema'] = short_EMA
    signals['long_ema'] = long_EMA

    # Generate trading signals (1: Long position, -1: Short position)
    signals['signal'][short_window:] = np.where(signals['short_ema'][short_window:] > signals['long_ema'][short_window:], 1.0, -1.0)

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Define the short and long windows
short_window = 12
long_window = 26

# Get the EMA crossover signals
signals = ema_crossover(df['Close'], short_window, long_window)

# Plot
plt.figure(figsize=(12,5))
plt.plot(df.index, df['Close'], label='Close Price', color='blue')
plt.plot(df.index, signals['short_ema'], label='Short EMA', color='red')
plt.plot(df.index, signals['long_ema'], label='Long EMA', color='green')
plt.plot(df.index, signals['signal'], label='Signal', color='black', linestyle='--')
plt.legend(loc='best')
plt.show()
```

This code calculates the short and long EMA, generates trading signals based on the crossover of these two EMAs, and plots the close price, short EMA, long EMA, and the trading signals.

Please replace `df` with your actual DataFrame variable and make sure that your DataFrame has a 'Close' column. You may also need to adjust the short and long window parameters according to your needs.

Please note that this is a very basic EMA crossover strategy and might not be profitable in real trading. Always backtest your strategies before live trading.