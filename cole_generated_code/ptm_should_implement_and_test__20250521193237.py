To implement and test new trading strategies, we can create a simple backtesting framework using Python. Here's a simple example:

```python
import pandas as pd
import numpy as np
from datetime import datetime

class TradingStrategy:
    def __init__(self, data):
        self.data = data
        self.buy_signals = []
        self.sell_signals = []

    def generate_signals(self):
        raise NotImplementedError

class MovingAverageCrossover(TradingStrategy):
    def __init__(self, data, short_window, long_window):
        super().__init__(data)
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self):
        signals = pd.DataFrame(index=self.data.index)
        signals['signal'] = 0.0

        # Create short simple moving average over the short window
        signals['short_mavg'] = self.data['Close'].rolling(window=self.short_window, min_periods=1, center=False).mean()

        # Create long simple moving average over the long window
        signals['long_mavg'] = self.data['Close'].rolling(window=self.long_window, min_periods=1, center=False).mean()

        # Create signals
        signals['signal'][self.short_window:] = np.where(signals['short_mavg'][self.short_window:] 
            > signals['long_mavg'][self.short_window:], 1.0, 0.0)

        # Generate trading orders
        signals['positions'] = signals['signal'].diff()

        self.buy_signals = signals[signals['positions'] == 1.0]
        self.sell_signals = signals[signals['positions'] == -1.0]

        return signals

# Load data
data = pd.read_csv('data.csv', index_col='Date', parse_dates=True)

# Initialize strategy
strategy = MovingAverageCrossover(data, short_window=50, long_window=200)

# Generate signals
signals = strategy.generate_signals()

# Print signals
print(signals)
```

This is a simple moving average crossover strategy. It generates a buy signal when the short-term moving average crosses above the long-term moving average, and a sell signal when the short-term moving average crosses below the long-term moving average.

Please note that this is a very basic example and real-world trading strategies can be much more complex. Also, this code assumes that you have a `data.csv` file with historical price data with 'Close' prices and 'Date' as index. 

You can replace the `MovingAverageCrossover` with any other strategy you want to test. The `generate_signals` method should return a DataFrame with a 'signal' column, where 1 indicates a buy signal and -1 indicates a sell signal.