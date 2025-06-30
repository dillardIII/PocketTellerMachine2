from ghost_env import INFURA_KEY, VAULT_ADDRESS
To implement and test new trading strategies, we can use Python's pandas library for data manipulation and analysis. We will also use numpy for numerical computations. The following is a simple example of a moving average crossover strategy, which is one of the most common systematic trading strategies.

Please note that this is a very simplified example and real-world trading strategies are much more complex and require careful consideration of many factors.

```python
import pandas as pd
import numpy as np

class TradingStrategy:
    def __init__(self, short_window, long_window):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data):
        signals = pd.DataFrame(index=data.index)
        signals['signal'] = 0.0

        # Create short simple moving average over the short window
        signals['short_mavg'] = data['Close'].rolling(window=self.short_window, min_periods=1, center=False).mean()

        # Create long simple moving average over the long window
        signals['long_mavg'] = data['Close'].rolling(window=self.long_window, min_periods=1, center=False).mean()

        # Create signals
        signals['signal'][self.short_window:] = np.where(signals['short_mavg'][self.short_window:] 
            > signals['long_mavg'][self.short_window:], 1.0, 0.0)   

        # Generate trading orders
        signals['positions'] = signals['signal'].diff()

        return signals

# Test the strategy with some data
data = pd.read_csv('path_to_your_data.csv')  # replace with the path to your data file
strategy = TradingStrategy(40, 100)
signals = strategy.generate_signals(data)

print(signals)
```

In this example, we're using a simple moving average crossover strategy, where we generate a trading signal when the short-term moving average crosses the long-term moving average. This is a very basic strategy and in practice, you would likely use more complex strategies and consider more factors.

Please replace `'path_to_your_data.csv'` with the actual path to your data file. The data file should be a CSV file with a 'Close' column that represents the closing prices of the stock.