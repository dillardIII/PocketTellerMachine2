from ghost_env import INFURA_KEY, VAULT_ADDRESS
To develop a trading strategy, we need to define a set of rules to guide our trading decisions. This could be based on various factors such as moving averages, momentum indicators, market trends, etc. 

Here is a simple Python code using pandas library to implement a moving average crossover strategy. This strategy is based on two moving averages, a short-term (fast) and a long-term (slow). The basic idea is to buy when the fast moving average crosses above the slow moving average and sell when the fast moving average crosses below the slow moving average.

```python
import pandas as pd
import numpy as np
import yfinance as yf

# Download historical data for required stocks
ticker = "AAPL"
ticker_data = yf.download(ticker,'2020-01-01','2021-12-31')

# Calculate moving averages
short_window = 20
long_window = 100

signals = pd.DataFrame(index=ticker_data.index)
signals['signal'] = 0.0

# Short moving average
signals['short_mavg'] = ticker_data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Long moving average
signals['long_mavg'] = ticker_data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create signals
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] 
                                            > signals['long_mavg'][short_window:], 1.0, 0.0)   

# Generate trading orders
signals['positions'] = signals['signal'].diff()

# Print `signals`
print(signals)
```

In this code, we first download the historical data for the required stock using the `yfinance` library. Then we calculate the short-term and long-term moving averages. We then create a signal when the short moving average crosses the long moving average. A buy signal is generated when the short moving average is greater than the long moving average and a sell signal is generated when the short moving average is less than the long moving average.

Please note that this is a very basic trading strategy and may not be profitable in real trading. It's always recommended to backtest any strategy before live trading. Also, this strategy doesn't take into account transaction costs, slippage, etc. which could significantly impact the performance.