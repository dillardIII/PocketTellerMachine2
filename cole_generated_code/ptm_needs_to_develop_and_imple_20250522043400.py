from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here's a simple example of a Python code that implements two basic trading strategies: Mean Reversion and Momentum. Please note that this is a very simplified version and real trading strategies should consider more factors and be tested thoroughly.

```python
import pandas as pd
import numpy as np

class Strategy:
    def __init__(self, data):
        self.data = data

    def mean_reversion(self, window):
        # Calculate the mean of the past 'window' days
        mean = self.data.rolling(window).mean()

        # Create a signal when the price is below the mean
        signal = np.where(self.data < mean, 1, 0)

        return signal

    def momentum(self, window):
        # Calculate the difference in price over the past 'window' days
        momentum = self.data - self.data.shift(window)

        # Create a signal when the momentum is positive
        signal = np.where(momentum > 0, 1, 0)

        return signal

# Assume we have price data in a pandas DataFrame
data = pd.DataFrame()

# Initialize the strategy
strategy = Strategy(data)

# Implement the mean reversion strategy with a window of 10 days
mean_reversion_signal = strategy.mean_reversion(10)

# Implement the momentum strategy with a window of 5 days
momentum_signal = strategy.momentum(5)
```

In this code, the `mean_reversion` method implements a mean reversion strategy, which assumes that the price will revert to its mean over time. It creates a trading signal when the price is below the mean.

The `momentum` method implements a momentum strategy, which assumes that the price will continue in the same direction. It creates a trading signal when the momentum is positive.

Please note that in real trading, you would also need to consider transaction costs, risk management, portfolio optimization and many other factors.