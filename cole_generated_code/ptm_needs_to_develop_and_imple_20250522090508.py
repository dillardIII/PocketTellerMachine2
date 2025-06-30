from ghost_env import INFURA_KEY, VAULT_ADDRESS
Sure, here is a simple example of a Python code that implements two basic trading strategies: Mean Reversion and Momentum. This is a simple simulation and doesn't involve real money. For real trading strategies, you would need to use APIs provided by your brokerage, which can be complex and risky.

```python
import numpy as np
import pandas as pd

# Assuming we have a DataFrame 'df' with 'Close' prices of a stock

# Mean Reversion Strategy
def mean_reversion(df):
    # Calculate the mean of the past 20 days
    mean_20 = df['Close'].rolling(20).mean()
    
    # Buy when the price is 2% less than the mean of the past 20 days
    df['Buy_Signal'] = np.where(df['Close'] < mean_20 * 0.98, 1, 0)
    
    # Sell when the price is 2% more than the mean of the past 20 days
    df['Sell_Signal'] = np.where(df['Close'] > mean_20 * 1.02, 1, 0)
    
    return df

# Momentum Strategy
def momentum(df):
    # Calculate the difference in price from the past 20 days
    momentum_20 = df['Close'].diff(20)
    
    # Buy when the momentum is positive
    df['Buy_Signal'] = np.where(momentum_20 > 0, 1, 0)
    
    # Sell when the momentum is negative
    df['Sell_Signal'] = np.where(momentum_20 < 0, 1, 0)
    
    return df

# Applying the strategies to the DataFrame
df_mr = mean_reversion(df)
df_momentum = momentum(df)
```

This code calculates buy and sell signals based on the strategies. In a real-world scenario, you would need to consider transaction costs, slippage, risk management, etc. Also, these strategies are very simple and may not be profitable in real trading. Always backtest your strategies before live trading.