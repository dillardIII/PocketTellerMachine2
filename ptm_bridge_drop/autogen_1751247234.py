from ghost_env import INFURA_KEY, VAULT_ADDRESS
Below is a simple Python trading strategy that you can expand upon. This example focuses on a momentum-based trading strategy using moving averages.

```python
import pandas as pd
import numpy as np

class MovingAverageCrossoverStrategy:
    def __init__(self, short_window=40, long_window=100):
        self.short_window = short_window
        self.long_window = long_window
        self.signals = None

    def generate_signals(self, prices):
        """Generates trading signals based on moving average crossover."""
        self.signals = pd.DataFrame(index=prices.index)
        self.signals['price'] = prices
        self.signals['signal'] = 0.0

        # Create the short and long simple moving averages (SMA)
        self.signals['short_mavg'] = prices.rolling(window=self.short_window, min_periods=1, center=False).mean()
        self.signals['long_mavg'] = prices.rolling(window=self.long_window, min_periods=1, center=False).mean()

        # Create signals
        self.signals['signal'][self.short_window:] = np.where(
            self.signals['short_mavg'][self.short_window:] > self.signals['long_mavg'][self.short_window:], 1.0, 0.0)

        # Generate trading orders
        self.signals['positions'] = self.signals['signal'].diff()

        return self.signals

# Example usage:
if __name__ == "__main__":
    # Sample price data
    price_data = pd.Series(
        [20, 21, 22, 21, 24, 26, 27, 29, 30, 34, 36, 33, 31, 32, 33, 34, 35, 37, 38, 40],
        index=pd.date_range(start='2023-01-01', periods=20, freq='D')
    )

    strategy = MovingAverageCrossoverStrategy(short_window=3, long_window=5)
    signals = strategy.generate_signals(price_data)

    print(signals)
```

### Key Components:
- **Moving Averages**: The strategy utilizes both short and long Simple Moving Averages (SMA) to determine market trends.
- **Signal Generation**: A buy signal is generated when the short-term SMA crosses above the long-term SMA, and a sell signal when it crosses below.
- **Position Management**: The strategy records positions based on these signals—going from no position (0) to a long position (1), or vice versa.

### Usage:
- **Initialization**: Use the `MovingAverageCrossoverStrategy` class to set the windows for short and long moving averages.
- **Signal Generation**: The `generate_signals` method processes price data to provide trading signals.

This basic structure provides a starting point for a trading strategy and can be expanded with additional logic like stop-loss, take-profit, volume filter, etc. The price data here is just a placeholder; you can replace it with your actual data source.