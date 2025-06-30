from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple Python code that simulates a basic trading strategy using moving averages. This strategy will increase the number of trades by trading every time the short term moving average crosses the long term moving average.

```python
import pandas as pd
import numpy as np

class TradingStrategy:
    def __init__(self, short_window=50, long_window=200):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, df):
        # Create short simple moving average over the short window
        df['short_mavg'] = df['Close'].rolling(window=self.short_window, min_periods=1, center=False).mean()

        # Create long simple moving average over the long window
        df['long_mavg'] = df['Close'].rolling(window=self.long_window, min_periods=1, center=False).mean()

        # Create signals
        df['signal'] = np.where(df['short_mavg'] > df['long_mavg'], 1.0, 0.0)

        # Generate trading orders
        df['positions'] = df['signal'].diff()

        return df

# Test the strategy with some data
df = pd.read_csv('your_data.csv')  # replace with your data file
strategy = TradingStrategy()
df = strategy.generate_signals(df)

# Print the DataFrame
print(df)
```

This code assumes that you have a DataFrame `df` with a 'Close' column for closing prices. It calculates short and long term moving averages and creates a 'signal' column where it marks 1.0 when the short term average is above the long term average (indicating a buy signal) and 0.0 otherwise. It then calculates the difference in these signals to generate 'positions', which represent trading orders. A positive difference indicates a buy order and a negative difference indicates a sell order.

Please note that this is a very basic trading strategy and might not be profitable in real-world trading. It's recommended to use more sophisticated strategies and risk management techniques in live trading.