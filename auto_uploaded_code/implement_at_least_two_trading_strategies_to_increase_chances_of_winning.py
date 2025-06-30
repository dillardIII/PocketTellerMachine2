from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here are two basic trading strategies in implemented Python code:

1. Mean Reversion Strategy: This strategy assumes that the price will return to its mean after a certain period of time.

2. Momentum Strategy: This strategy assumes that the stock price will continue in its current direction based on recent prices.

```python
import numpy as np
import pandas as pd

# Assume we have a data frame 'df' with 'Close' price of a stock
df = pd.read_csv('stock_data.csv')

# Mean Reversion Strategy
def mean_reversion(df, window_size):
    # Calculate the mean of the specified window size
    mean = df['Close'].rolling(window=window_size).mean()

    # Trading signals based on mean reversion strategy
    # Buy signal: When the closing price drops below the mean, assuming price will revert
    # Sell signal: When the closing price goes above the mean, assuming price will revert
    df['Buy_Signal'] = np.where(df['Close'] < mean, 1, 0)
    df['Sell_Signal'] = np.where(df['Close'] > mean, -1, 0)

    return df

# Momentum Strategy
def momentum(df, lookback):
    # Calculate the momentum based on recent prices
    momentum = df['Close'] - df['Close'].shift(lookback)

    # Trading signals based on momentum strategy
    # Buy signal: When the momentum is positive, assuming price will continue going up
    # Sell signal: When the momentum is negative, assuming price will continue going down
    df['Buy_Signal'] = np.where(momentum > 0, 1, 0)
    df['Sell_Signal'] = np.where(momentum < 0, -1, 0)

    return df

# Implement the strategies
df = mean_reversion(df, 14)
df = momentum(df, 3)
```

NB: These are very simple and basic strategies and shouldn't be used in real trading without additional risk management, backtesting and modification to suit the particular needs and risk tolerance of the trader.