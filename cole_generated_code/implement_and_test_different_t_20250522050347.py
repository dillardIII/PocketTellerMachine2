from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, I can provide you with a simple Python code that implements two different trading strategies: Moving Average Crossover and Mean Reversion. 

Please note that this is a simplified version and real-world trading strategies can be much more complex and sophisticated. 

Also, this code assumes that you have historical price data in a pandas dataframe named 'df' with 'Close' column representing closing prices.

```python
import pandas as pd
import numpy as np

# Moving Average Crossover Strategy
def moving_average_crossover(df, short_window=40, long_window=100):
    signals = pd.DataFrame(index=df.index)
    signals['signal'] = 0.0

    # Short moving average
    signals['short_mavg'] = df['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

    # Long moving average
    signals['long_mavg'] = df['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

    # Create signals
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                                > signals['long_mavg'][short_window:], 1.0, 0.0)   

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Mean Reversion Strategy
def mean_reversion(df, window=40):
    signals = pd.DataFrame(index=df.index)
    signals['signal'] = 0.0

    # Compute the mean and standard deviation of prices over the window period
    signals['mean'] = df['Close'].rolling(window=window, min_periods=1, center=False).mean()
    signals['std'] = df['Close'].rolling(window=window, min_periods=1, center=False).std()

    # Create signals
    signals['signal'] = np.where(df['Close'] < (signals['mean'] - 1.5*signals['std']), 1.0, 0.0)

    # Generate trading orders
    signals['positions'] = signals['signal'].diff()

    return signals

# Test the strategies
df = pd.read_csv('historical_prices.csv')  # replace with your actual file

mac_signals = moving_average_crossover(df)
mr_signals = mean_reversion(df)

print(mac_signals)
print(mr_signals)
```

In the moving average crossover strategy, when the short moving average crosses above the long moving average, it generates a buy signal. When the short moving average crosses below the long moving average, it generates a sell signal.

In the mean reversion strategy, when the price falls more than 1.5 standard deviations below the mean, it generates a buy signal, assuming that the price will revert to the mean.

You can adjust the parameters of these strategies to fit your needs. Also, remember that these strategies do not take into account transaction costs or slippage.