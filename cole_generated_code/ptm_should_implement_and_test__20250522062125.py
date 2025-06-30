from ghost_env import INFURA_KEY, VAULT_ADDRESS
To implement and test new trading strategies, we can create a simple Python program using Pandas library to analyze financial data. Here's a simple example of a mean reversion strategy:

```python
import pandas as pd
import numpy as np
from pandas_datareader import data as web

def calculate_strategy_returns(data, short_window, long_window):
    # Calculate the moving averages
    data['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    data['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1).mean()

    # Create signals
    data['signal'] = np.where(data['short_mavg'] > data['long_mavg'], 1.0, 0.0)

    # Generate trading orders
    data['positions'] = data['signal'].diff()

    # Calculate daily returns
    data['strategy_returns'] = data['positions'] * data['Close'].pct_change()

    return data

def test_strategy(symbol, start_date, end_date, short_window, long_window):
    # Get the historical data
    data = web.DataReader(symbol, 'yahoo', start_date, end_date)

    # Calculate the strategy returns
    data = calculate_strategy_returns(data, short_window, long_window)

    # Calculate the cumulative returns
    cumulative_returns = (1 + data['strategy_returns']).cumprod()

    return cumulative_returns

# Test the strategy
cumulative_returns = test_strategy('AAPL', '2010-01-01', '2020-12-31', 50, 200)
print(cumulative_returns)
```

This program implements a simple mean reversion strategy, where it goes long when the short moving average is above the long moving average, and goes short when the short moving average is below the long moving average. The strategy returns are calculated based on these trading signals.

Please note that this is a very simplified example and real trading strategies would be much more complex and would also need to take into account transaction costs, slippage, risk management, etc. Also, this strategy uses Yahoo Finance to get the historical data, which might not be accurate or reliable for real trading. For real trading, you would need to use a reliable data source and also implement real-time trading using a trading API.