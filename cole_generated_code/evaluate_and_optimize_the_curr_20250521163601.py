from ghost_env import INFURA_KEY, VAULT_ADDRESS
Due to the complexity of trading algorithms, without specifics, it's hard to give a proper sample code. However, I can give you a generic structure of evaluating and optimizing a trading algorithm using python and few libraries such as Pandas and Quantopian.

```python
import pandas as pd
import numpy as np
from quantopian.pipeline import Pipeline
from quantopian.research import run_pipeline
from quantopian.pipeline.data import USEquityPricing
from quantopian.pipeline.factors import SimpleMovingAverage

# Define the trading strategy
class Strategy:
    def __init__(self, short_window=30, long_window=60):
        self.short_window = short_window
        self.long_window = long_window        

    # Trading logic
    def compute_signals(self, historical_prices):
        signals = pd.DataFrame(index=historical_prices.index)
        signals['signal'] = 0.0

        # Create short simple moving average over the short window
        signals['short_mavg'] = historical_prices['Close'].rolling(window=self.short_window, min_periods=1).mean()

        # Create long simple moving average over the long window
        signals['long_mavg'] = historical_prices['Close'].rolling(window=self.long_window, min_periods=1).mean()

        # Create signals
        signals['signal'][self.short_window:] = np.where(signals['short_mavg'][self.short_window:] 
            > signals['long_mavg'][self.short_window:], 1.0, 0.0)   

        # Generate trading orders
        signals['positions'] = signals['signal'].diff()

        return signals

# Evaluate the strategy with historical data
historical_prices = # Insert your historical data here
strategy = Strategy(short_window=40, long_window=100)
signals = strategy.compute_signals(historical_prices)

# Optimize the strategy
from scipy.optimize import brute
def optimize_strategy(params):
    strategy = Strategy(short_window=int(params[0]), long_window=int(params[1]))
    signals = strategy.compute_signals(historical_prices)
    return -compute_portfolio_value(signals)    # Assuming that this function is available

grid = (slice(30, 60, 1), slice(60, 120, 1))    # Define range for short_window and long_window
optimal_params = brute(optimize_strategy, grid, finish=None)

# Print the optimal parameters
print(f'Optimal Parameters: short_window={int(optimal_params[0])}, long_window={int(optimal_params[1])}')
```
Please modify and customize the above code according to your specific needs and the actual data source you will be using.

Also, you'll need to interact with actual market data. It's possible to use APIs such as the `yfinance` package or directly from brokerage accounts like Interactive Brokers or Alpaca Markets. Only backtesting is done here in this script. Note that this is a simplified algorithm example and it may not be profitable or appropriate for actual trading. Real trading algorithms incorporate risk management, multiple indicators, and market regime filters among others.